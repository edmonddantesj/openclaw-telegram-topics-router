# Main Project Building — DB Gap Note (2026-02-19)

User note: user believes prior discussion about main project building / DB spec may not be in SSOT DB.

## What we currently have (evidence)
- AOI Core (Main Project) supports approve→run→proof E2E.
  - Latest known proof run: beta001
  - Proof dir: /tmp/aoi_run_beta001/
  - Log: /tmp/aoi_core_beta001_run.20260218_135107.log
  - SSOT: CURRENT_STATE.md

## What is missing / uncertain
- A dedicated SSOT doc that defines the Main Project “DB” (schema, tables, lifecycle, required indexes, ingestion paths).
- If a prior conversation contains the intended DB design, it should be pasted and then distilled into SSOT.

## Proposed decision gate
- If user provides the prior conversation dump, follow the longform intake SOP:
  1) Read fully
  2) Summarize first (key decisions + open items)
  3) Propose DB schema + migration plan
  4) Save to SSOT (local + Notion)

## Next action
- Await user paste of the prior main-project DB conversation.
