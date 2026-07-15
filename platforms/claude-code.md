# Claude Code

## 安装位置

| 范围 | 路径 |
|------|------|
| 本 vault | `<vault>/.claude/skills/vault-daily-commit/` |
| 全局 | `~/.claude/skills/vault-daily-commit/` |

## 安装

```bash
mkdir -p .claude/skills
cp -r vault-daily-commit .claude/skills/
```

或 `install.sh claude-code` / `install.ps1 -Target claude-code`。

## 验证

粘贴：

```text
今天的笔记写完了，请帮我 commit。（见 prompts.md）
```
