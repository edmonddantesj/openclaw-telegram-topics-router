#!/bin/zsh
set -euo pipefail
WORKSPACE="/Users/silkroadcat/.openclaw/workspace"
OUTDIR="$WORKSPACE/ops/reports/security_audit"
mkdir -p "$OUTDIR"
DAY=$(date +%F)
OUT="$OUTDIR/REPORT_${DAY}.md"
{
  echo "# Monthly Security Audit — $DAY"
  echo
  echo "## OpenClaw health"
  openclaw health || true
  echo
  echo "## LaunchAgents snapshot"
  launchctl list | egrep 'ai\\.aoi|openclaw' || true
  echo
  echo "## Disk"
  df -h /
} > "$OUT" 2>&1
