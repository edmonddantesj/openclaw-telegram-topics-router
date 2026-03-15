# ACP Longform Article — Summary (2026-02-18) v0.1

Source raw SSOT: `context/ACP_LONGFORM_ARTICLE_RAW_2026-02-18_V0_1.txt`

## 1) Core thesis
- Agent capability is rising, but **production reliability** is blocked by unstable systems, lack of auditability, unclear safety boundaries, and non-reproducible outputs.
- Aoineco publishes on **ACP** not as a “catalog”, but as a **trust + settlement + reputation** testbed for production-grade agent services.

## 2) Shared design principles
1) **PLAN-ONLY by default**
   - Explicitly avoids: fund movement/swaps, restarts/config changes, automated external posting, secret/token access.
   - Delivers: plans + checklists + risk cards + proof artifacts.
2) **Proof-first**
   - Structured JSON reports, checklists, ADR-style notes, deterministic artifacts + sha256.
3) **Secure defaults**
   - No secret leakage, explicit network boundaries, output caps, evidence without dumping sensitive logs.

## 3) ACP lineup described in the article
- `time_oracle_clock_sync` — $0.01 bait: clock snapshot + drift estimate (fallback sources).
- `gateway_healthcheck_recovery_plan` — $0.05: plan-only recovery plan for Gateway issues.
- `aoi_token_safety` — token/contract risk report (warn-first, no onchain execution).  
  - NOTE: current listing has been updated to **$1 fixed (first 5 buyers promo)**; article price text should be updated.
- `debridge_sol_base_swap_plan` — $0.05: cross-chain swap planning via deBridge/DLN (no swaps).
- `nexus_oracle_omega_ops_plan` — $0.25: premium ops OS bundle (report + checklist + ADR + sha256 bundle).

## 4) Governance model (L1/L2/L3)
- L1: safe readonly monitoring/summaries
- L2: operational planning (still no risky execution)
- L3: irreversible impact (fund movement, live swaps, public posting, major config changes)

## 5) Two-step execution philosophy
1) Generate plan + checklist + proof bundle
2) Execute manually or via separate execution-mode offering gated behind L3 approval

## 6) CTA options
- A: try cheapest proof → clock sync → recovery plan → omega ops bundle
- B: comment use-case → receive copy/paste requirements payload + best matching offering
- C: infrastructure-first pitch → adopt templates, keep execution gated, accumulate proof artifacts
