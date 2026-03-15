#!/usr/bin/env bash
set -euo pipefail

# Limitless hourly shadow runner (report-only)
# - snapshots odds/EV at (roughly) top-of-hour
# - settles the most recent hour whose deadline passed
#
# Writes JSONL to:
# - /tmp/limitless_odds_btc_hourly.jsonl
# - /tmp/limitless_ev_btc_hourly.jsonl
# - /tmp/limitless_settle_btc_hourly.jsonl

WS="/Users/silkroadcat/.openclaw/workspace"
LOGDIR="/tmp/openclaw"
mkdir -p "$LOGDIR"

STAMP="$(date +%Y%m%d_%H%M%S)"

# Step 1: capture odds + EV snapshot (best-effort)
if bash "$WS/scripts/limitless/run_btc_shadow_snapshot.sh" >>"$LOGDIR/limitless-shadow-hourly.out.log" 2>>"$LOGDIR/limitless-shadow-hourly.err.log"; then
  echo "[$STAMP] snapshot: ok" >>"$LOGDIR/limitless-shadow-hourly.out.log"
else
  echo "[$STAMP] snapshot: fail" >>"$LOGDIR/limitless-shadow-hourly.err.log"
fi

# Step 2: settle (best-effort)
if python3 "$WS/scripts/limitless/settle_btc_hourly_shadow.py" >>"$LOGDIR/limitless-shadow-hourly.out.log" 2>>"$LOGDIR/limitless-shadow-hourly.err.log"; then
  echo "[$STAMP] settle: ok" >>"$LOGDIR/limitless-shadow-hourly.out.log"
else
  echo "[$STAMP] settle: fail" >>"$LOGDIR/limitless-shadow-hourly.err.log"
fi
