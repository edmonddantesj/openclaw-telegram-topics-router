# Limitless BTC Next Top-of-Hour — Roadmap (v0.1)

## Objective
Maximize expected value (EV) on BTC hourly top-of-hour markets using:
- p(YES) = P(price_at_target > strike)
- odds snapshots across multiple candidate entry times
- strict governance gates (shadow-first → canary → staged expansion)

## Stage 0 (Shadow-first)
- Snapshot schedule: -50/-30/-20/-10/-5/-2/-1
- Record:
  - market slug, strike, odds/prices, orderbook top-of-book
  - baseline & target close (Binance 1m)
  - V6 signals (agreement, kelly) + derived mu + sigma(60m)
  - computed P_yes and EV_yes/EV_no

## Stage 1 (Canary Live)
- Live window: -10/-5/-2/-1 only
- Caps: $1 per bet, $3 per day, bankroll floor $4
- Circuit breakers: 3 consecutive losses or -30% drawdown

## Stage 2 (Expansion)
- Expand to -20 → then -30/-50 only after evidence thresholds

## Deliverables
- JSONL logs for odds + EV
- daily digest: best entry time stats + EV distribution
- proof bundle: manifest + sha256
