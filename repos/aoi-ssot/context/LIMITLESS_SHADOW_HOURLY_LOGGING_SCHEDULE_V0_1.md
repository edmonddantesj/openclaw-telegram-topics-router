# Limitless Shadow — Hourly Logging Schedule (v0.1)

Date: 2026-02-20 (KST)
Owner: Edmond + Aoineco
Status: READY

## Purpose
Accumulate enough real odds + settlement evidence to evaluate V6 on Limitless-style hourly YES/NO markets over 7–14 days.

## What is logged
- Odds snapshots (prices p) and EV notes:
  - `/tmp/limitless_odds_btc_hourly.jsonl`
  - `/tmp/limitless_ev_btc_hourly.jsonl`
- Settlements (YES/NO outcome):
  - `/tmp/limitless_settle_btc_hourly.jsonl`

## Schedule (macOS LaunchAgent)
- LaunchAgent label: `ai.aoi.ssot.limitless_shadow_hourly`
- Plist path: `~/Library/LaunchAgents/ai.aoi.ssot.limitless_shadow_hourly.plist`
- Runs: **every hour at minute 01** (system local time)
- Script:
  - `aoi-ssot/scripts/limitless_shadow_hourly_runner.sh`

## Safety / guardrails
- Report-only. No wallet actions.
- Keys stay in vault; no secrets written to repo.
- Public comms: no profit claims.

## Daily evidence snapshot (recommended)
- LaunchAgent: `ai.aoi.ssot.limitless_shadow_daily_snapshot`
- Runs daily at **09:30** local time
- Script: `scripts/limitless_shadow_daily_snapshot_runner.sh`
- Output: creates a new proof bundle under `context/proof_samples/limitless_shadow_daily_<timestamp>/`

## Smoke test
- Manual run:
  - `bash scripts/limitless_shadow_hourly_runner.sh`
  - `bash scripts/limitless_shadow_daily_snapshot_runner.sh`
- Expected:
  - lines appended to odds/ev JSONL
  - settlement best-effort append (may skip if nothing expired)
  - daily proof bundle folder created
