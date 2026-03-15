#!/usr/bin/env bash
set -euo pipefail

# Public-safe deterministic proofs runner
# Goal: regenerate TEASER-safe evidence bundles + run deterministic tests.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

STAMP="$(date +"%Y%m%d_%H%M%S")"
OUTDIR="/tmp/aoi_public_teaser_proofs_${STAMP}"
mkdir -p "$OUTDIR"

echo "[1/5] Running deterministic proof tests (fail-closed)…"
python3 scripts/test_audit_stall_demo.py
python3 scripts/test_bazaar_fx_skill_demo.py

echo "[2/5] Regenerating Bazaar registry + search index (auto)…"
# Generate into a temp proof directory so we don't mutate existing samples.
REGDIR="$OUTDIR/nexus_bazaar_registry"
mkdir -p "$REGDIR"

python3 scripts/bazaar_registry_generate.py --outdir "$REGDIR" --auto
python3 scripts/bazaar_core_temp_compute.py --registry "$REGDIR/registry_index.json" --outdir "$REGDIR"
python3 scripts/bazaar_registry_render_md.py --registry "$REGDIR/registry_index_enriched.json" --out "$REGDIR/README.md"
python3 scripts/bazaar_registry_search_index_generate.py --registry "$REGDIR/registry_index_enriched.json" --out "$REGDIR/registry_search_index.json"

echo "[3/5] Generating Audit Stall PASS/FAIL demos…"
AUDITDIR="$OUTDIR/audit_stall"
mkdir -p "$AUDITDIR"

# Reuse sample audit_request.json and policy as inputs to generate fresh outdirs.
PASS_SAMPLE="context/proof_samples/audit_stall_demo_20260220_135002"
FAIL_SAMPLE="context/proof_samples/audit_stall_demo_20260220_140316_fail"

python3 scripts/audit_stall_demo_runner.py --input-file "$PASS_SAMPLE/audit_request.json" --policy "$PASS_SAMPLE/audit_policy.json" --outdir "$AUDITDIR/pass"
python3 scripts/audit_stall_demo_runner.py --input-file "$FAIL_SAMPLE/audit_request.json" --policy "$FAIL_SAMPLE/audit_policy.json" --outdir "$AUDITDIR/fail"

echo "[4/5] Generating S-DNA verify-only demo…"
SDNADIR="$OUTDIR/sdna_verify"
mkdir -p "$SDNADIR"

# Reuse an existing verified json as a stable target for the demo runner.
SDNA_SAMPLE_JSON="context/proof_samples/sdna_verify_demo_20260220_145451/sdna_verify.json"
python3 scripts/sdna_verify_demo_runner.py --target "$SDNA_SAMPLE_JSON" --outdir "$SDNADIR"

echo "[5/5] Done. Output paths:"
echo "- Registry:      $REGDIR"
echo "- Audit Stall:   $AUDITDIR"
echo "- S-DNA verify:  $SDNADIR"
echo "- Root outdir:   $OUTDIR"

echo "\nTip: For public copy, only use claims listed in context/PUBLIC_CLAIMS_REGISTRY_V0_1.md"
