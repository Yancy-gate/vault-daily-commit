# vault-daily-commit

跨平台 Agent Skill：在 Obsidian vault 里**安全提交每日笔记**（笔记 + 附件截图），避免 Obsidian Git stash/pull 导致「回滚」和 webp 丢失。

**通用版**：`SKILL.md` + 可编辑 `vault-config.md`（路径、提交信息、排除项）

## 目录结构

```
skills/vault-daily-commit/
├── SKILL.md           # Agent 执行规范（通用）
├── vault-config.md    # ★ 每个 vault 改这个
├── prompts.md         # 用户提示词
├── README.md          # 本文件
├── install.sh         # macOS/Linux 一键安装
├── install.ps1        # Windows 一键安装
└── platforms/         # 各 Agent 安装说明
    ├── cursor.md
    ├── claude-code.md
    ├── opencode.md
    └── codex.md
```

GitHub：https://github.com/Yancy-gate/vault-daily-commit

**Release 下载**（给朋友）：https://github.com/Yancy-gate/vault-daily-commit/releases/tag/v1.0.0

| 包 | 适用 |
|----|------|
| `vault-daily-commit-universal-*.zip` | 全平台 + 安装脚本 |
| `vault-daily-commit-cursor-*.zip` | Cursor |
| `vault-daily-commit-claude-code-*.zip` | Claude Code |
| `vault-daily-commit-opencode-*.zip` | OpenCode |
| `vault-daily-commit-codex-*.zip` | Codex CLI |

## 快速安装（给朋友）

### 1. 拿到文件夹

从仓库复制整个 `vault-daily-commit/`，或：

```bash
git clone https://github.com/Yancy-gate/vault-daily-commit.git
# 只需 skills/vault-daily-commit 目录
```

### 2. 改配置

编辑 `vault-config.md`：笔记目录、截图目录、commit 信息模板。

### 3. 装到对应 Agent

| Agent | 安装位置 | 文档 |
|-------|----------|------|
| **Cursor** | `<vault>/.cursor/skills/vault-daily-commit/` 或 `~/.cursor/skills/` | [platforms/cursor.md](platforms/cursor.md) |
| **Claude Code** | `<vault>/.claude/skills/` 或 `~/.claude/skills/` | [platforms/claude-code.md](platforms/claude-code.md) |
| **OpenCode** | `~/.opencode/skills/vault-daily-commit/` | [platforms/opencode.md](platforms/opencode.md) |
| **Codex CLI** | `~/.codex/skills/vault-daily-commit/` | [platforms/codex.md](platforms/codex.md) |

### 一键脚本

```bash
# macOS/Linux — 安装到用户全局，可多次运行
bash install.sh cursor      # 或 claude-code | opencode | codex | all
```

```powershell
# Windows
.\install.ps1 -Target cursor    # 或 claude-code | opencode | codex | all
.\install.ps1 -Target all -VaultRoot "D:\path\to\vault"   # 同时装到 vault 内 .cursor/skills
```

## 使用

1. 笔记写完，截图在配置的附件目录，Obsidian 预览正常  
2. 粘贴 [prompts.md](prompts.md) 里的提示词  
3. 确认 Agent 展示的 `status` / 拟提交文件  
4. commit 完成；需要时再让它 push  

## 本 vault 默认约定

- 截图：`杂项/`
- 链接：`![[杂项/….webp]]`
- `.gitignore`：`!杂项/*.webp`

## License

MIT
