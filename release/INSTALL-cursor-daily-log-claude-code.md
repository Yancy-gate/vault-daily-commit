# cursor-daily-log · Claude Code 版安装与使用

> 版本 1.1.0 · 适用于 Claude Code  
> 仓库：https://github.com/Yancy-gate/vault-daily-commit

## 安装

Skill → `~/.claude/skills/cursor-daily-log/`（或 vault 内 `.claude/skills/`）

```powershell
.\install.ps1 -Target claude-code -InstallRuntime
# 编辑 config.json 后注册任务：
.\install.ps1 -RegisterSchedule
```

## 用法

见包内 `prompts.md` / `SKILL.md`。
