#!/bin/zsh
set -euo pipefail
WORKSPACE="/Users/silkroadcat/.openclaw/workspace"
OUTDIR="$WORKSPACE/ops/reports/proof_regen"
mkdir -p "$OUTDIR"
DAY=$(date +%F)
OUT="$OUTDIR/REPORT_${DAY}.md"
{
  echo "# Weekly Proof Regen — $DAY"
  echo
  echo "## Latest digest artifacts"
  ls -1t "$WORKSPACE/artifacts/digest" 2>/dev/null | head -n 10 || true
  echo
  echo "## Latest maintenance artifacts"
  find "$WORKSPACE/artifacts" -maxdepth 2 -type f | tail -n 20 || true
  echo
  echo "## HF digest pointer"
  test -f "$WORKSPACE/context/ops/digests/HF_ACTIVE_DIGEST_LATEST.md" && echo "HF digest exists" || echo "HF digest missing"
} > "$OUT" 2>&1
