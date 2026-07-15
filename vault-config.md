# vault-daily-commit 配置

复制本 skill 到新 vault 时，**只改这个文件**即可；`SKILL.md` 保持通用。

下列为**占位示例**，请改成你自己的目录名。

## 路径

| 键 | 示例路径 | 说明 |
|----|----------|------|
| `notes_primary` | `notes/` | 主笔记目录（必改） |
| `notes_extra` | `notes-extra/` | 额外笔记目录（可选） |
| `attachments` | `attachments/` | 截图 / 附件目录 |
| `attachments_glob` | `*.webp` | 要跟踪的附件类型 |

## Git

| 键 | 示例值 |
|----|--------|
| `gitignore_attachment_rule` | `!attachments/*.webp` |
| `default_commit_message` | `daily notes {date}` |
| `extra_commit_message` | `extra notes {date}` |

`{date}` = 当天 `YYYY-MM-DD`

## 禁止纳入本次提交（除非用户明确要求）

- `.obsidian/`、`workspace.json`、各插件 `data.json`
- 无关大删除、大体积二进制、其它未列入上方路径的目录
- 不要使用 `git add -A`

## 默认行为

- **只 commit**，不 push（用户说 push / 推远程 时才 push）
- 提交前必须 `git status` + `git diff`（限定上述路径）

## Obsidian 约定（建议）

- 截图放 `attachments/`（或你在上表配置的目录）
- 链接与实际附件路径一致，例如 `![[attachments/example.webp]]`
