#!/bin/zsh
set -euo pipefail

WS="$HOME/.openclaw/workspace"
OUTDIR="$WS/artifacts/state_saves"
mkdir -p "$OUTDIR"

TS="$(date +"%Y%m%d_%H%M%S")"
BASENAME="state_snapshot__${TS}"
TMPDIR="$(mktemp -d)"

# What we snapshot (curated, recoverable, not huge binaries)
# NOTE: include per-agent durable notes under agents/*/context only (not full agents workspaces).
PATHS=(
  "$WS/MEMORY.md"
  "$WS/USER.md"
  "$WS/IDENTITY.md"
  "$WS/context"
  "$WS/memory"
  "$WS/scripts"
)

# Agent-local SSOT (agents/*/context)
AGENT_CONTEXT_DIRS=()
if [[ -d "$WS/agents" ]]; then
  while IFS= read -r d; do
    AGENT_CONTEXT_DIRS+=("$d")
  done < <(find "$WS/agents" -maxdepth 2 -type d -name context 2>/dev/null | sort)
fi

# Build a file list (files only)
LIST="$TMPDIR/filelist.txt"
: > "$LIST"
for p in "${PATHS[@]}"; do
  if [[ -f "$p" ]]; then
    echo "${p#$WS/}" >> "$LIST"
  elif [[ -d "$p" ]]; then
    (cd "$WS" && find "${p#$WS/}" -type f -print) >> "$LIST"
  fi
done

# Add agent contexts
for d in "${AGENT_CONTEXT_DIRS[@]}"; do
  (cd "$WS" && find "${d#$WS/}" -type f -print) >> "$LIST"
done

# Create tar.gz
TAR="$OUTDIR/${BASENAME}.tar.gz"
(cd "$WS" && tar -czf "$TAR" -T "$LIST")

# Manifest + sha256
MAN="$OUTDIR/${BASENAME}__manifest.txt"
SHA="$OUTDIR/${BASENAME}__sha256.txt"
{
  echo "# $BASENAME"
  echo "created_at=$(date -Iseconds)"
  echo "workspace=$WS"
  echo ""
  echo "## included_files"
  cat "$LIST"
} > "$MAN"

shasum -a 256 "$TAR" > "$SHA"

# Retention: keep last 30 snapshots
ls -1t "$OUTDIR"/state_snapshot__*.tar.gz 2>/dev/null | tail -n +31 | while read -r old; do
  base="${old%.tar.gz}"
  rm -f "$old" "${base}__manifest.txt" "${base}__sha256.txt" || true
  # also remove any stray variants
  rm -f "${base}__manifest.txt" "${base}__sha256.txt" || true

done

rm -rf "$TMPDIR"

echo "state_snapshot: wrote $TAR"
