# 用户提示词模板

复制到 **Cursor / Claude Code / OpenCode / Codex** 对话即可触发 `vault-daily-commit`。

## 推荐版

把 `YYYY-MM-DD` 换成当天日期。

```text
今天数学笔记写完了，请帮我 commit。

范围只包含：
- 考研/数学/ 下今天改过的笔记
- 杂项/ 里新增或改过的 webp 截图
- 如有必要，可顺带 .gitignore 里与附件相关的改动

不要提交：插件配置、workspace、无关删除、大 PDF、其它目录。
提交信息用：数学笔记 YYYY-MM-DD
先 git status / diff 给我看一眼再 commit，不要 push。
```

## 短版

```text
帮我 commit 今天的考研数学笔记和杂项里的新截图，别带无关文件，先 status 再提交，不要 push。
```

## 推远程

在任意版本末尾加：

```text
提交成功后请再 push。
```

## 其它科目

```text
英语笔记也一起提交（考研/英语/）。
```

## 显式调用 skill（Claude Code / 部分 CLI）

```text
使用 vault-daily-commit skill，按 vault-config.md 提交今日笔记。
```
