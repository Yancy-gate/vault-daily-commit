# vault-daily-commit 配置

复制本 skill 到新 vault 时，**只改这个文件**即可；`SKILL.md` 保持通用。

## 路径（本 vault 默认值）

| 键 | 路径 | 说明 |
|----|------|------|
| `notes_math` | `考研/数学/` | 数学每日笔记 |
| `notes_english` | `考研/英语/` | 英语笔记（可选） |
| `attachments` | `杂项/` | 截图目录 |
| `attachments_glob` | `*.webp` | 要跟踪的附件类型 |

## Git

| 键 | 值 |
|----|-----|
| `gitignore_attachment_rule` | `!杂项/*.webp` |
| `default_commit_message` | `数学笔记 {date}` |
| `english_commit_message` | `英语笔记 {date}` |

`{date}` = 当天 `YYYY-MM-DD`

## 禁止纳入本次提交（除非用户明确要求）

- `.obsidian/`、`workspace.json`、各插件 `data.json`
- `copilot/`、无关大删除、大 PDF
- `wiki/`、`计划/`、课设大目录
- 不要使用 `git add -A`

## 默认行为

- **只 commit**，不 push（用户说 push / 推远程 时才 push）
- 提交前必须 `git status` + `git diff`（限定上述路径）

## Obsidian 约定（本 vault）

- 截图放 `杂项/`
- 链接：`![[杂项/….webp]]` 或 `![[….webp]]`
