# RFQ Routing Decision (Demo)

## TL;DR
- Best route: **merchant_blue_rfq**
- Reason: lowest effective price (price + fee) under trust policy (guardian_pass=True, sdna_verified=True).

## Inputs
- pair: USDC/ETH
- side: BUY
- amount_in: 1000.0

## Quotes compared
- merchant_silver_otc: REJECT (TIMEOUT)
- merchant_blue_rfq: price=3096.5, fee_bps=12, effective_price=3100.215800, latency_ms=180, guardian_pass=True, sdna_verified=True
- merchant_red_guarded: REJECT (RISK_POLICY_BLOCK)


## Trust policy
- trust_mode: `prefer_verified`
- guardian_pass=false merchants are not recommended by default.
- sdna_verified=true is preferred when choosing between eligible quotes.

## Freshness policy
- deadline_ms: `2500`
- latency_ms > deadline_ms => REJECT(TIMEOUT)
- valid_until_sec <= 0 => REJECT(QUOTE_EXPIRED)

## Guardrails
- Report-only: no signing, no trade execution.
- Evidence-first: proof_manifest + sha256sum + run_log.
