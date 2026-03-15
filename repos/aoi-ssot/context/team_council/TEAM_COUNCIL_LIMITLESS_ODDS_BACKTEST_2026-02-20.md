# Team Council (Lite) — decision

## Topic
Limitless hourly strategy: use real odds(p) vs even-odds; add p-floor for slippage; choose evaluation window (24h vs 7d/14d)

## Context (optional)
We built V6 Limitless-style hourly YES/NO sims. Even-odds model showed high winrate; then we added real Limitless odds snapshots (/tmp/limitless_odds_btc_hourly.jsonl) + settlements (/tmp/limitless_settle_btc_hourly.jsonl). In a 24h window, odds-based ROI looked very high but sample size small and selection bias likely. Need team decision on evaluation method and risk guardrails.

Artifacts (SSOT repo):
- aoi-ssot script (even-odds): `scripts/v6_limitless_hourly_24h_sim.py`
- aoi-ssot script (odds-based): `scripts/v6_limitless_hourly_odds_backtest.py`
- Odds/settle logs (local): `/tmp/limitless_odds_btc_hourly.jsonl`, `/tmp/limitless_settle_btc_hourly.jsonl`

## Constraints (optional)
- L3 actions forbidden: no real wallet trades.
- Public comms must be TEASER-safe; no profit guarantees.
- Prefer deterministic, reproducible evidence and SSOT logging.

---

## TL;DR (2 lines)
- Use **real odds(p)** as the only evaluation baseline; even-odds is only a sanity-check.
- Decide go/no-go based on **7–14 days** of hourly results with strict guardrails (p-floor + spread/slippage penalty + 1 bet/hour).

## Role opinions (2–3 lines each)
- 🧿 Oracle (decision frame):
  - Decision: lock a *measurement standard* before we optimize. Assumptions: (1) odds snapshots are reliable at top-of-hour, (2) settlement outcome mapping is correct, (3) low-p markets imply high payout but low liquidity.
  - Recommendation: **Conditional Go** — proceed in shadow mode only, using odds-based PnL across 7–14d; treat 24h spikes as noise.

- 🧠 Analyzer (scoring/trade-offs):
  - Options: (A) even-odds backtest (fast but misleading), (B) odds-based (correct), (C) odds-based + liquidity/slippage model (more realistic).
  - Score: B is mandatory; C is preferred. Use 7d as minimum sample; 14d to reduce regime bias. Track ROI, winrate, bet count, MDD, and “p-tail exposure”.

- ⚔️ Security (security/risk):
  - Risks: overfitting to short window; selection bias (“best entry”); hidden costs (spread/slippage); mis-specified settlement time; relying on an API key.
  - Guardrails: **1 bet/hour max**, no martingale, enforce **p-floor** (e.g., p>=0.05) and optionally cap spend per hour; keep keys in vault; report-only.

- ⚡ Builder (feasibility/MVP):
  - Feasible now: we already have odds+settle JSONL logs; just extend the backtest window and add parameters (hours, p-floor, fee/slippage penalty, max_bet).
  - MVP timeline: 0.5 day to implement + 1 day to run 7–14d backtests + 0.5 day to package metrics report + charts.

- 📢 Comms (messaging/market):
  - 1-liner: “We measure prediction bets with receipts: odds snapshots + deterministic settlement + reproducible ROI.”
  - Objection: “Your winrate/ROI looks too good to be true.” Response: “We use real market odds and publish the full backtest manifest; short windows are treated as noise; no profit claims.”

## Consensus / Conflict
- Consensus: odds-based evaluation is required; 24h is not enough; guardrails must model slippage/liquidity.
- Conflict: how aggressive to be with low-p markets (high payout) vs skip for liquidity risk.

## Dissent (at least 1)
- Dissent: “We should ignore odds-based PnL entirely until we can model liquidity/slippage from orderbook depth; otherwise it’s still misleading.”

## Assumptions (3)
1. `/tmp/limitless_odds_btc_hourly.jsonl` snapshots are close enough to the actual tradeable prices at decision time.
2. `/tmp/limitless_settle_btc_hourly.jsonl` outcome mapping matches Limitless settlement rules.
3. Position sizing from V6 (`position_size`) is a reasonable proxy for stake sizing under a $7 wallet.

## Recommendation
- **Conditional Go**
- Confidence: **Medium**
- Risk: **Medium**

## Next actions (Top 3)
1. Extend odds backtest to **7d/14d** runs and export metrics: ROI, winrate, bet count, average p, p-tail exposure, MDD.
2. Add realism knobs: `--p-floor`, `--slippage-bps`, `--max-bet-usd` (hard cap), and re-run the report.
3. Save results as a proof bundle (JSON+CSV+manifest) and mirror a Decision Log entry (L1/L2).
