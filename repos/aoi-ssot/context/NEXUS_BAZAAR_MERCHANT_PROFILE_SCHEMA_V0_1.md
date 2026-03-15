# Nexus Bazaar — Merchant Profile Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (public-safe schema) / STEALTH (scoring thresholds) / TOP SECRET (tokenomics/treasury)

> Purpose: Standard merchant metadata contract for FX/SWAP stalls in Nexus Bazaar.
> This schema is **public-safe**: it describes what merchants declare and what trust flags mean.

---

## 1) File name
- `merchant_profile.json`

## 2) Required fields
```json
{
  "merchant_id": "merchant_blue_rfq",
  "name": "Blue RFQ Stall",
  "version": "0.1",
  "quote_modes": ["RFQ", "OTC"],
  "supported_pairs": ["USDC/ETH", "USDC/SOL"],
  "size_limits": {"min": 10, "max": 100000},
  "fees_model": "fee_bps + external settlement fees (est.)",
  "constraints": ["report-only", "no custody", "no auto-signing"],
  "contact": {
    "preferred": "notion|email|x|telegram",
    "handle": "@merchant_handle"
  },
  "trust": {
    "guardian_pass": true,
    "guardian_tier": "T1",
    "sdna_verified": true,
    "core_temp": 50.0,
    "last_audited_at": "2026-02-20T12:00:00+09:00"
  },
  "settlement": {
    "supported_options": ["x402", "invoice", "onchain-intent"],
    "execution": "report-only"
  },
  "evidence_paths": [
    "context/proof_samples/...",
    "context/ADOPTION_GATE_CHECKLIST_V0_1.md"
  ]
}
```

---

## 3) Trust flags (meaning)
- `guardian_pass`: Skill-Guardian / security gate passed for the merchant implementation.
- `sdna_verified`: merchant code/artifacts are provenance-verified (S‑DNA).
- `core_temp`: reputation score (TEASER). If not implemented, may be `null`.

**Note:** exact thresholds/weights for routing are STEALTH.

---

## 4) Validation rules (v0.1)
- `merchant_id` must be stable and unique.
- `supported_pairs` must be non-empty.
- `size_limits.min` <= `size_limits.max`.
- `trust.guardian_pass=false` → merchant cannot be recommended by default (may be shown as "unverified").

---

## 5) Evidence
- Aggregator spec: `context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md`
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
