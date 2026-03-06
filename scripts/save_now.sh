#!/bin/zsh
set -euo pipefail

WS="$HOME/.openclaw/workspace"

# 1) Render + sync Ralph Loop ledger (best-effort)
if [[ -x "$WS/scripts/ralph_loop_sync.sh" ]]; then
  "$WS/scripts/ralph_loop_sync.sh" || true
fi

# 2) md-vault autosync (best-effort)
if [[ -x "$WS/scripts/md_vault_autosync.sh" ]]; then
  "$WS/scripts/md_vault_autosync.sh" || true
fi

# 3) State snapshot (hard requirement)
"$WS/scripts/state_snapshot.sh"

# 4) Snapshot remote upload (best-effort)
if [[ -x "$WS/scripts/state_snapshot_upload_github.sh" ]]; then
  "$WS/scripts/state_snapshot_upload_github.sh" || true
fi

echo "save_now: done"
