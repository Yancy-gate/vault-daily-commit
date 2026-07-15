---
name: cursor-daily-log
description: >-
  Capture today's Cursor Agent sessions into Obsidian as day-level theme
  threads plus one-liner session summaries (not raw quotes). Use when the
  user asks for Cursor日志, 今日 Cursor 摘要, 抓取今天会话, 写 Cursor 日志,
  nightly transcript summary, or 主线总结今天干了什么.
---

# cursor-daily-log

把本机 Cursor Agent **当天**会话沉淀进 Obsidian：

1. **今日主线**（2～5 条宏观主题）
2. **各会话摘要**（每会话一句）

运行时脚本在同 skill 的 `scripts/`；Windows 推荐装到 `~/.cursor/scripts/cursor-daily-log/` 并注册计划任务。

配置说明见 [config.example.json](config.example.json)（安装后复制为 `config.json`）。

人类提示词：[prompts.md](prompts.md)

## Workflow（对话触发）

```
- [ ] 1. 取当天日期（Windows: Get-Date -Format yyyy-MM-dd）
- [ ] 2. 确认已安装 scripts（~/.cursor/scripts/cursor-daily-log 或本 skill/scripts）
- [ ] 3. 确认 config.json 有 vault_path / python_path
- [ ] 4. 运行 run.ps1（可加 -Date）
- [ ] 5. 打开生成的 `<log_subdir>/YYYY-MM-DD.md` 给用户看主线
```

### 手动运行

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\.cursor\scripts\cursor-daily-log\run.ps1"
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\.cursor\scripts\cursor-daily-log\run.ps1" -Date YYYY-MM-DD
```

### 注册每晚任务（默认 21:00）

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:USERPROFILE\.cursor\scripts\cursor-daily-log\install-schedule.ps1"
```

任务名：`CursorDailyLogToObsidian`。`LastTaskResult` 应为 `0`；若为 `9009`，检查 `python_path`。

## 摘要链路

`summary.provider: auto`：DeepSeek（`.env` 里 `DEEPSEEK_API_KEY`）→ Ollama → 启发式。

**禁止**把 API Key 写进 git / skill 仓库。

## 与 vault-daily-commit 的关系

| Skill | 做什么 |
|-------|--------|
| `vault-daily-commit` | 安全 commit 每日笔记 + 截图 |
| `cursor-daily-log` | 总结当天 Cursor 会话进 Obsidian 日志 |

可同仓库安装、分工使用。
