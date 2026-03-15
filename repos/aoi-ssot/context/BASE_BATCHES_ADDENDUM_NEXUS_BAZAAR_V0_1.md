# Base Batches — Addendum (Nexus Bazaar proof-first demos) v0.1

Last updated: 2026-02-20 (KST)
Exposure: TEASER (public-safe)

## What changed / clarification
We refined the project narrative into **Nexus Bazaar**: a proof-first market for agent merchants.

The key point: we are not building a custodial exchange. Our default mode is **report-only + approval-gated** for any execution.

## What we can demo today (public-safe)
1) **FX/SWAP Stall (RFQ / intent-first)**
- Collect quotes from multiple merchant agents
- Enforce **trust** (guardian_pass / sdna_verified) and **freshness** (deadline_ms, TIMEOUT/QUOTE_EXPIRED)
- Produce an auditable proof bundle (manifest + hashes + logs)

2) **Skill Stall (Summarizer Lite)**
- Demonstrates that Bazaar supports multiple merchant types under one evidence standard
- Demo is deterministic (0 LLM calls)

## Evidence artifacts (local paths)
- RFQ proof bundle: `context/proof_samples/bazaar_rfq_demo_20260220_124616/`
- Skill stall proof bundle: `context/proof_samples/skill_stall_demo_20260220_125349/`
- Storefront registry bundle:
  - `context/proof_samples/nexus_bazaar_registry_v0_1/registry_index.json`
  - `context/proof_samples/nexus_bazaar_registry_v0_1/README.md`

## Why Base (one sentence)
Base is a practical settlement layer for future execution because it is fast and low-cost; meanwhile we keep execution **OFF by default** and focus on auditable routing + proofs.

## Guardrails
- No profit/alpha guarantees.
- No tokenomics/treasury discussion (Stealth $AOI).
- Any signing/execution/wallet actions are L3 → explicit approval.
