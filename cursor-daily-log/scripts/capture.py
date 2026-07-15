#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture today's Cursor Agent sessions into Obsidian logs/Cursor/YYYY-MM-DD.md.

Only includes user turns whose <timestamp> falls on the target local date.
1) Each session → one refined Chinese sentence
2) All sessions → 2–5 macro「今日主线」
Re-running overwrites that day's file (idempotent).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TS_RE = re.compile(r"<timestamp>(.*?)</timestamp>", re.I)
UQ_RE = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.S | re.I)
SCRIPT_DIR = Path(__file__).resolve().parent

SKIP_PREFIXES = (
    "Briefly inform the user about the task result",
    "The following task has finished",
    "<system_notification>",
)

SUMMARY_SYSTEM = (
    "你是日志摘要助手。根据用户当天在 Cursor 里的多条发言，"
    "理解真实意图后，用一句通顺、精炼的中文概括「今天这个会话做了什么」。"
    "要求：只输出这一句话；不要条目、不要引号、不要原话堆砌；"
    "侧重目标与结果/推进方向，可合并多条发言；长度约 30–80 字。"
)

THREADS_SYSTEM = (
    "你是日终复盘助手。下面是用户当天各 Cursor 会话的一句摘要。"
    "请宏观归纳成 2～5 条「主线」（按主题/目标合并，不要按会话逐条复述）。"
    "每条主线一行，格式严格为：`- **主线名**：一句话说明今天在这条线上推进了什么`。"
    "主线名要短（2～8 字）；说明要精炼；可跨项目合并；不要输出其他前后缀。"
)


def load_config() -> dict:
    cfg_path = SCRIPT_DIR / "config.json"
    with cfg_path.open(encoding="utf-8") as f:
        return json.load(f)


def load_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def parse_ts(raw: str, tz: ZoneInfo) -> datetime | None:
    core = raw.split(" (")[0].strip()
    for fmt in (
        "%A, %b %d, %Y, %I:%M %p",
        "%A, %B %d, %Y, %I:%M %p",
    ):
        try:
            return datetime.strptime(core, fmt).replace(tzinfo=tz)
        except ValueError:
            continue
    return None


def extract_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for c in content:
            if isinstance(c, dict) and c.get("type") == "text":
                parts.append(c.get("text") or "")
        return "".join(parts)
    return ""


def humanize_project(project_dir_name: str) -> str:
    """Strip common Cursor project-dir prefixes without hard-coding usernames."""
    name = project_dir_name
    # c-Users-<name>-Projects-foo → foo ; d-Tools-editor-bar → bar
    name = re.sub(r"^[a-z]-Users-[^-]+-Projects-", "", name, count=1)
    name = re.sub(r"^[a-z]-Users-[^-]+-Desktop-", "", name, count=1)
    name = re.sub(r"^[a-z]-Users-[^-]+-", "", name, count=1)
    name = re.sub(r"^[a-z]-Projects-", "", name, count=1)
    name = re.sub(r"^[a-z]-Tools-editor-", "", name, count=1)
    name = re.sub(r"^[a-z]-", "", name, count=1)
    if name == "empty-window":
        return "home / empty-window"
    return name.replace("-", " ")


@dataclass
class Turn:
    dt: datetime
    query: str


@dataclass
class Session:
    session_id: str
    project: str
    path: Path
    turns: list[Turn] = field(default_factory=list)
    summary: str = ""

    @property
    def start(self) -> datetime:
        return self.turns[0].dt

    @property
    def end(self) -> datetime:
        return self.turns[-1].dt


