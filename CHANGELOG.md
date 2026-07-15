# Changelog

## [1.1.1] - 2026-07-15

### Changed — 脱敏 / 通用化

- 去掉示例中的个人 vault 目录名与科目专用提示词；改为 `notes/`、`attachments/` 等占位
- `prompts.md` / 各平台 INSTALL 改为「按 vault-config 提交」通用说法
- `cursor-daily-log`：示例日志目录改为 `logs/Cursor`；项目名清洗不再硬编码本机用户名
- 配置示例中的 API / 本地路径改为中性占位（不含真实 key）

架构与两工具分包方式不变。

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

### 默认约定（已在 1.1.1 改为占位示例）

- 路径与提交信息均在 `vault-config.md` 配置
- 提交前 scoped `git status` / `git diff`，禁止 `git add -A`
