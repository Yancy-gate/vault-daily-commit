# Cursor

## 安装位置

| 范围 | Skill 路径 |
|------|-----------|
| 本 vault | `<vault>/.cursor/skills/cursor-daily-log/` |
| 全局 | `~/.cursor/skills/cursor-daily-log/` |

运行时（计划任务）：`~/.cursor/scripts/cursor-daily-log/`

## 安装

```powershell
.\install.ps1 -Target cursor -VaultRoot "D:\path\to\vault" -InstallRuntime
# 编辑 config.json 后：
.\install.ps1 -RegisterSchedule
```

## 验证

对话：`请按 cursor-daily-log 生成今天的 Cursor 日志`
