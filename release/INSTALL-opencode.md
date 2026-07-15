# vault-daily-commit · OpenCode 版安装与使用

> 版本 1.1.0 · 适用于 [OpenCode](https://opencode.ai)

## 安装

### 全局安装（推荐）

```bash
mkdir -p ~/.opencode/skills
cp -r vault-daily-commit ~/.opencode/skills/
```

```powershell
$dest = "$env:USERPROFILE\.opencode\skills\vault-daily-commit"
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Recurse vault-daily-commit $dest -Force
```

### 改配置

编辑 `~/.opencode/skills/vault-daily-commit/vault-config.md`（或复制后改安装目录里的那份）。

## 每天用

```bash
cd /path/to/obsidian-vault
opencode
```

对话粘贴 `prompts.md` 推荐版，或：

```text
使用 vault-daily-commit，按 vault-config 提交今日考研笔记和杂项截图。
```

## OpenCode 说明

- Skill 路径：`~/.opencode/skills/<skill-name>/SKILL.md`
- 若已 symlink 整个 claude-obsidian `skills/` 到 `~/.opencode/skills/claude-obsidian`，本 skill 可能已在其中，无需重复安装
- 确保在 **vault git 根** 打开 OpenCode

## 链接

- Release：https://github.com/Yancy-gate/vault-daily-commit/releases/tag/v1.1.0
