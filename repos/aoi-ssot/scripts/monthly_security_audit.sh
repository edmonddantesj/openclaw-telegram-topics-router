#!/usr/bin/env bash
set -euo pipefail

# Monthly security audit (local)
# L1/L2 only: report-only. Does NOT post externally.

OUTDIR="/tmp/aoi_monthly_security_audit_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTDIR"

{
  echo "date: $(date -Iseconds)"
  echo "host: $(hostname)"
  echo "pwd: $(pwd)"
} > "$OUTDIR/meta.txt"

# OpenClaw security posture (best-effort)
(openclaw security audit || true) | tee "$OUTDIR/openclaw_security_audit.txt"

# Repo integrity checks (best-effort)
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

python3 scripts/test_audit_stall_demo.py | tee "$OUTDIR/test_audit_stall_demo.txt"
python3 scripts/test_bazaar_fx_skill_demo.py | tee "$OUTDIR/test_bazaar_fx_skill_demo.txt"

# Git status snapshot
(git status --porcelain || true) > "$OUTDIR/git_status_porcelain.txt"

echo "OK. Report folder: $OUTDIR"
