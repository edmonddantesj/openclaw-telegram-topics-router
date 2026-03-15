# Limitless BTC — Next Top-of-Hour (KST) EV Pipeline Spec v0.1

## Goal
For BTC Hourly markets, predict direction at the **next KST top-of-hour** and maximize expected value (EV) by choosing an entry time t.

## Mapping
- YES ≙ UP
- NO  ≙ DOWN

## Inputs
- V6: p(up) at time t (plus confidence / agreement)
- Limitless: odds snapshot at time t
  - Market `prices[]` (YES/NO)
  - If tradeType=clob: orderbook (best bid/ask, midpoint, lastTradePrice)
- Settlement label (direction):
  - **baseline** = BTC price at the **previous top-of-hour (KST)** (snapshot reference)
  - **target** = BTC price at the **next top-of-hour (KST)**
  - label UP if target > baseline, else DOWN (or FLAT treated as DOWN/NEUTRAL by policy)
  - Deterministic price source: Binance BTCUSDT 1m kline close at each top-of-hour (UTC-converted)

## Shadow-only phase (no bets)
1) Discover current Hourly BTC market slug
2) Snapshot odds at schedule times (**wide shadow**): **-50m, -30m, -20m, -10m, -5m, -2m, -1m**
3) At/after top-of-hour, label outcome using deterministic candle close (baseline prev top-of-hour vs target next top-of-hour)
4) Compute EV per candidate time; choose best time/action; backtest across days

## Live window expansion policy (gated)
- Stage 0 (start):
  - Shadow: -50/-30/-20/-10/-5/-2/-1
  - Live allowed times: **-10/-5/-2/-1 only**
- Stage 1: expand live to **-20** only if:
  - recent shadow shows consistent positive EV at -20 with sufficient samples
  - canary live has 0 execution errors
  - circuit breakers/stop-loss rules are proven to trigger correctly
- Stage 2: expand live to **-30/-50** only if:
  - statistically meaningful EV edge at those times
  - liquidity/slippage/odds dynamics understood (no blow-ups)

Rule: if EV <= threshold or agreement is WEAK / Kelly==0 → HOLD (fail-closed)

## Scripts (implemented / planned)
Implemented (v0.1):
- `scripts/limitless/discover_hourly_btc_market.py`
- `scripts/limitless/snapshot_odds.py`
- `scripts/settle_next_top_of_hour_kst.py` (price oracle)

Planned (v0.2):
- Supabase integration: store `target_ts_kst/utc`, odds snapshots, EV metrics
- Auto scheduler (cron) for snapshot schedule
- Entry-time policy (only bet when EV>threshold)

## Safety
- Default: shadow-only logging
- Live requires explicit L3 approval (fund movement)