def collect_today_sessions(day: date, tz: ZoneInfo, max_q_chars: int) -> list[Session]:
    projects = Path.home() / ".cursor" / "projects"
    sessions: list[Session] = []
    if not projects.exists():
        return sessions

    for path in projects.rglob("*.jsonl"):
        if "subagents" in path.parts:
            continue
        try:
            session_id = path.stem
            project = path.parents[2].name
        except IndexError:
            continue

        turns: list[Turn] = []
        try:
            raw_lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue

        for line in raw_lines:
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if obj.get("role") != "user":
                continue
            raw = extract_text(obj.get("message", {}).get("content"))
            m = TS_RE.search(raw)
            if not m:
                continue
            dt = parse_ts(m.group(1), tz)
            if not dt or dt.date() != day:
                continue
            qm = UQ_RE.search(raw)
            q = (qm.group(1).strip() if qm else raw.strip())
            q = re.sub(r"\s+", " ", q).strip()
            if not q:
                continue
            if any(q.startswith(p) for p in SKIP_PREFIXES):
                continue
            if len(q) > max_q_chars:
                q = q[: max_q_chars - 1] + "…"
            turns.append(Turn(dt=dt, query=q))

        if turns:
            turns.sort(key=lambda t: t.dt)
            sessions.append(
                Session(
                    session_id=session_id,
                    project=humanize_project(project),
                    path=path,
                    turns=turns,
                )
            )

    sessions.sort(key=lambda s: s.start)
    return sessions


def clip(text: str, n: int) -> str:
    text = text.strip()
    if len(text) <= n:
        return text
    return text[: n - 1] + "…"


def heuristic_summary(session: Session) -> str:
    qs = [t.query.replace("```", "").strip() for t in session.turns if t.query.strip()]
    if not qs:
        return "未记录到有效用户意图。"
    if len(qs) == 1:
        return clip(re.sub(r"\s+", " ", qs[0]), 80)
    ranked = sorted(qs, key=lambda x: (len(x), x), reverse=True)
    head = ranked[0]
    mid = ranked[1] if len(ranked) > 1 else ""
    theme = clip(head, 42)
    if mid and mid[:12] not in theme:
        theme = f"{theme}；兼及{clip(mid, 28)}"
    return f"围绕「{clip(theme, 70)}」推进，共 {len(qs)} 轮对话。"


def build_prompt(session: Session, max_input: int) -> str:
    parts = [
        f"项目：{session.project}",
        f"发言条数：{len(session.turns)}",
        "用户发言（按时间）：",
    ]
    budget = max_input
    for i, t in enumerate(session.turns, 1):
        line = f"{i}. [{t.dt.strftime('%H:%M')}] {t.query}"
        if len(line) > budget:
            line = clip(line, max(40, budget))
        parts.append(line)
        budget -= len(line) + 1
        if budget < 40:
            parts.append(f"…另有 {len(session.turns) - i} 条已省略")
            break
    return "\n".join(parts)


def chat_completions(
    *,
    base_url: str,
    api_key: str,
    model: str,
    user_prompt: str,
    system: str = SUMMARY_SYSTEM,
    single_line: bool = True,
    timeout: float = 60.0,
) -> str | None:
    url = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "temperature": 0.2,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_prompt},
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
        text = body["choices"][0]["message"]["content"].strip()
        text = text.strip().strip("\"'「」")
        if single_line:
            text = re.sub(r"\s+", " ", text).strip()
            if "\n" in text:
                text = text.splitlines()[0].strip()
        else:
            cleaned: list[str] = []
            for line in text.splitlines():
                line = line.strip().lstrip("•").strip()
                if not line or line.startswith("#"):
                    continue
                if not line.startswith("-"):
                    line = "- " + line.lstrip("0123456789.、)） ")
                cleaned.append(line)
            text = "\n".join(cleaned).strip()
        return text or None
    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        KeyError,
        IndexError,
        TimeoutError,
        json.JSONDecodeError,
    ):
        return None


