#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTDIR="$ROOT/artifacts/v6_invest_routine"
HF="$ROOT/context/handoff/HF_v6_invest_live_restart_202603.md"
PLAYBOOK="$ROOT/context/topics/v6-invest_PLAYBOOK_V0_1.md"
EVMAX_DIR="$ROOT/artifacts/limitless_stage0_evmax"
STAKE_DIR="$ROOT/artifacts/limitless_live_trades"
DRY_DIR="$ROOT/artifacts/limitless_autotrade_dryrun"
TIMESTAMP="$(date '+%Y%m%d_%H%M%S')"
mkdir -p "$OUTDIR"

{
  echo "# v6-invest routine heartbeat: $TIMESTAMP"
  echo "- Playbook: $PLAYBOOK"
  echo "- Handoff: $HF"

  if [[ -f "$HF" ]]; then
    STATUS_LINE="$(grep -m1 "\*\*Status:\*\*" -- "$HF" | sed 's/.*\*\*Status:\*\*:[[:space:]]*//')"
    echo "- HF status: ${STATUS_LINE:-unknown}"
  else
    echo "- HF status: MISSING ($HF)"
  fi

  echo ""
  echo "## v6 artifact presence"
  for dir in "$EVMAX_DIR" "$STAKE_DIR" "$DRY_DIR"; do
    if [[ -d "$dir" ]]; then
      count=$(find "$dir" -maxdepth 1 -type f | wc -l | tr -d ' ')
      latest=$(find "$dir" -maxdepth 1 -type f | sort | tail -n 1)
      echo "- $(basename "$dir"): ${count} files, latest=${latest:-<none>}"
    else
      echo "- $(basename "$dir"): MISSING"
    fi
  done

  echo ""
  echo "## Playbook check (must not forget)"
  if [[ -f "$PLAYBOOK" ]]; then
    recurring_count=$(awk 'BEGIN{c=0} /^[0-9]+\)/{c++} /^- /{c++} END{print c}' "$PLAYBOOK")
    echo "- Recurring rules count: ${recurring_count}"
  else
    echo "- Playbook missing: $PLAYBOOK"
  fi

  echo ""
  echo "## launchd heartbeat generated at: $(date -Iseconds)"
} > "$OUTDIR/routine_${TIMESTAMP}.md"

# keep latest 30 files only
ls -1t "$OUTDIR"/routine_*.md 2>/dev/null | tail -n +31 | xargs -r rm -f

echo "v6-invest routine heartbeat written: $OUTDIR/routine_${TIMESTAMP}.md"