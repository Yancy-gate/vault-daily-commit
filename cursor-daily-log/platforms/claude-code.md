# Claude Code

## 安装位置

| 范围 | 路径 |
|------|------|
| 全局 | `~/.claude/skills/cursor-daily-log/` |
| 本 vault | `<vault>/.claude/skills/cursor-daily-log/` |

Windows 运行时仍放在 `~/.cursor/scripts/cursor-daily-log/`（与计划任务共用）。

## 安装

```powershell
.\install.ps1 -Target claude-code -InstallRuntime
.\install.ps1 -Target claude-code -VaultRoot "D:\path\to\vault" -InstallRuntime
```

## 验证

`请按 cursor-daily-log skill 生成本日会话日志`
