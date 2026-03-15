# AOI Squad Pro — Proof Bundle Demo (V0.1)

This folder is a **public-safe** proof bundle produced by the one-click demo:

```bash
cd ~/.openclaw/workspace && bash scripts/aoi_squad_pro_oneclick_demo.sh
```

## Files
- `proof.json` — machine-readable manifest (schema: `aoi-core/docs/PROOF_SCHEMA_V0_1.json`)
- `sha256sum.txt` — sha256 for every file in this bundle
- `report.md` — human-readable notes
- `artifacts/` — masked tails + digest + `public_safe_scan.txt`

## Safety
- Shadow-only; no fund movement.
- Scan result is recorded in `artifacts/public_safe_scan.txt`.
