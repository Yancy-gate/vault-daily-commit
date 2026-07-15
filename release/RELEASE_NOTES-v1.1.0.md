# vault-daily-commit 合集 v1.1.0

同仓两个工具，均提供 **universal + 各 AI 平台** 分包。

## 下载哪个包？

### A. 每日笔记安全 commit（原工具）

| 压缩包 | 适合谁 | 安装位置 |
|--------|--------|----------|
| `vault-daily-commit-universal-v1.1.0.zip` | 自己选平台 | 解压看 README |
| `vault-daily-commit-cursor-v1.1.0.zip` | Cursor | `<vault>/.cursor/skills/vault-daily-commit/` |
| `vault-daily-commit-claude-code-v1.1.0.zip` | Claude Code | `~/.claude/skills/vault-daily-commit/` |
| `vault-daily-commit-opencode-v1.1.0.zip` | OpenCode | `~/.opencode/skills/vault-daily-commit/` |
| `vault-daily-commit-codex-v1.1.0.zip` | Codex | `~/.codex/skills/vault-daily-commit/` |

每个平台包内有 **`INSTALL.md`**。

### B. Cursor 会话日志（本版新增）

| 压缩包 | 适合谁 | 安装位置 |
|--------|--------|----------|
| `cursor-daily-log-universal-v1.1.0.zip` | 自己选平台 | 解压看 README |
| `cursor-daily-log-cursor-v1.1.0.zip` | Cursor | `<vault>/.cursor/skills/cursor-daily-log/` |
| `cursor-daily-log-claude-code-v1.1.0.zip` | Claude Code | `~/.claude/skills/cursor-daily-log/` |
| `cursor-daily-log-opencode-v1.1.0.zip` | OpenCode | `~/.opencode/skills/cursor-daily-log/` |
| `cursor-daily-log-codex-v1.1.0.zip` | Codex | `~/.codex/skills/cursor-daily-log/` |

运行时 + 每晚任务另见包内 `INSTALL.md`（`~/.cursor/scripts/cursor-daily-log/`）。

## 本版亮点（cursor-daily-log）

- 今日主线 + 各会话一句摘要（不堆原话）
- DeepSeek / Ollama / 启发式回退
- 计划任务 21:00；`python_path` 修复 exit 9009

## 仓库

https://github.com/Yancy-gate/vault-daily-commit

完整变更见 `CHANGELOG.md`。
