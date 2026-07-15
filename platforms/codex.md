# Codex CLI

## 安装位置

| 范围 | 路径 |
|------|------|
| 用户全局 | `~/.codex/skills/vault-daily-commit/` |

Windows：`%USERPROFILE%\.codex\skills\vault-daily-commit\`

## 安装

```bash
mkdir -p ~/.codex/skills
cp -r skills/vault-daily-commit ~/.codex/skills/
```

或 `bash install.sh codex` / `install.ps1 -Target codex`。

## 使用

```bash
cd /path/to/obsidian-vault
codex
```

对话中使用 [prompts.md](../prompts.md) 中的提示词。

## 与 claude-obsidian 共存

```bash
ln -s "$(pwd)/skills" ~/.codex/skills/claude-obsidian
```

## 验证

```bash
codex --list-skills 2>/dev/null | grep vault-daily-commit || ls ~/.codex/skills/vault-daily-commit/SKILL.md
```

（具体 list 命令以本机 Codex 版本为准。）
