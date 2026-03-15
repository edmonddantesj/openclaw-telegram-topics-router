# SOL Phase 2 Roadmap v0.1 (Solana chain enablement)

Last updated: 2026-02-20 (KST)
Status: DRAFT

## Goal (user confirmed)
- Objective: **ALL**
  1) Base → Solana bridge planning
  2) Solana-side team skill purchase / settlement wallet experiment
  3) Meteora DLMM ops (future)
- Wallet types allowed for the experiment: **Both**
  - Human wallets: Phantom / Backpack
  - Custodial/SDK wallets (service)

## Non-negotiables (governance)
- Any real on-chain execution (bridge/transfer/bet) is **L3**.
- Default for SOL Phase 2 is **report-only + approval-card + proof bundle**.
- Canary-first: tiny canary tx before any material movement.

## Phase 2A — Report-only foundation (no signing)
### Outputs (proof bundle)
- `context/proof_samples/sol_phase2_report_<timestamp>/`
  - `approval_card.md`
  - `policy_eval.json`
  - `risk_notes.md`
  - `public_safe_scan.txt`
  - `sha256sum.txt`

### Tasks
1) Define chain boundary:
   - Base remains micro-preapproved swap-only.
   - Solana actions are planned only.
2) Define allowlists:
   - Allowed protocols: (TBD) deBridge / CCTP / Meteora
   - Allowed assets: USDC only (initial)
3) Define failure codes:
   - E_CHAIN_MISMATCH / E_WALLET_PROVIDER_UNREACHABLE / E_PROOF_MISSING / E_BRIDGE_UNSUPPORTED / E_RATE_LIMIT

## Phase 2B — Wallet onboarding experiment (still no automatic transfers)
- Collect wallet_intent for:
  - Phantom/Backpack addresses
  - Custodial wallet identifiers
- Validate: address format + chain + network
- Proof requirements: same VCP fields (proof_dir, input_digest, sha256, logs)

## Phase 2C — Meteora DLMM ops (future)
- Only after 2A+2B are stable.
- Requires explicit L3 approval for any deposits/LP actions.

## Dependencies
- ACP wallet governance: `context/ACP_WALLET_GOVERNANCE_V0_1.md`
- Survival autonomy DRY-RUN spec: `context/SURVIVAL_AUTONOMY_DRYRUN_SPEC_V0_1.md`
- ACP automation policy: `aoi-core/state/acp_automation_policy_v0_1.json`

## Open Questions
- Which bridge rail first: deBridge vs CCTP?
- Solana RPC provider + rate limit posture.
- Where to store Solana wallet intents (ledger vs Notion).
