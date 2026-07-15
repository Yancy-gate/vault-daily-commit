# OpenCode

## 安装位置

| 范围 | 路径 |
|------|------|
| 用户全局（推荐） | `~/.opencode/skills/vault-daily-commit/` |

Windows：`%USERPROFILE%\.opencode\skills\vault-daily-commit\`

## 安装

```bash
mkdir -p ~/.opencode/skills
cp -r skills/vault-daily-commit ~/.opencode/skills/
```

```powershell
$dest = Join-Path $env:USERPROFILE '.opencode\skills\vault-daily-commit'
New-Item -ItemType Directory -Force -Path (Split-Path $dest) | Out-Null
Copy-Item -Recurse skills\vault-daily-commit $dest -Force
```

或 `bash install.sh opencode` / `install.ps1 -Target opencode`。

## 使用

1. `cd` 到你的 Obsidian vault（git 根）  
2. 启动 OpenCode  
3. 粘贴 [prompts.md](../prompts.md) 推荐版  

## 与 claude-obsidian 共存

若整个 `skills/` 已通过 symlink 挂到 OpenCode：

```bash
ln -s "$(pwd)/skills" ~/.opencode/skills/claude-obsidian
```

则 `vault-daily-commit` 已在 `skills/vault-daily-commit/`，无需单独复制。

## 验证

确认 `~/.opencode/skills/vault-daily-commit/SKILL.md` 存在；在 vault 根对话触发 commit 流程。
