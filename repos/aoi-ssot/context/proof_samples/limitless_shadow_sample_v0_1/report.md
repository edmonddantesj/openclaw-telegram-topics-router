# Proof Bundle Sample — Limitless BTC Hourly Shadow (v0.1)

## Scope
Shadow-only reference run: odds snapshot + EV calc + (when available) settle + Supabase sync + digest.

## Safety
- No live bets / no fund movements.
- No secrets printed.

## Evidence
Included artifacts show the latest JSONL tail excerpts and a Supabase-based digest output.

## How to reproduce (local)
```bash
cd ~/.openclaw/workspace
bash -lc "/Users/silkroadcat/.openclaw/workspace/scripts/limitless/run_btc_shadow_snapshot.sh"
set -a; source the-alpha-oracle/vault/supabase.env; set +a
python3 scripts/limitless/upload_limitless_shadow_to_supabase.py
python3 scripts/limitless/limitless_daily_digest_supabase.py
```
