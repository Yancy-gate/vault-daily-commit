# Cursor

## 安装位置（二选一）

| 范围 | 路径 |
|------|------|
| 仅本 vault | `<vault>/.cursor/skills/vault-daily-commit/` |
| 所有项目 | `~/.cursor/skills/vault-daily-commit/` |

Windows 全局：`%USERPROFILE%\.cursor\skills\vault-daily-commit\`

## 安装

```powershell
Copy-Item -Recurse skills\vault-daily-commit .cursor\skills\
```

或运行 `install.ps1 -Target cursor -VaultRoot <vault路径>`。

## 验证

1. 用 Cursor 打开 vault 根目录  
2. 对话输入：`帮我 commit 今天的考研数学笔记`  
3. Agent 应先 `git status`，且只 stage `vault-config.md` 里的路径  

## 说明

Cursor 自动发现 `.cursor/skills/*/SKILL.md`，无需额外配置。
