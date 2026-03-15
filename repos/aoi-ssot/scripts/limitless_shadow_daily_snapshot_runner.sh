#!/usr/bin/env bash
set -euo pipefail

# Daily Limitless shadow evidence snapshot (public-safe proof bundle)
# Writes a new bundle under aoi-ssot/context/proof_samples/

ROOT="/Users/silkroadcat/.openclaw/workspace/repos/aoi-ssot"
LOGDIR="/tmp/openclaw"
mkdir -p "$LOGDIR"

cd "$ROOT"
python3 scripts/limitless_shadow_daily_snapshot.py --hours 24 --tail 400 \
  >>"$LOGDIR/limitless-shadow-daily.out.log" \
  2>>"$LOGDIR/limitless-shadow-daily.err.log"