def resolve_deepseek(cfg: dict) -> tuple[str, str, str] | None:
    sum_cfg = cfg.get("summary") or {}
    base = sum_cfg.get("deepseek_base_url", "https://api.deepseek.com")
    model = sum_cfg.get("deepseek_model", "deepseek-chat")
    key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not key:
        env_path = sum_cfg.get("deepseek_env_file") or ""
        if env_path:
            key = load_env_file(Path(env_path)).get("DEEPSEEK_API_KEY", "")
    if not key:
        return None
    return base, key, model


def resolve_ollama(cfg: dict) -> tuple[str, str, str] | None:
    sum_cfg = cfg.get("summary") or {}
    base = sum_cfg.get("ollama_base_url", "http://127.0.0.1:11434/v1")
    model = sum_cfg.get("ollama_model", "qwen2.5-coder:7b")
    return base, "ollama", model


def provider_order(cfg: dict) -> list[str]:
    provider = ((cfg.get("summary") or {}).get("provider") or "auto").lower()
    if provider == "deepseek":
        return ["deepseek", "heuristic"]
    if provider == "ollama":
        return ["ollama", "heuristic"]
    if provider == "heuristic":
        return ["heuristic"]
    return ["deepseek", "ollama", "heuristic"]


def call_with_providers(
    cfg: dict,
    user_prompt: str,
    *,
    system: str,
    single_line: bool,
) -> tuple[str | None, str]:
    for name in provider_order(cfg):
        if name == "heuristic":
            return None, "heuristic"
        if name == "deepseek":
            ds = resolve_deepseek(cfg)
            if not ds:
                continue
            base, key, model = ds
            text = chat_completions(
                base_url=base,
                api_key=key,
                model=model,
                user_prompt=user_prompt,
                system=system,
                single_line=single_line,
            )
            if text:
                return text, "deepseek"
        if name == "ollama":
            ol = resolve_ollama(cfg)
            if not ol:
                continue
            base, key, model = ol
            text = chat_completions(
                base_url=base,
                api_key=key,
                model=model,
                user_prompt=user_prompt,
                system=system,
                single_line=single_line,
                timeout=120.0,
            )
            if text:
                return text, "ollama"
    return None, "heuristic"


def summarize_session(session: Session, cfg: dict) -> tuple[str, str]:
    sum_cfg = cfg.get("summary") or {}
    if not sum_cfg.get("enabled", True):
        return heuristic_summary(session), "heuristic"

    prompt = build_prompt(session, int(sum_cfg.get("max_input_chars", 3500)))
    text, via = call_with_providers(
        cfg,
        prompt,
        system=SUMMARY_SYSTEM,
        single_line=True,
    )
    if text:
        return clip(text, 120), via
    return heuristic_summary(session), "heuristic"


def heuristic_threads(sessions: list[Session]) -> str:
    by_proj: dict[str, list[Session]] = {}
    for s in sessions:
        by_proj.setdefault(s.project, []).append(s)
    lines: list[str] = []
    for proj, group in by_proj.items():
        bits = [g.summary for g in group if g.summary]
        joined = "；".join(bits[:2]) if bits else "有会话活动"
        name = clip(proj.replace("home / ", ""), 8)
        lines.append(f"- **{name}**：{clip(joined, 90)}")
        if len(lines) >= 5:
            break
    return "\n".join(lines) if lines else "- **日常**：当天会话较少，未形成明显主线。"


def summarize_day_threads(sessions: list[Session], cfg: dict) -> tuple[str, str]:
    if not sessions:
        return "- **日常**：今天还没有可记录的 Cursor 会话。", "none"
    if len(sessions) == 1:
        return f"- **主线**：{sessions[0].summary}", "derived"

    sum_cfg = cfg.get("summary") or {}
    if not sum_cfg.get("enabled", True):
        return heuristic_threads(sessions), "heuristic"

    parts = [f"日期会话共 {len(sessions)} 个，摘要如下："]
    for i, s in enumerate(sessions, 1):
        parts.append(
            f"{i}. [{s.start.strftime('%H:%M')}-{s.end.strftime('%H:%M')}] "
            f"{s.project}（{len(s.turns)}条）：{s.summary}"
        )
    text, via = call_with_providers(
        cfg,
        "\n".join(parts),
        system=THREADS_SYSTEM,
        single_line=False,
    )
    if text:
        theme_lines = [ln for ln in text.splitlines() if ln.strip()][:5]
        return "\n".join(theme_lines), via
    return heuristic_threads(sessions), "heuristic"


