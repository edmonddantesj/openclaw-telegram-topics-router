# Nexus Bazaar — registry_index.json Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: OPEN (schema)

> Purpose: A single index file that aggregates Bazaar merchants and their offerings.
> This is the minimal "Storefront layer" registry artifact.

---

## 1) File name
- `registry_index.json`

## 2) Minimal schema
```json
{
  "generated_at": "2026-02-20T13:10:00+09:00",
  "bazaar": {
    "name": "Nexus Bazaar",
    "version": "0.1",
    "exposure": "TEASER"
  },
  "merchants": [
    {
      "merchant_id": "merchant_blue_rfq",
      "type": "FX_STALL",
      "profile_path": "merchant_profiles/merchant_blue_rfq.merchant_profile.json",
      "catalog_path": null,
      "policy_path": null,
      "latest_proof_sample": "context/proof_samples/bazaar_rfq_demo_.../"
    },
    {
      "merchant_id": "merchant_summarizer_lite",
      "type": "SKILL_STALL",
      "profile_path": "merchant_profiles/merchant_summarizer_lite.merchant_profile.json",
      "catalog_path": "skill_catalog.json",
      "policy_path": null,
      "latest_proof_sample": "context/proof_samples/skill_stall_demo_.../"
    }
  ]
}
```

## 3) Merchant types (initial)
- `FX_STALL` — RFQ/OTC/intent-first settlement merchants
- `SKILL_STALL` — skill/service merchants
- `DATA_STALL` — datasets/indexes
- `AUDIT_STALL` — guardian/QC/rebuild services

---

## 4) Evidence
- Bazaar aggregator spec: `context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md`
- Merchant profile schema: `context/NEXUS_BAZAAR_MERCHANT_PROFILE_SCHEMA_V0_1.md`
- Skill catalog schema: `context/NEXUS_BAZAAR_SKILL_CATALOG_SCHEMA_V0_1.md`
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
