---
name: vault-daily-commit
description: >-
  Safely commit daily Obsidian study notes and attachment screenshots without
  staging unrelated vault changes. Reads paths from vault-config.md. Use when
  the user asks to commit daily notes, 数学笔记, 考研笔记, 杂项截图, vault
  backup, or says 帮我 commit / 每日笔记提交 / 今天笔记写完了.
---

# vault-daily-commit

Scoped git commit for daily study notes. Prevents「版本回滚 / 图片丢失」from unstaged edits + Obsidian Git pull/stash.

**Before running**: read [vault-config.md](vault-config.md) in this skill directory for paths, commit messages, and exclusions.

Human doc (this vault): `其他/Cursor每日笔记提交.md`

## Workflow

```
- [ ] 1. Read vault-config.md
- [ ] 2. Get today date (YYYY-MM-DD)
- [ ] 3. git status + git diff (scoped paths only)
- [ ] 4. Show user planned files; wait if ambiguous
- [ ] 5. Stage allowlisted paths only
- [ ] 6. git commit
- [ ] 7. git status verify
- [ ] 8. git push (only if user requested)
```

### Step 1 — Date

- **Windows**: `Get-Date -Format yyyy-MM-dd`
- **macOS/Linux**: `date +%Y-%m-%d`

### Step 2 — Inspect (scoped)

Use paths from `vault-config.md`. Example for default vault:

```bash
git status --porcelain -- "考研/" "杂项/" ".gitignore"
git diff --stat -- "考研/" "杂项/"
```

```powershell
git status --porcelain -- "考研/" "杂项/" ".gitignore"
git diff --stat -- "考研/" "杂项/"
```

Add `考研/英语/` when user asks for 英语.

### Step 3 — Stage (allowlist)

**Include** when changed:

- Notes dirs from config (`notes_math`, `notes_english`, …)
- `attachments` + `attachments_glob` (e.g. `杂项/*.webp`)
- `.gitignore` only if attachment rules changed

**Exclude**: see `vault-config.md` → 禁止纳入本次提交.

```bash
git add -- "考研/数学/"
git add -f -- "杂项/"*.webp    # if webp ignored by .gitignore
```

```powershell
git add -- "考研/数学/"
git add -f -- "杂项/*.webp"
```

Never `git add -A`.

### Step 4 — Commit message

From `vault-config.md` `default_commit_message`, substitute `{date}`.

### Step 5 — Push

Only when user says: push / 推远程 / 提交成功后请再 push.

```bash
git push origin HEAD
```

## Hard rules

| Do | Don't |
|----|-------|
| Read `vault-config.md` first | Hard-code paths when config exists |
| `git status` / `git diff` before commit | `git add -A` |
| Stage allowlisted paths only | Commit `.obsidian/` or workspace |
| Default: no push | `git reset --hard`, force push |
| `git add -f` for ignored webp | Mix unrelated bulk deletes into note commit |

## User trigger phrases

See [prompts.md](prompts.md). When user pastes them, follow this skill.

## Post-commit (tell user)

- Today's `.md` is in the commit
- New webp in attachments dir and tracked (`git ls-files`)
- Obsidian preview shows images (links match attachment path)

## Platform install

- [README.md](README.md) — all agents
- [platforms/cursor.md](platforms/cursor.md)
- [platforms/claude-code.md](platforms/claude-code.md)
- [platforms/opencode.md](platforms/opencode.md)
- [platforms/codex.md](platforms/codex.md)