def render_markdown(
    day: date,
    sessions: list[Session],
    generated_at: datetime,
    providers: list[str],
    threads_md: str,
) -> str:
    lines: list[str] = []
    lines.append("---")
    lines.append(f"date: {day.isoformat()}")
    lines.append("tags:")
    lines.append("  - cursor")
    lines.append("  - 日志")
    lines.append(f"generated: {generated_at.strftime('%Y-%m-%d %H:%M')}")
    lines.append("source: agent-transcripts (today-only)")
    lines.append("format: day-threads-plus-session-oneliners")
    if providers:
        lines.append(f"summary_via: {', '.join(sorted(set(providers)))}")
    lines.append("---")
    lines.append("")
    lines.append(f"# Cursor 日志 {day.isoformat()}")
    lines.append("")
    lines.append(f"> 仅包含 **{day.isoformat()}** 当天有用户发言的会话。")
    lines.append(
        f"> 先按**主线**宏观归纳，再附各会话一句摘要。生成于 {generated_at.strftime('%Y-%m-%d %H:%M')}。"
    )
    lines.append("")

    if not sessions:
        lines.append("今天还没有可记录的 Cursor Agent 会话。")
        lines.append("")
        return "\n".join(lines)

    lines.append(
        f"**会话数：** {len(sessions)}　**发言条数：** {sum(len(s.turns) for s in sessions)}"
    )
    lines.append("")
    lines.append("## 今日主线")
    lines.append("")
    lines.append(threads_md)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 各会话摘要")
    lines.append("")

    for i, s in enumerate(sessions, 1):
        sid_short = s.session_id[:8]
        lines.append(f"### {i}. {s.project} · `{sid_short}`")
        lines.append("")
        lines.append(f"- **时间：** {s.start.strftime('%H:%M')} – {s.end.strftime('%H:%M')}")
        lines.append(f"- **今日发言：** {len(s.turns)} 条")
        lines.append(f"- **摘要：** {s.summary}")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export today's Cursor sessions to Obsidian")
    parser.add_argument(
        "--date",
        help="Target date YYYY-MM-DD (default: today in configured timezone)",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print path and counts only")
    args = parser.parse_args()

    cfg = load_config()
    tz = ZoneInfo(cfg.get("timezone", "Asia/Shanghai"))
    day = date.fromisoformat(args.date) if args.date else datetime.now(tz).date()

    vault = Path(cfg["vault_path"])
    out_dir = vault / cfg.get("log_subdir", "logs/Cursor")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"{day.isoformat()}.md"

    sessions = collect_today_sessions(day, tz, int(cfg.get("max_query_chars", 400)))

    providers: list[str] = []
    for s in sessions:
        summary, via = summarize_session(s, cfg)
        s.summary = summary
        providers.append(via)
        print(f"[{via}] {s.session_id[:8]}: {summary}", flush=True)

    threads_md, threads_via = summarize_day_threads(sessions, cfg)
    providers.append(f"threads:{threads_via}")
    print(f"[threads/{threads_via}]\n{threads_md}", flush=True)

    now = datetime.now(tz)
    md = render_markdown(day, sessions, now, providers, threads_md)

    if args.dry_run:
        print(f"Would write: {out_file}")
        print(f"Sessions: {len(sessions)} turns: {sum(len(s.turns) for s in sessions)}")
        return 0

    out_file.write_text(md, encoding="utf-8")
    print(f"Wrote {out_file}")
    print(f"Sessions: {len(sessions)} turns: {sum(len(s.turns) for s in sessions)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
