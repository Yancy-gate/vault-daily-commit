# vault-daily-commit · OpenCode 版安装与使用

> 版本 1.1.1 · 适用于 [OpenCode](https://opencode.ai)

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

编辑安装目录里的 `vault-config.md`。

## 每天用

```bash
cd /path/to/obsidian-vault
opencode
```

对话粘贴 `prompts.md` 推荐版，或：

```text
使用 vault-daily-commit，按 vault-config 提交今日笔记和附件截图。
```

## OpenCode 说明

- Skill 路径：`~/.opencode/skills/<skill-name>/SKILL.md`
- 确保在 **vault git 根** 打开 OpenCode

## 链接

- Release：https://github.com/Yancy-gate/vault-daily-commit/releases
