# vault-daily-commit · Codex CLI 版安装与使用

> 版本 1.1.0 · 适用于 OpenAI [Codex CLI](https://github.com/openai/codex)

## 安装

```bash
mkdir -p ~/.codex/skills
cp -r vault-daily-commit ~/.codex/skills/
```

```powershell
$dest = "$env:USERPROFILE\.codex\skills\vault-daily-commit"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Recurse vault-daily-commit $dest -Force
```

编辑安装目录下的 `vault-config.md`。

## 每天用

```bash
cd /path/to/obsidian-vault
codex
```

粘贴 `prompts.md` 中的提交提示词。

## Codex 说明

- Skill 路径：`~/.codex/skills/<skill-name>/SKILL.md`
- 与 claude-obsidian 共存时可 symlink：`ln -s "$(pwd)/skills" ~/.codex/skills/claude-obsidian`
- 在 vault 根运行，Agent 才能正确 `git status`

## 链接

- Release：https://github.com/Yancy-gate/vault-daily-commit/releases/tag/v1.1.0
