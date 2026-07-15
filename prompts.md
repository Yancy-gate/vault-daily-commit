# 用户提示词模板

复制到 **Cursor / Claude Code / OpenCode / Codex** 对话即可触发 `vault-daily-commit`。

路径以你本地的 `vault-config.md` 为准；下面用通用说法，不绑定具体科目目录。

## 推荐版

把 `YYYY-MM-DD` 换成当天日期。

```text
今天的笔记写完了，请按 vault-daily-commit 帮我 commit。

范围只包含 vault-config.md 里配置的：
- 笔记目录中今天改过的文件
- 附件目录里新增或改过的截图（按配置的 glob）
- 如有必要，可顺带 .gitignore 里与附件相关的改动

不要提交：插件配置、workspace、无关删除、大文件、其它目录。
提交信息用 vault-config 里的默认模板（把日期换成 YYYY-MM-DD）。
先 git status / diff 给我看一眼再 commit，不要 push。
```

## 短版

```text
帮我按 vault-config 提交今天的笔记和附件截图，别带无关文件，先 status 再 commit，不要 push。
```

## 推远程

在任意版本末尾加：

```text
提交成功后请再 push。
```

## 额外笔记目录

若 `vault-config.md` 里配置了 `notes_extra`：

```text
额外笔记目录也一起提交。
```

## 显式调用 skill（Claude Code / 部分 CLI）

```text
使用 vault-daily-commit skill，按 vault-config.md 提交今日笔记。
```
