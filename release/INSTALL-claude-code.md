# vault-daily-commit · Claude Code 版安装与使用

> 版本 1.1.0 · 适用于 [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

## 这个 Skill 做什么

在 Obsidian vault 里**安全提交每日笔记**：只 stage 笔记 + 附件截图，避免 Git 同步把未提交改动冲掉。

## 安装

### 步骤 1：解压到 skills 目录

| 范围 | 路径 |
|------|------|
| **仅本 vault**（推荐） | `<vault>/.claude/skills/vault-daily-commit/` |
| 所有项目 | `~/.claude/skills/vault-daily-commit/` |

```bash
mkdir -p .claude/skills
cp -r vault-daily-commit .claude/skills/
```

```powershell
New-Item -ItemType Directory -Force -Path .claude\skills | Out-Null
Copy-Item -Recurse vault-daily-commit .claude\skills\
```

### 步骤 2：改 `vault-config.md`

按你的 vault 改笔记路径、截图目录、commit 信息。

### 步骤 3：在 vault 根启动 Claude Code

```bash
cd /path/to/your-obsidian-vault
claude
```

## 每天用

在 Claude Code 对话中粘贴（见 `prompts.md`）：

```text
今天数学笔记写完了，请帮我 commit。
范围只包含 vault-config.md 里的笔记和杂项 webp。
先 git status / diff，不要 push。
```

或显式调用：

```text
使用 vault-daily-commit skill 提交今日笔记。
```

## Claude Code 特有说明

- **工作目录**：必须在 git 仓库根（Obsidian vault 根）
- **Skill 发现**：`.claude/skills/*/SKILL.md` 会被自动加载
- **工具权限**：首次 commit 时 Claude 可能请求运行 `git` 命令，请允许
- 若与 claude-obsidian 项目共用：也可把本 skill 放在仓库 `skills/vault-daily-commit/`，由 `AGENTS.md` 统一发现

## 常见问题

| 问题 | 处理 |
|------|------|
| 找不到 skill | 检查 `.claude/skills/vault-daily-commit/SKILL.md` 是否存在 |
| 提交了不该提交的文件 | 在提示词里强调「不要 git add -A」，并检查 `vault-config.md` 排除项 |
| webp 未跟踪 | `git add -f` + gitignore 例外规则 |

## 链接

- Release：https://github.com/Yancy-gate/vault-daily-commit/releases/tag/v1.1.0
