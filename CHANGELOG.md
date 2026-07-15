# Changelog

## [1.1.0] - 2026-07-15

### Added — cursor-daily-log

同仓库新增第二个工具：**Cursor 会话日志** Agent Skill + Windows 运行时。

- 仅抓取当天 Agent 用户发言
- **今日主线**（2～5 条）+ **各会话一句摘要**（非原话）
- 摘要：DeepSeek → Ollama → 启发式
- 计划任务默认 21:00；`python_path` 修复 Task Scheduler exit 9009
- Release 分包：`cursor-daily-log-{universal,cursor,claude-code,opencode,codex}-v1.1.0.zip`

### Changed — vault-daily-commit

- 仓库升级为「每日笔记 commit + Cursor 日志」双工具合集
- `vault-daily-commit-*` 平台包同步打到 v1.1.0（skill 行为与 1.0.0 兼容）

## [1.0.0] - 2026-07-13

### Added

- 通用 Agent Skill：`SKILL.md` + 可配置 `vault-config.md`
- 支持 Cursor、Claude Code、OpenCode、Codex CLI
- `prompts.md` 用户提示词模板
- `install.sh` / `install.ps1` 一键安装
- `platforms/` 各 Agent 安装说明
- GitHub Release 分包：`universal` + 各平台 zip

### 默认 vault 约定

- 笔记：`考研/数学/`、`考研/英语/`
- 截图：`杂项/*.webp`
- 提交前 scoped `git status` / `git diff`，禁止 `git add -A`
