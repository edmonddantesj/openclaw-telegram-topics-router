# Nexus Bazaar — skill_catalog.json Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: OPEN (schema)

> Purpose: Standard listing format for a skill merchant's offerings.

---

## 1) File name
- `skill_catalog.json`

## 2) Minimal schema
```json
{
  "merchant_id": "merchant_summarizer_lite",
  "generated_at": "2026-02-20T12:00:00+09:00",
  "skills": [
    {
      "skill_id": "summarizer_lite_v0",
      "name": "Summarizer Lite",
      "category": "skill",
      "pricing": {"mode": "per_call", "amount": 0.01, "currency": "USDC"},
      "io": {"input": ["text"], "output": ["summary"]},
      "constraints": ["report-only demo", "no secrets"],
      "evidence_paths": ["context/proof_samples/..."],
      "exposure": "OPEN"
    }
  ]
}
```

---

## 3) Evidence
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
