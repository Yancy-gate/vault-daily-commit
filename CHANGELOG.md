# Changelog

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
