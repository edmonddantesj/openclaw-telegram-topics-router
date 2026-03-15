#!/usr/bin/env python3
"""Regression tests for FX Stall + Skill Stall proof bundles.

Run:
  python3 scripts/test_bazaar_fx_skill_demo.py

No external deps.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_json(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def assert_true(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def assert_eq(a, b, msg: str) -> None:
    if a != b:
        raise AssertionError(f"{msg}: expected={b!r} got={a!r}")


def verify_manifest(dirpath: Path) -> None:
    mf = dirpath / "proof_manifest.json"
    assert_true(mf.exists(), f"missing proof_manifest.json: {dirpath}")

    j = read_json(mf)
    self_sha = j.get("self_sha256")
    assert_true(isinstance(self_sha, str) and len(self_sha) > 10, "manifest self_sha256 missing")

    # self_sha256 is defined as sha256(canonical_json(manifest without self_sha256))
    jj = dict(j)
    jj.pop("self_sha256", None)
    canon = json.dumps(jj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    expected = hashlib.sha256(canon).hexdigest()
    assert_eq(self_sha, expected, "manifest canonical self_sha256 mismatch")

    # Must include an entry for itself in files[] (sha may differ due to self-referential update)
    files = j.get("files") or []
    me = [x for x in files if x.get("path") == "proof_manifest.json"]
    assert_true(len(me) == 1, "manifest files[] must include proof_manifest.json")


def run(cmd: list[str]) -> None:
    p = subprocess.run(cmd, cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"command failed ({p.returncode}): {' '.join(cmd)}\n---\n{p.stdout}")


def test_fx_bundle() -> None:
    runner = ROOT / "scripts/bazaar_rfq_demo_runner.py"
    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "fx"
        outdir.mkdir(parents=True, exist_ok=True)
        run(
            [
                sys.executable,
                str(runner),
                "--pair",
                "USDC/ETH",
                "--side",
                "BUY",
                "--amount-in",
                "1000",
                "--trust-mode",
                "prefer_verified",
                "--deadline-ms",
                "2500",
                "--outdir",
                str(outdir),
                "--run-id",
                "test-fx",
            ]
        )

        for req in ["quote_request.json", "routing_report.json", "sha256sum.txt", "run_log.txt", "decision_summary.md"]:
            assert_true((outdir / req).exists(), f"FX bundle missing {req}")

        verify_manifest(outdir)

        rr = read_json(outdir / "routing_report.json")
        dec = rr.get("decision") or {}
        assert_true(dec.get("recommended_merchant_id"), "routing_report missing decision.recommended_merchant_id")


def test_skill_bundle() -> None:
    runner = ROOT / "scripts/skill_stall_demo_runner.py"
    with tempfile.TemporaryDirectory() as td:
        outdir = Path(td) / "skill"
        outdir.mkdir(parents=True, exist_ok=True)
        run(
            [
                sys.executable,
                str(runner),
                "--merchant-id",
                "merchant_summarizer_lite",
                "--skill-id",
                "summarizer_lite_v0",
                "--input",
                "This is sentence one. This is sentence two. This is sentence three.",
                "--outdir",
                str(outdir),
                "--run-id",
                "test-skill",
            ]
        )

        for req in ["skill_request.json", "skill_response.json", "sha256sum.txt", "run_log.txt", "decision_summary.md"]:
            assert_true((outdir / req).exists(), f"Skill bundle missing {req}")

        verify_manifest(outdir)

        resp = read_json(outdir / "skill_response.json")
        assert_true("output" in resp, "skill_response missing output")


def main() -> None:
    test_fx_bundle()
    test_skill_bundle()
    print("OK: FX + Skill proof bundle tests passed")


if __name__ == "__main__":
    main()
