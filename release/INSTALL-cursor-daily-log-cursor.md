# cursor-daily-log · Cursor 版安装与使用

> 版本 1.1.0 · 适用于 Cursor Agent  
> 仓库：https://github.com/Yancy-gate/vault-daily-commit

## 做什么

抓取本机 Cursor **当天**会话 → Obsidian `其他/Cursor日志/YYYY-MM-DD.md`：

- **今日主线**（2～5 条）
- **各会话一句摘要**（不堆原话）

## 安装

### 1. Skill

解压后把 `cursor-daily-log` 放到：

`<vault>/.cursor/skills/cursor-daily-log/`

或全局：`%USERPROFILE%\.cursor\skills\cursor-daily-log\`

### 2. 运行时 + 定时

```powershell
.\install.ps1 -InstallRuntime
notepad "$env:USERPROFILE\.cursor\scripts\cursor-daily-log\config.json"
.\install.ps1 -RegisterSchedule
```

必改：`vault_path`、`python_path`；（可选）DeepSeek `.env` 路径。

## 每天用

```text
请按 cursor-daily-log：生成本日 Cursor 日志，读一下今日主线。
```

更多见 `prompts.md`。

## 排错

| 现象 | 处理 |
|------|------|
| 任务 exit 9009 | 设置 `python_path` 为 python.exe 绝对路径 |
| 没有摘要 | 检查 DeepSeek key / Ollama，或用 `provider: heuristic` |
| Skill 未触发 | 确认目录名与 `SKILL.md` 存在 |
