# Royalty Rail Spec — B-min (USDC on Base) v0.1

Last updated: 2026-02-20 (KST)
Status: DRAFT (execution gated)

## Goal
Provide a **real, auditable royalty payout rail** for skill creators:
- Ledger SSOT
- Monthly statements
- Payouts are **manual + approval-gated** (no auto transfers)

## Rail
- Asset: **USDC**
- Chain: **Base (EVM)**
- Address format: `0x...`

## Governance (must)
- L3 required for any real payout execution (money/on-chain)
- Default mode: report-only

## SSOT
- Royalty ledger SSOT: `aoi-core/state/royalty_ledger.json`
- Outreach template: `context/ROYALTY_OUTREACH_CONTACT_LOG_TEMPLATE_V0_1.md`
- Policy: `context/ROYALTY_AND_ATTRIBUTION_POLICY.md`

## Minimum data model (per entry)
- creator_name / handle
- skill_ref (source URL or slug)
- sdna_id (optional)
- amount_usdc
- chain=base
- recipient_address
- month (YYYY-MM)
- status: planned|approved|paid|void
- proof: tx_hash (only when paid)

## Monthly statement
- Generator script: `scripts/royalty_statement_generate.py`
- Output dir: `reports/royalty/`

## Notes
- This spec intentionally does NOT include private keys, signing automation, or auto payout.
