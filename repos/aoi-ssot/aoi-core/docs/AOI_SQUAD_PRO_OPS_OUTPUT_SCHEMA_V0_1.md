# AOI Squad Pro — Ops Output Schema (v0.1)

Purpose: define a *public-safe*, fixed structure for any AOI Squad Pro run output.
This is inspired by “dimensions” style schemas, but **ops-native** (not personality).

## The 6 Ops Dimensions (fixed)
1) **Intent** — what we intended to do (goal, scope, constraints)
2) **Action** — what we actually executed (commands, versions, runtime)
3) **Artifacts** — what was produced (paths, urls, sha256)
4) **Risk/Gates** — L1/L2/L3 classification, caps, kill-switches, policy notes
5) **Result** — success/failure + key metrics (e.g., edge, win proxy, counts)
6) **Next** — next 1–3 actions (queue-ready)

## Minimal JSON example
```json
{
  "schema": "aoi.ops_output.v0.1",
  "run_id": "beta001",
  "intent": {"goal": "...", "scope": "..."},
  "action": {"commands": ["..."], "versions": {"openclaw": "2026.2.17"}},
  "artifacts": [{"path": "/tmp/...", "sha256": "...", "note": "..."}],
  "risk": {"tier": "L2", "gates": ["shadow-only"], "caps": {"usd_per_day": 3}},
  "result": {"status": "ok", "metrics": {"ev_rows": 9}},
  "next": ["...", "..."]
}
```

## Notes
- Proof Bundle schema is separately tracked in `aoi-core/docs/PROOF_SCHEMA_V0_1.json`.
- This schema is meant for *human-readable reports* and *machine ingestion*.
