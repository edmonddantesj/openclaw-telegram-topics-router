#!/usr/bin/env python3
"""Skill Stall Demo Runner (report-only)

Creates a reproducible proof bundle for a *skill merchant* in Nexus Bazaar.

This demo is deterministic and does NOT call any external LLM.
It simulates a "Summarizer Lite" skill by producing a simple extractive summary.

Outputs (per aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md):
- skill_request.json
- skill_response.json
- decision_summary.md
- proof_manifest.json
- sha256sum.txt
- run_log.txt

Usage:
  python3 scripts/skill_stall_demo_runner.py \
    --merchant-id merchant_summarizer_lite \
    --skill-id summarizer_lite_v0 \
    --input "..." \
    --outdir context/proof_samples/skill_stall_demo

"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any


def now_kst_iso() -> str:
    utc = datetime.now(timezone.utc)
    kst = utc + timedelta(hours=9)
    return kst.strftime("%Y-%m-%dT%H:%M:%S+09:00")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def simple_summary(text: str, max_sentences: int = 2) -> str:
    # Very simple deterministic summarizer: pick first N non-empty sentences.
    # Split on '.', '!', '?' keeping it naive.
    import re

    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        return ""
    return " ".join(parts[:max_sentences])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--merchant-id", default="merchant_summarizer_lite")
    ap.add_argument("--skill-id", default="summarizer_lite_v0")
    ap.add_argument("--input", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--run-id", default=None)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    run_id = args.run_id or f"skill-stall-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # 1) request
    req = {
        "request_id": run_id,
        "merchant_id": args.merchant_id,
        "skill_id": args.skill_id,
        "input": {
            "text": args.input,
            "max_sentences": 2,
        },
        "mode": "report-only",
        "generated_at": now_kst_iso(),
    }
    write_json(outdir / "skill_request.json", req)

    # 2) response
    out_text = simple_summary(args.input, 2)
    resp = {
        "request_id": run_id,
        "merchant_id": args.merchant_id,
        "skill_id": args.skill_id,
        "status": "OK",
        "output": {
            "summary": out_text,
            "method": "extractive_first_sentences",
        },
        "generated_at": now_kst_iso(),
    }
    write_json(outdir / "skill_response.json", resp)

    # 3) decision summary
    decision = f"""# Skill Stall Run (Demo)

## TL;DR
- Skill: **{args.skill_id}** (merchant: **{args.merchant_id}**)
- Output: deterministic extractive summary (no external LLM calls).

## Inputs
- text_len: {len(args.input)}
- max_sentences: 2

## Output
{out_text}

## Guardrails
- Report-only: no external calls, no secrets.
- Evidence-first: proof_manifest + sha256sum + run_log.
"""
    write_text(outdir / "decision_summary.md", decision)

    # 4) run_log
    run_log = "\n".join(
        [
            f"generated_at={now_kst_iso()}",
            f"run_id={run_id}",
            f"cmd=python3 scripts/skill_stall_demo_runner.py --merchant-id {args.merchant_id} --skill-id {args.skill_id} --input <text> --outdir {outdir}",
            "mode=report-only",
            "llm_calls=0",
        ]
    )
    write_text(outdir / "run_log.txt", run_log)

    # 5) proof manifest
    manifest_path = outdir / "proof_manifest.json"
    manifest: dict[str, Any] = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "inputs_digest": sha256_file(outdir / "skill_request.json"),
        "exposure_tier": "OPEN",
        "approvals": [],
        "evidence_paths": [
            "aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md",
            "context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md",
        ],
        "files": [],
    }

    # Compute manifest self hash over canonical JSON **excluding** self_sha256.
    def manifest_canonical_sha256(obj: dict[str, Any]) -> str:
        o = dict(obj)
        o.pop("self_sha256", None)
        b = json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(b).hexdigest()

    # First pass: write then enumerate
    write_json(manifest_path, manifest)
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # Second pass: refresh file hashes after manifest write
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # sha256sum
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    lines = [f"{sha256_file(p)}  {p.relative_to(outdir).as_posix()}" for p in all_files]
    write_text(outdir / "sha256sum.txt", "\n".join(lines))

    print(str(outdir))


if __name__ == "__main__":
    main()
