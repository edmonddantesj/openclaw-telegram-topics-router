#!/usr/bin/env python3
"""Audit Stall Demo Runner (report-only)

Creates a reproducible proof bundle for an *audit merchant* (Skill-Guardian style).

This is a deterministic demo and does NOT execute untrusted code.
It simulates a Tier-1 style scan over a provided text snippet (e.g., a skill manifest)
by checking for risky patterns defined in a versioned `audit_policy.json`.

Outputs (per aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md):
- audit_request.json
- audit_policy.json
- guardian_report.json
- decision_summary.md
- proof_manifest.json
- sha256sum.txt
- run_log.txt

Usage:
  python3 scripts/audit_stall_demo_runner.py \
    --merchant-id merchant_guardian_audit \
    --audit-id guardian_report_v0 \
    --input-file <path> \
    --outdir context/proof_samples/audit_stall_demo_...

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


def scan_text(text: str, policy: dict[str, Any]) -> dict[str, Any]:
    """Very small deterministic scan. Not a real security scanner."""

    findings: list[dict[str, Any]] = []

    defaults = policy.get("defaults", {}) if isinstance(policy, dict) else {}
    tier = str(defaults.get("tier", "T1"))
    rules = policy.get("rules", []) if isinstance(policy, dict) else []

    for r in rules:
        try:
            code = str(r.get("code"))
            sev = str(r.get("severity", "medium"))
            pat = str(r.get("pattern"))
            msg = str(r.get("message", ""))
            rx = re.compile(pat, re.I)
        except Exception:
            continue

        if rx.search(text):
            findings.append({"code": code, "severity": sev, "message": msg})

    # Severity gating (policy-driven)
    fail_on = defaults.get("fail_on_severity", ["high"])
    fail_on_set = {str(x).lower() for x in (fail_on or [])}
    severities = {str(f.get("severity", "")).lower() for f in findings}

    if severities & fail_on_set:
        verdict = "FAIL"
    else:
        verdict = "PASS" if not findings else "REVIEW"

    risk = "low" if verdict == "PASS" else ("high" if verdict == "FAIL" else "medium")

    return {
        "tier": tier,
        "verdict": verdict,
        "risk": risk,
        "findings": findings,
        "policy_id": policy.get("policy_id"),
        "policy_version": policy.get("version"),
        "notes": "Deterministic demo scan; do not treat as a full security audit.",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--merchant-id", default="merchant_guardian_audit")
    ap.add_argument("--audit-id", default="guardian_report_v0")
    ap.add_argument("--input-file", required=True)
    ap.add_argument("--policy", default=None, help="Path to audit_policy.json (optional; default uses outdir/audit_policy.json if present)")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--run-id", default=None)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    run_id = args.run_id or f"audit-stall-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    in_path = Path(args.input_file)
    text = in_path.read_text(encoding="utf-8", errors="ignore")

    # Load policy
    policy_path = Path(args.policy) if args.policy else (outdir / "audit_policy.json")
    if not policy_path.exists():
        raise SystemExit("audit policy missing: provide --policy or place audit_policy.json in outdir")
    policy = json.loads(policy_path.read_text(encoding="utf-8", errors="ignore"))

    # request
    req = {
        "request_id": run_id,
        "merchant_id": args.merchant_id,
        "audit_id": args.audit_id,
        "policy": {
            "path": str(policy_path),
            "sha256": sha256_file(policy_path),
            "policy_id": policy.get("policy_id"),
            "version": policy.get("version"),
        },
        "input": {
            "path": str(in_path),
            "sha256": sha256_file(in_path),
            "bytes": in_path.stat().st_size,
        },
        "mode": "report-only",
        "generated_at": now_kst_iso(),
    }
    write_json(outdir / "audit_request.json", req)

    # scan
    scan = scan_text(text, policy)
    report = {
        "request_id": run_id,
        "merchant_id": args.merchant_id,
        "audit_id": args.audit_id,
        "generated_at": now_kst_iso(),
        "guardian_report": scan,
    }
    write_json(outdir / "guardian_report.json", report)

    # decision summary
    tl = scan["verdict"]
    decision = f"""# Audit Stall Run (Demo)

## TL;DR
- Audit: **{args.audit_id}** (merchant: **{args.merchant_id}**)
- Verdict: **{tl}** (tier {scan['tier']}, risk {scan['risk']})

## Input
- file: `{in_path}`
- sha256: `{req['input']['sha256']}`

## Findings
"""
    if not scan["findings"]:
        decision += "- (none)\n"
    else:
        for f in scan["findings"]:
            decision += f"- {f['code']} ({f['severity']}): {f['message']}\n"

    decision += """

## Guardrails
- Demo is deterministic and does not execute the input.
- Report-only: no signing, no external effects.
- Evidence-first: proof_manifest + sha256sum + run_log.
"""
    write_text(outdir / "decision_summary.md", decision)

    # run_log
    run_log = "\n".join(
        [
            f"generated_at={now_kst_iso()}",
            f"run_id={run_id}",
            f"cmd=python3 scripts/audit_stall_demo_runner.py --merchant-id {args.merchant_id} --audit-id {args.audit_id} --input-file {in_path} --outdir {outdir}",
            "mode=report-only",
        ]
    )
    write_text(outdir / "run_log.txt", run_log)

    # proof manifest
    manifest_path = outdir / "proof_manifest.json"
    manifest: dict[str, Any] = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "inputs_digest": sha256_file(outdir / "audit_request.json"),
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

    write_json(manifest_path, manifest)
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})

    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # refresh file hashes after manifest write
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
