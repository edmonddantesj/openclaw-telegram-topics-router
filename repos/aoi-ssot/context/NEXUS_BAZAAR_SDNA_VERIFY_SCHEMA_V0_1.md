# Nexus Bazaar — `sdna_verify.json` Schema v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Status: DRAFT
Exposure: TEASER (public-safe)

## Purpose
Provide a **verify-only** (no mutation) S‑DNA verification artifact for skills/merchants.

- Default stance: **verify/report-only**.
- No imprinting into third-party artifacts unless explicit consent (L3).

## File
- `sdna_verify.json`

## Minimal schema (v0.1)
```json
{
  "generated_at": "2026-02-20T14:20:00+09:00",
  "run_id": "sdna-verify-20260220_142000",
  "mode": "verify-only",
  "target": {
    "kind": "file|bundle",
    "path": "skills/foo/SKILL.md",
    "sha256": "..."
  },
  "protocol": {
    "protocol_version": "1.0",
    "author_id": null,
    "sdna_id": null
  },
  "result": {
    "verified": false,
    "signal": "none|present|verified|mismatch",
    "notes": "..."
  },
  "evidence": {
    "matches": [
      {"type": "header", "value": "S-DNA: AOI-..."}
    ]
  }
}
```

## Interpretation (TEASER-safe)
- `verified=true` means: S‑DNA marker was detected and matched the expected format in this verify routine.
- This is **not** a full security audit. Combine with `guardian_report.json` for security posture.

## Evidence
- Artifacts standard: `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
