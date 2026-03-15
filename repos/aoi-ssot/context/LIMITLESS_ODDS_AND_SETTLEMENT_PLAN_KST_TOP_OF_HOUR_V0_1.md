# Limitless — Odds Snapshot + KST Top-of-Hour Settlement Plan (v0.1)

## Goal
Optimize expected value (EV) for "predict direction at next top-of-hour" markets by combining:
- probability forecast p(up) at time t
- Limitless odds/orderbook at time t
- target settlement time = next **KST** top-of-hour

## Key decision
- Target time: **next top-of-hour in KST**.
- Store both:
  - `target_ts_kst` (human reference)
  - `target_ts_utc` (for price sources and some APIs)

## Limitless API evidence (from api.limitless.exchange/api-v1)
Relevant public endpoints exist to capture odds:
- `GET /markets/{addressOrSlug}` — market details; includes pricing fields for AMM markets (e.g., `prices: [..]`).
- `GET /markets/{slug}/orderbook` — current orderbook for CLOB markets; returns bids/asks + `adjustedMidpoint` + `lastTradePrice`.
- `GET /markets/{slug}/historical-price` — historical price data (interval supports 1h/6h/1d/...).

Auth note:
- API key via `X-API-Key: lmts_...` recommended; cookie auth is deprecated.

## Data we must log (minimal)
Per snapshot:
- `captured_at` (UTC)
- `captured_at_kst`
- `market_slug`
- `market_type` (amm|clob)
- For AMM: `prices[]` (YES/NO) and liquidity/openInterest if provided
- For CLOB: top-of-book: best bid/ask price + size, adjustedMidpoint, lastTradePrice

Per prediction:
- `prediction_at` (UTC)
- `prediction_at_kst`
- `target_top_of_hour_kst`
- `target_top_of_hour_utc`
- `direction` (UP/DOWN)
- `p_up` (0..1)

## Settlement (labeling) for "next top-of-hour"
- Compute target close price using a deterministic source (ex: Binance BTCUSDT 1m kline).
- Rule: choose the 1m candle whose **openTime == target_ts_utc** (converted from KST top-of-hour).
- Use that candle's **close** as settlement reference.

## EV computation (high-level)
For each candidate entry time t:
- compute p_up(t)
- derive implied payout/odds from AMM prices or CLOB orderbook
- compute EV for UP and DOWN
- choose best action among {UP, DOWN, HOLD}

## Safety gates
- Default: shadow-only (log p + odds + eventual outcome)
- Canary live: bet cap $1, day cap $3, bankroll floor $4, circuit breakers

## Next implementation steps
1) Implement `scripts/limitless_snapshot_odds.py` (public endpoints) to log odds snapshots to local JSONL.
2) Implement `scripts/settle_next_top_of_hour.py` to label predictions using Binance 1m close at target_ts.
3) Backfill last N days for analysis and select entry-time schedule (e.g., -10m, -5m, -2m, -1m).
