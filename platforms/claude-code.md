# Claude Code

## 安装位置（二选一）

| 范围 | 路径 |
|------|------|
| 仅本 vault | `<vault>/.claude/skills/vault-daily-commit/` |
| 所有项目 | `~/.claude/skills/vault-daily-commit/` |

## 安装

```bash
mkdir -p .claude/skills
cp -r skills/vault-daily-commit .claude/skills/
```

```powershell
New-Item -ItemType Directory -Force -Path .claude\skills | Out-Null
Copy-Item -Recurse skills\vault-daily-commit .claude\skills\
```

或 `bash install.sh claude-code` / `install.ps1 -Target claude-code`。

## 使用

在 Claude Code 中打开 **git 仓库根目录**（vault 根），然后：

```text
今天数学笔记写完了，请帮我 commit。（见 prompts.md）
```

或：

```text
使用 vault-daily-commit skill 提交今日笔记。
```

## 验证

```bash
# 在 vault 根
ls .claude/skills/vault-daily-commit/SKILL.md
```

Claude Code 会话内应能按 `vault-config.md` 限定范围执行 git。

## 说明

- 若 vault 已是 claude-obsidian 项目且 `skills/` 在仓库内，也可把本 skill 放在 `skills/vault-daily-commit/`，与 `AGENTS.md` 多 Agent 安装脚本一致  
- 朋友自用 vault：推荐 `.claude/skills/` 项目级安装 + 改 `vault-config.md`
