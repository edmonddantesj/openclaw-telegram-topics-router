#!/usr/bin/env python3
"""Mini regression tests for Audit Stall demo + Registry auto-scan.

Goals
- Deterministic PASS/FAIL behavior via policy-driven severity gating.
- Registry auto-scan includes AUDIT_STALL and surfaces PASS/FAIL bundles.

Run:
  python3 scripts/test_audit_stall_demo.py

No external deps.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

PASS_SAMPLE = ROOT / "context/proof_samples/audit_stall_demo_20260220_135002"
FAIL_SAMPLE = ROOT / "context/proof_samples/audit_stall_demo_20260220_140316_fail"


def run(cmd: list[str]) -> None:
    p = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"command failed ({p.returncode}): {' '.join(cmd)}\n---\n{p.stdout}")


def read_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def assert_eq(a, b, msg: str) -> None:
    if a != b:
        raise AssertionError(f"{msg}: expected={b!r} got={a!r}")


def test_audit_pass_fail() -> None:
    runner = ROOT / "scripts/audit_stall_demo_runner.py"

    # PASS: scan a benign input with PASS policy
    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "pass"
        outdir.mkdir(parents=True, exist_ok=True)
        # reuse policy file (versioned)
        policy = PASS_SAMPLE / "audit_policy.json"
        inp = ROOT / "scripts/bazaar_registry_generate.py"
        run(
            [
                sys.executable,
                str(runner),
                "--merchant-id",
                "merchant_guardian_audit",
                "--audit-id",
                "guardian_report_v0",
                "--input-file",
                str(inp),
                "--policy",
                str(policy),
                "--outdir",
                str(outdir),
                "--run-id",
                "test-pass",
            ]
        )
        rep = read_json(outdir / "guardian_report.json")
        assert_eq(rep["guardian_report"]["verdict"], "PASS", "PASS verdict")

    # FAIL: scan the failing sample with FAIL policy (has high severity rule)
    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "fail"
        outdir.mkdir(parents=True, exist_ok=True)
        policy = FAIL_SAMPLE / "audit_policy.json"
        inp = FAIL_SAMPLE / "fail_sample.txt"
        run(
            [
                sys.executable,
                str(runner),
                "--merchant-id",
                "merchant_guardian_audit",
                "--audit-id",
                "guardian_report_v0",
                "--input-file",
                str(inp),
                "--policy",
                str(policy),
                "--outdir",
                str(outdir),
                "--run-id",
                "test-fail",
            ]
        )
        rep = read_json(outdir / "guardian_report.json")
        assert_eq(rep["guardian_report"]["verdict"], "FAIL", "FAIL verdict")
        assert_eq(rep["guardian_report"]["risk"], "high", "FAIL risk")


def test_registry_autoscan_includes_audit() -> None:
    gen = ROOT / "scripts/bazaar_registry_generate.py"

    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "registry"
        outdir.mkdir(parents=True, exist_ok=True)
        run(
            [
                sys.executable,
                str(gen),
                "--outdir",
                str(outdir),
                "--auto",
                "--run-id",
                "test-registry",
            ]
        )
        idx = read_json(outdir / "registry_index.json")
        merchants = idx.get("merchants", [])
        audit = [m for m in merchants if m.get("type") == "AUDIT_STALL"]
        if not audit:
            raise AssertionError("AUDIT_STALL missing from registry_index.json")
        m0 = audit[0]
        ps = m0.get("proof_samples")
        if not isinstance(ps, list) or len(ps) < 2:
            raise AssertionError("AUDIT_STALL proof_samples missing PASS/FAIL entries")


def main() -> None:
    test_audit_pass_fail()
    test_registry_autoscan_includes_audit()
    print("OK: audit stall + registry tests passed")


if __name__ == "__main__":
    main()
