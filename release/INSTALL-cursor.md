# vault-daily-commit · Cursor 版安装与使用

> 版本 1.1.0 · 适用于 [Cursor](https://cursor.com) Agent

## 这个 Skill 做什么

在 Obsidian vault 里**安全提交每日笔记**：只 stage 笔记目录 + 附件截图，避免 Obsidian Git 自动 pull/stash 导致内容「回滚」或 webp 丢失。

## 安装（3 分钟）

### 步骤 1：解压到正确位置

将本 zip 解压后，把整个 `vault-daily-commit` 文件夹放到：

| 范围 | 路径 |
|------|------|
| **仅本 vault**（推荐） | `<你的Obsidian库根>/.cursor/skills/vault-daily-commit/` |
| 所有 Cursor 项目 | `~/.cursor/skills/vault-daily-commit/` |

Windows 全局示例：`C:\Users\你的用户名\.cursor\skills\vault-daily-commit\`

```powershell
# 示例：装到某个 vault
$vault = "D:\Obsidian\我的库"
New-Item -ItemType Directory -Force -Path "$vault\.cursor\skills" | Out-Null
Copy-Item -Recurse vault-daily-commit "$vault\.cursor\skills\"
```

### 步骤 2：改配置

编辑 `vault-config.md`：

- `notes_math` → 你的数学笔记目录
- `attachments` → 你的截图目录（如 `杂项/`）
- `default_commit_message` → 提交信息模板

### 步骤 3：验证

1. 用 **Cursor 打开 vault 根目录**（含 `.git` 的文件夹）
2. 新建 Agent 对话，输入：`列出你能用的 skills` 或直接试提交提示词
3. 应能识别 `vault-daily-commit`

## 每天用（复制到 Cursor 对话）

**推荐版**（把日期改成今天）：

```text
今天数学笔记写完了，请帮我 commit。

范围只包含：
- 考研/数学/ 下今天改过的笔记
- 杂项/ 里新增或改过的 webp 截图

不要提交：插件配置、workspace、无关删除、大 PDF、其它目录。
提交信息用：数学笔记 YYYY-MM-DD
先 git status / diff 给我看一眼再 commit，不要 push。
```

**短版**：

```text
帮我 commit 今天的考研数学笔记和杂项里的新截图，别带无关文件，先 status 再提交，不要 push。
```

**要推 GitHub 时** 末尾加：`提交成功后请再 push。`

完整模板见包内 `prompts.md`。

## Agent 应执行什么

1. 读 `vault-config.md`
2. `git status` / `git diff`（只看你配置的路径）
3. 展示拟提交文件，等你确认
4. `git add` 允许列表内的文件（**不用** `git add -A`）
5. `git commit`
6. 仅在你要求时 `git push`

## 常见问题

| 问题 | 处理 |
|------|------|
| Skill 没触发 | 确认文件夹名是 `vault-daily-commit`，内有 `SKILL.md` |
| 截图 commit 不进去 | `.gitignore` 忽略了 `*.webp` → 需 `git add -f 杂项/xxx.webp`，并在 gitignore 加 `!杂项/*.webp` |
| Obsidian 图裂了 | 链接路径要和截图实际目录一致，如 `![[杂项/xxx.webp]]` |
| 打开了子文件夹 | Cursor 工作区必须是 **vault git 根**，不是 `考研/` 子目录 |

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | Agent 执行规范 |
| `vault-config.md` | **你要改的配置** |
| `prompts.md` | 提示词副本 |
| `README.md` | 总览 |

## 链接

- 完整仓库：https://github.com/Yancy-gate/vault-daily-commit
- Release：https://github.com/Yancy-gate/vault-daily-commit/releases/tag/v1.1.0
