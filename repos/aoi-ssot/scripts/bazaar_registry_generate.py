#!/usr/bin/env python3
"""Generate Nexus Bazaar registry_index.json (storefront index) from proof_samples.

Scans known proof sample folders and emits:
- registry_index.json
- proof_manifest.json
- sha256sum.txt
- run_log.txt

This is report-only and public-safe: it only outputs *pointers* to local paths.

Usage:
  # Explicit inputs
  python3 scripts/bazaar_registry_generate.py \
    --outdir context/proof_samples/nexus_bazaar_registry_v0_1 \
    --fx-sample context/proof_samples/bazaar_rfq_demo_20260220_124616 \
    --skill-sample context/proof_samples/skill_stall_demo_20260220_125349

  # Auto-scan latest proof samples (no args other than outdir)
  python3 scripts/bazaar_registry_generate.py \
    --outdir context/proof_samples/nexus_bazaar_registry_v0_1 \
    --auto

  # Auto-scan also includes AUDIT stalls if present
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


def list_fx_merchants(fx_sample: Path) -> list[dict[str, Any]]:
    merchants: list[dict[str, Any]] = []
    mp_dir = fx_sample / "merchant_profiles"
    if not mp_dir.exists():
        return merchants

    for p in sorted(mp_dir.glob("*.merchant_profile.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
            mid = obj.get("merchant_id")
            if not mid:
                continue
            merchants.append(
                {
                    "merchant_id": mid,
                    "type": "FX_STALL",
                    "profile_path": str(p),
                    "catalog_path": None,
                    "policy_path": None,
                    "latest_proof_sample": str(fx_sample) + "/",
                }
            )
        except Exception:
            continue

    return merchants


def list_skill_merchants(skill_sample: Path) -> list[dict[str, Any]]:
    merchants: list[dict[str, Any]] = []
    mp_dir = skill_sample / "merchant_profiles"
    catalog = skill_sample / "skill_catalog.json"

    if mp_dir.exists():
        for p in sorted(mp_dir.glob("*.merchant_profile.json")):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
                mid = obj.get("merchant_id")
                if not mid:
                    continue
                merchants.append(
                    {
                        "merchant_id": mid,
                        "type": "SKILL_STALL",
                        "profile_path": str(p),
                        "catalog_path": str(catalog) if catalog.exists() else None,
                        "policy_path": None,
                        "latest_proof_sample": str(skill_sample) + "/",
                    }
                )
            except Exception:
                continue

    return merchants


def list_audit_merchants(audit_sample: Path, audit_pass: Path | None = None, audit_fail: Path | None = None) -> list[dict[str, Any]]:
    merchants: list[dict[str, Any]] = []
    mp_dir = audit_sample / "merchant_profiles"
    catalog = audit_sample / "skill_catalog.json"

    if not mp_dir.exists():
        return merchants

    for p in sorted(mp_dir.glob("*.merchant_profile.json")):
        try:
            obj = json.loads(p.read_text(encoding="utf-8"))
            mid = obj.get("merchant_id")
            if not mid:
                continue
            policy = audit_sample / "audit_policy.json"
            proof_samples = []
            # Prefer explicit PASS/FAIL samples if available
            if audit_pass:
                proof_samples.append(str(audit_pass) + "/")
            if audit_fail and (not audit_pass or audit_fail != audit_pass):
                proof_samples.append(str(audit_fail) + "/")

            merchants.append(
                {
                    "merchant_id": mid,
                    "type": "AUDIT_STALL",
                    "profile_path": str(p),
                    "catalog_path": str(catalog) if catalog.exists() else None,
                    "policy_path": str(policy) if policy.exists() else None,
                    "latest_proof_sample": str(audit_sample) + "/",
                    "proof_samples": proof_samples if proof_samples else None,
                }
            )
        except Exception:
            continue

    return merchants


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--fx-sample", default=None)
    ap.add_argument("--skill-sample", default=None)
    ap.add_argument(
        "--auto",
        action="store_true",
        help="Auto-detect latest FX/Skill proof samples under context/proof_samples.",
    )
    ap.add_argument(
        "--samples-root",
        default="context/proof_samples",
        help="Root folder for auto-scan mode.",
    )
    ap.add_argument("--bazaar-version", default="0.1")
    ap.add_argument("--exposure", default="TEASER")
    ap.add_argument("--run-id", default=None)
    args = ap.parse_args()

    outdir = Path(args.outdir)

    samples_root = Path(args.samples_root)

    def pick_latest_dir(prefix: str) -> Path | None:
        if not samples_root.exists():
            return None
        cands = [p for p in samples_root.iterdir() if p.is_dir() and p.name.startswith(prefix)]
        if not cands:
            return None
        cands.sort(key=lambda p: (p.name, p.stat().st_mtime), reverse=True)
        return cands[0]

    def pick_latest_audit_by_verdict(want: str) -> Path | None:
        """Pick latest audit_stall_demo_* sample that has guardian_report.json with verdict==want."""
        if not samples_root.exists():
            return None
        want_u = want.upper().strip()
        cands = [p for p in samples_root.iterdir() if p.is_dir() and p.name.startswith("audit_stall_demo_")]
        if not cands:
            return None
        cands.sort(key=lambda p: (p.name, p.stat().st_mtime), reverse=True)
        for p in cands:
            rep = p / "guardian_report.json"
            if not rep.exists():
                continue
            try:
                obj = json.loads(rep.read_text(encoding="utf-8"))
                verdict = str(obj.get("guardian_report", {}).get("verdict", "")).upper()
                if verdict == want_u:
                    return p
            except Exception:
                continue
        return None

    fx_sample_s = args.fx_sample
    skill_sample_s = args.skill_sample
    audit_sample_s: str | None = None
    audit_pass_s: str | None = None
    audit_fail_s: str | None = None

    if args.auto:
        fx = pick_latest_dir("bazaar_rfq_demo_")
        sk = pick_latest_dir("skill_stall_demo_")
        au = pick_latest_dir("audit_stall_demo_")
        apass = pick_latest_audit_by_verdict("PASS")
        afail = pick_latest_audit_by_verdict("FAIL")
        if not fx or not sk:
            raise SystemExit(f"auto-scan failed under {samples_root}: fx={bool(fx)} skill={bool(sk)}")
        fx_sample_s = str(fx)
        skill_sample_s = str(sk)
        audit_sample_s = str(au) if au else None
        audit_pass_s = str(apass) if apass else None
        audit_fail_s = str(afail) if afail else None

    if not fx_sample_s or not skill_sample_s:
        raise SystemExit("Provide --fx-sample and --skill-sample, or use --auto")

    fx_sample = Path(fx_sample_s)
    skill_sample = Path(skill_sample_s)
    audit_sample = Path(audit_sample_s) if audit_sample_s else None
    audit_pass = Path(audit_pass_s) if audit_pass_s else None
    audit_fail = Path(audit_fail_s) if audit_fail_s else None

    run_id = args.run_id or f"bazaar-registry-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    merchants = []
    merchants += list_fx_merchants(fx_sample)
    merchants += list_skill_merchants(skill_sample)
    if audit_sample:
        merchants += list_audit_merchants(audit_sample, audit_pass=audit_pass, audit_fail=audit_fail)

    registry = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "bazaar": {"name": "Nexus Bazaar", "version": args.bazaar_version, "exposure": args.exposure},
        "inputs": {
            "fx_sample": str(fx_sample),
            "skill_sample": str(skill_sample),
            "audit_sample": str(audit_sample) if audit_sample else None,
            "audit_pass_sample": str(audit_pass) if audit_pass else None,
            "audit_fail_sample": str(audit_fail) if audit_fail else None,
        },
        "merchants": merchants,
    }

    write_json(outdir / "registry_index.json", registry)

    run_log = "\n".join(
        [
            f"generated_at={now_kst_iso()}",
            f"run_id={run_id}",
            f"cmd=python3 scripts/bazaar_registry_generate.py --outdir {outdir} --fx-sample {fx_sample} --skill-sample {skill_sample} --auto {args.auto} --samples-root {samples_root}",
            "mode=report-only",
        ]
    )
    write_text(outdir / "run_log.txt", run_log)

    # proof manifest
    manifest_path = outdir / "proof_manifest.json"
    manifest: dict[str, Any] = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "inputs_digest": sha256_file(outdir / "registry_index.json"),
        "exposure_tier": "OPEN",
        "approvals": [],
        "evidence_paths": [
            "context/NEXUS_BAZAAR_REGISTRY_INDEX_SCHEMA_V0_1.md",
            "aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md",
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
    manifest["self_sha256"] = sha256_file(manifest_path)
    write_json(manifest_path, manifest)

    # sha256sum
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    lines = [f"{sha256_file(p)}  {p.relative_to(outdir).as_posix()}" for p in all_files]
    write_text(outdir / "sha256sum.txt", "\n".join(lines))

    print(str(outdir))


if __name__ == "__main__":
    main()
