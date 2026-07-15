# cursor-daily-log

扫描本机 Cursor Agent 当天会话，写入 Obsidian：

1. **今日主线**（2～5 条）
2. **各会话摘要**（一句，不堆原话）

本目录是 **Agent Skill**；可执行脚本在 `scripts/`。

同属仓库：[vault-daily-commit](https://github.com/Yancy-gate/vault-daily-commit)（每日笔记安全 commit）。

## 安装 Skill（各 AI 工具）

| Agent | 路径 | 说明 |
|-------|------|------|
| Cursor | `<vault>/.cursor/skills/cursor-daily-log/` | [platforms/cursor.md](platforms/cursor.md) |
| Claude Code | `~/.claude/skills/cursor-daily-log/` | [platforms/claude-code.md](platforms/claude-code.md) |
| OpenCode | `~/.opencode/skills/cursor-daily-log/` | [platforms/opencode.md](platforms/opencode.md) |
| Codex | `~/.codex/skills/cursor-daily-log/` | [platforms/codex.md](platforms/codex.md) |

一键：

```powershell
.\install.ps1 -Target cursor -VaultRoot "D:\path\to\vault"
.\install.ps1 -Target all -VaultRoot "D:\path\to\vault"
```

## 安装运行时（Windows 计划任务必需）

```powershell
.\install.ps1 -InstallRuntime
# 编辑 %USERPROFILE%\.cursor\scripts\cursor-daily-log\config.json
.\install.ps1 -RegisterSchedule
```

## Release 分包

见 GitHub Releases：`cursor-daily-log-{universal,cursor,claude-code,opencode,codex}-v*.zip`

## License

MIT（与仓库相同）
