# Nexus Bazaar — `registry_search_index.json` Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (public-safe)

## Purpose
Create a **denormalized search/sort index** for Bazaar storefronts.
- Enables filtering by merchant name/id, stall type, category, price, dates, and trust signals.
- Avoids any profit/alpha wording; purely discovery + governance metadata.

## File
- `registry_search_index.json`

## Minimal schema (v0.1)
```json
{
  "generated_at": "2026-02-20T15:00:00+09:00",
  "run_id": "bazaar-search-index-20260220_150000",
  "source_registry": "context/proof_samples/nexus_bazaar_registry_v0_1/registry_index_enriched.json",
  "exposure": "TEASER",
  "items": [
    {
      "item_id": "AUDIT_STALL:merchant_guardian_audit:guardian_report_v0",
      "stall_type": "AUDIT_STALL",
      "merchant": {
        "merchant_id": "merchant_guardian_audit",
        "name": "Guardian Audit Stall",
        "core_temp": 14.0,
        "badges": ["🛡️Guardian"],
        "trust": {"guardian_pass": true, "guardian_tier": "T1", "sdna_verified": false}
      },
      "offer": {
        "kind": "audit|skill|rfq",
        "category": "audit",
        "pricing": {"amount": 0.01, "currency": "USDC", "mode": "per_call"},
        "generated_at": "2026-02-20T14:03:16+09:00"
      },
      "pointers": {
        "profile_path": "...",
        "catalog_path": "...",
        "policy_path": "...",
        "proof_latest": "...",
        "proof_samples": ["..."]
      }
    }
  ]
}
```

## Sort keys (recommended)
- `merchant.core_temp` desc
- `offer.generated_at` desc
- `offer.pricing.amount` asc

## Notes
- Popularity ranking is **not** included in v0.1 (to avoid ambiguous/financial interpretation). If needed, introduce a separate `activity_score` based on proof bundle recency/count.

