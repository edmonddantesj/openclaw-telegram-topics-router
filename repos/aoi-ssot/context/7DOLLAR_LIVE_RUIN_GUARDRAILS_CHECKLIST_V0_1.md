# $7 LIVE — Ruin Guardrails Checklist (v0.1)

## Principle
**Ruin prevention > performance.** A single automation mistake should not wipe the bankroll.

## Gate 0 — Always-on (default OFF)
- `OPS_ENABLED=0` by default
- `LIMITLESS_LIVE_ENABLED=0` by default
- Any missing env / RPC mismatch → **HALT**

## Gate 1 — Funding / Caps
- Hard cap per bet: **$1 max**
- Hard cap per day: **$3 max**
- Minimum remaining bankroll floor: **$4** (stop if below)

## Gate 2 — Circuit Breakers
- **Consecutive losses ≥ 3** → stop for 24h
- **Net loss ≥ $2 (or ≥ 30% of bankroll)** → stop and require manual review
- Any execution error (RPC, tx failure, unexpected response) → stop

## Gate 3 — Canary mode (recommended start)
- Duration: 1 day
- Frequency: max 3 runs/day
- After each run: store proof bundle + update summary

## Gate 4 — Logging / Proof
- Every run writes:
  - input.json (masked)
  - decision + rationale
  - execution result
  - sha256 manifest

## Gate 5 — Preflight checks (must pass)
- ChainId = 8453 (Base)
- Wallet ETH gas >= MIN_ETH
- USDC allowance >= required (manual approve only)
- Supabase key can update settlement fields (or settlement disabled)

## Go/No-Go
- Go only if Gates 0–5 all pass and Canary has 0 execution errors.
