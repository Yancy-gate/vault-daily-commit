# vault-daily-commit v1.0.0

Obsidian 每日笔记**安全 Git 提交** Agent Skill — 跨 Cursor / Claude Code / OpenCode / Codex。

## 下载哪个包？

| 压缩包 | 适合谁 | 安装位置 |
|--------|--------|----------|
| **universal** | 想自己选平台 / 全文件 | 解压后看 `README.md` |
| **cursor** | Cursor 用户 | `<vault>/.cursor/skills/vault-daily-commit/` |
| **claude-code** | Claude Code 用户 | `<vault>/.claude/skills/vault-daily-commit/` |
| **opencode** | OpenCode 用户 | `~/.opencode/skills/vault-daily-commit/` |
| **codex** | Codex CLI 用户 | `~/.codex/skills/vault-daily-commit/` |

每个平台包内都有 **`INSTALL.md`**（安装 + 每日用法 + 排错）。

## 3 步上手

1. **下载** 对应平台的 zip，解压  
2. **编辑** `vault-config.md`（笔记目录、截图目录、commit 信息）  
3. **对话** 粘贴 `prompts.md` 里的提示词，让 Agent commit  

## 每日提示词（最短）

```text
帮我 commit 今天的考研数学笔记和杂项里的新截图，别带无关文件，先 status 再提交，不要 push。
```

## 核心规则

- 提交前必须 `git status` / `git diff`（只看配置的目录）
- **禁止** `git add -A`
- 默认 **只 commit**，不 push（要说「请再 push」才推）
- 截图目录需在 `.gitignore` 有跟踪例外（如 `!杂项/*.webp`）

## 仓库内路径

https://github.com/Yancy-gate/vault-daily-commit

## Changelog

见包内 `CHANGELOG.md`。
