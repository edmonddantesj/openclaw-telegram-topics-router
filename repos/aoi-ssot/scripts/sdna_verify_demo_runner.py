#!/usr/bin/env python3
"""S-DNA verify-only demo runner (deterministic, report-only).

This emits a proof bundle that includes `sdna_verify.json`.

NOTE: v0.1 is intentionally lightweight: it checks for common S-DNA markers
in plaintext files. It does NOT modify the target.

Usage:
  python3 scripts/sdna_verify_demo_runner.py \
    --target skills/aoineco-team-council/SKILL.md \
    --outdir context/proof_samples/sdna_verify_demo_...

"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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


def manifest_canonical_sha256(obj: dict[str, Any]) -> str:
    o = dict(obj)
    o.pop("self_sha256", None)
    b = json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(b).hexdigest()


def detect_sdna(text: str) -> tuple[bool, str, list[dict[str, str]]]:
    matches: list[dict[str, str]] = []

    # Common markers
    for rx in [
        re.compile(r"S-DNA:\s*(AOI-[A-Za-z0-9\-]+)", re.I),
        re.compile(r"sdna\s*=\s*\{[^\}]+\}", re.I),
        re.compile(r"AOI-\d{4}-\d{4}-SDNA-[0-9a-fA-F]+"),
    ]:
        m = rx.search(text)
        if m:
            matches.append({"type": "marker", "value": m.group(0)})

    if not matches:
        return False, "none", []

    # v0.1: presence implies verified (format-only)
    return True, "verified", matches


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--declared-author-id", default=None)
    ap.add_argument("--declared-sdna-id", default=None)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    run_id = args.run_id or f"sdna-verify-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    target = Path(args.target)
    raw = target.read_text(encoding="utf-8", errors="ignore")

    verified, signal, matches = detect_sdna(raw)

    sdna_verify = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "mode": "verify-only",
        "target": {
            "kind": "file",
            "path": str(target),
            "sha256": sha256_file(target),
        },
        "protocol": {
            "protocol_version": "1.0",
            "author_id": args.declared_author_id,
            "sdna_id": args.declared_sdna_id,
        },
        "result": {
            "verified": bool(verified),
            "signal": signal,
            "notes": "Verify-only demo: format/presence check. Combine with guardian_report for security.",
        },
        "evidence": {"matches": matches},
    }

    write_json(outdir / "sdna_verify.json", sdna_verify)

    decision = f"""# S-DNA Verify Run (Demo)

## TL;DR
- target: `{target}`
- verified: **{sdna_verify['result']['verified']}** (signal={signal})

## Guardrails
- verify-only: no file mutation.
- deterministic: no external calls.
"""
    write_text(outdir / "decision_summary.md", decision)

    run_log = "\n".join(
        [
            f"generated_at={now_kst_iso()}",
            f"run_id={run_id}",
            f"cmd=python3 scripts/sdna_verify_demo_runner.py --target {target} --outdir {outdir}",
            "mode=report-only",
        ]
    )
    write_text(outdir / "run_log.txt", run_log)

    manifest_path = outdir / "proof_manifest.json"
    manifest: dict[str, Any] = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "inputs_digest": sha256_file(outdir / "sdna_verify.json"),
        "exposure_tier": "OPEN",
        "approvals": [],
        "evidence_paths": [
            "aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md",
            "context/NEXUS_BAZAAR_SDNA_VERIFY_SCHEMA_V0_1.md",
        ],
        "files": [],
    }

    write_json(manifest_path, manifest)
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # refresh file hashes + self sha
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
