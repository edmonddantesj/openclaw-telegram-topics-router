# Nexus Bazaar — routing_report.json Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (schema) / STEALTH (weights/thresholds)

> Purpose: Standardize how the Aggregator explains routing decisions and rejections.

---

## 1) File name
- `routing_report.json`

## 2) Minimal schema
```json
{
  "run_id": "bazaar-rfq-...",
  "generated_at": "2026-02-20T12:00:00+09:00",
  "pair": "USDC/ETH",
  "side": "BUY",
  "amount_in": 1000,
  "policies": {
    "trust_mode": "prefer_verified",
    "deadline_ms": 2500
  },
  "merchants": [
    {
      "merchant_id": "merchant_blue_rfq",
      "status": "OK",
      "trust": {"guardian_pass": true, "sdna_verified": true, "core_temp": null},
      "quote": {"price": 3096.5, "fee_bps": 12, "effective_price": 3100.2158, "latency_ms": 180, "valid_until_sec": 15},
      "eligibility": {"eligible": true, "reasons": []}
    },
    {
      "merchant_id": "merchant_silver_otc",
      "status": "REJECT",
      "reject": {"code": "TIMEOUT", "human": "..."},
      "eligibility": {"eligible": false, "reasons": ["TIMEOUT"]}
    }
  ],
  "decision": {
    "recommended_merchant_id": "merchant_blue_rfq",
    "reason_codes": ["BEST_EFFECTIVE_PRICE", "TRUST_OK"],
    "notes": "..."
  }
}
```

## 3) Reason codes (initial)
- `BEST_EFFECTIVE_PRICE`
- `LOWEST_LATENCY`
- `TRUST_OK`
- `PREFERRED_SDNA`
- `EXCLUDED_UNVERIFIED`
- `TIMEOUT`
- `QUOTE_EXPIRED`
- `RISK_POLICY_BLOCK`

---

## 4) Evidence
- Aggregator spec: `context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md`
- Merchant profile schema: `context/NEXUS_BAZAAR_MERCHANT_PROFILE_SCHEMA_V0_1.md`
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
