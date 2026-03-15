# Proof Bundle — AOI Squad Pro One-click Demo (v0.1)

## Run ID
demo_limitless_shadow_20260219_014332

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
```bash
cd ~/.openclaw/workspace
bash scripts/aoi_squad_pro_oneclick_demo.sh
```
