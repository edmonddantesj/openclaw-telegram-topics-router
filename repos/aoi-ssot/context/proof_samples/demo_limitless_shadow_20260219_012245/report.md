# Proof Bundle — AOI Squad Pro One-click Demo (v0.1)

## Run ID
demo_limitless_shadow_20260219_012245

## Scope
Limitless BTC Hourly Shadow reference pipeline:
- odds snapshot + EV calc
- (best-effort) settle
- Supabase sync
- Supabase-based digest

## Safety
- Shadow-only: no live bets, no fund movement.
- No secrets printed.

## How to reproduce (local)
[1/8] shadow snapshot (odds+EV, best-effort)
[2/8] settle (best-effort)
[3/8] supabase sync (idempotent, best-effort)
[4/8] digest snapshot (prefer Supabase; fallback local)
[5/8] public-safe scan report
[6/8] write report.md
