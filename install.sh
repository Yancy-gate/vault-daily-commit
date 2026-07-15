#!/usr/bin/env bash
# Install vault-daily-commit skill for Cursor / Claude Code / OpenCode / Codex
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="${1:-all}"
VAULT_ROOT="${2:-}"

install_one() {
  local agent="$1"
  local dest="$2"
  mkdir -p "$(dirname "$dest")"
  if [ -L "$dest" ]; then
    echo "[skip] symlink exists: $dest"
    return
  fi
  if [ -d "$dest" ]; then
    rm -rf "$dest"
  fi
  cp -r "$SCRIPT_DIR" "$dest"
  echo "[ok] $agent -> $dest"
}

case "$TARGET" in
  cursor)
    if [ -n "$VAULT_ROOT" ]; then
      install_one "cursor (vault)" "$VAULT_ROOT/.cursor/skills/vault-daily-commit"
    else
      echo "Usage: install.sh cursor <vault-root>"
      exit 1
    fi
    ;;
  claude-code)
    if [ -n "$VAULT_ROOT" ]; then
      install_one "claude-code (vault)" "$VAULT_ROOT/.claude/skills/vault-daily-commit"
    else
      install_one "claude-code (global)" "$HOME/.claude/skills/vault-daily-commit"
    fi
    ;;
  opencode)
    install_one "opencode" "$HOME/.opencode/skills/vault-daily-commit"
    ;;
  codex)
    install_one "codex" "$HOME/.codex/skills/vault-daily-commit"
    ;;
  all)
    install_one "opencode" "$HOME/.opencode/skills/vault-daily-commit"
    install_one "codex" "$HOME/.codex/skills/vault-daily-commit"
    install_one "claude-code (global)" "$HOME/.claude/skills/vault-daily-commit"
    if [ -n "$VAULT_ROOT" ]; then
      install_one "cursor (vault)" "$VAULT_ROOT/.cursor/skills/vault-daily-commit"
      install_one "claude-code (vault)" "$VAULT_ROOT/.claude/skills/vault-daily-commit"
    fi
    echo "Tip: pass vault root as 2nd arg to also install cursor/claude-code project skills"
    ;;
  *)
    echo "Usage: install.sh {cursor|claude-code|opencode|codex|all} [vault-root]"
    exit 1
    ;;
esac

echo "Done. Edit vault-config.md in the installed copy for your paths."
