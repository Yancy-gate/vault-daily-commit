# vault-daily-commit

Obsidian 学习库的两个跨平台 Agent 工具（**同仓分发**）：

| 工具 | 作用 |
|------|------|
| **vault-daily-commit**（仓库根目录） | 安全提交每日笔记 + 附件截图（防 Obsidian Git 回滚） |
| **[cursor-daily-log/](cursor-daily-log/)** | 把当天 Cursor 会话归纳成「主线 + 一句摘要」写入笔记 |

GitHub：https://github.com/Yancy-gate/vault-daily-commit  
**Release**：https://github.com/Yancy-gate/vault-daily-commit/releases

路径与提示词均为**通用占位**；安装后请改 `vault-config.md` / `config.json`。

---

## 1) vault-daily-commit（每日笔记 commit）

```
SKILL.md / vault-config.md / prompts.md / install.* / platforms/
```

| 包 | 适合谁 |
|----|--------|
| `vault-daily-commit-universal-*.zip` | 全平台 |
| `vault-daily-commit-cursor-*.zip` | Cursor |
| `vault-daily-commit-claude-code-*.zip` | Claude Code |
| `vault-daily-commit-opencode-*.zip` | OpenCode |
| `vault-daily-commit-codex-*.zip` | Codex CLI |

```powershell
.\install.ps1 -Target cursor -VaultRoot "D:\path\to\vault"
```

最短提示词：

```text
帮我按 vault-config 提交今天的笔记和附件截图，别带无关文件，先 status 再 commit，不要 push。
```

---

## 2) cursor-daily-log（Cursor 会话日志）

详见 [cursor-daily-log/README.md](cursor-daily-log/README.md)。

| 包 | 适合谁 |
|----|--------|
| `cursor-daily-log-universal-*.zip` | 全平台 |
| `cursor-daily-log-cursor-*.zip` | Cursor |
| `cursor-daily-log-claude-code-*.zip` | Claude Code |
| `cursor-daily-log-opencode-*.zip` | OpenCode |
| `cursor-daily-log-codex-*.zip` | Codex CLI |

```powershell
cd cursor-daily-log
.\install.ps1 -Target cursor -VaultRoot "D:\path\to\vault" -InstallRuntime
# 编辑 %USERPROFILE%\.cursor\scripts\cursor-daily-log\config.json 后：
.\install.ps1 -RegisterSchedule
```

---

## License

MIT
