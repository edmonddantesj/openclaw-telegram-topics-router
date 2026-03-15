#!/usr/bin/env python3
"""Regression checks for AOI Council policy scorecard thresholds.

Usage:
  python3 scripts/test_council_policy_profile_regression.py \
      --config context/AOI_COUNCIL_POLICY_ENGINE_CONFIG_V0_1.json

  python3 scripts/test_council_policy_profile_regression.py \
      --label conservative \
      --config context/AOI_COUNCIL_POLICY_ENGINE_PROFILE_CONSERVATIVE_V0_1.json
"""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

import aoi_council_run as runner


CASES = [
    {
        "name": "safe_open",
        "topic": "moltbook draft summary",
        "context": "release notes for open copy",
        "evidence": [],
        "expected": {"status": "PASS", "score": 0},
    },
    {
        "name": "wallet_guard",
        "topic": "wallet signing and deploy sequence",
        "context": "pre-launch deploy checklist",
        "evidence": [],
        "expected": {"status": "WARN", "score": 45},
    },
    {
        "name": "top_secret_exposure",
        "topic": "distribution of treasury",
        "context": "private key handling strategy draft",
        "evidence": [],
        "expected": {"status": "WARN", "score": 45},
    },
    {
        "name": "final_marker",
        "topic": "public final artifact",
        "context": "publish-safe note",
        "evidence": [],
        "expected": {"status": "WARN", "score": 20},
    },
]


def write_temp_evidence(lines: list[str]) -> list[str]:
    if not lines:
        return []
    paths = []
    for content in lines:
        fp = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
        fp.write(content.encode("utf-8"))
        fp.close()
        paths.append(fp.name)
    return paths


def run_case(case: dict, config_path: str) -> tuple[bool, str]:
    inputs = {"topic": case["topic"], "context": case["context"]}
    evidence_paths = write_temp_evidence(case.get("evidence", []))

    runner._load_policy_config(config_path)
    policy = runner._policy_check(inputs, "pro", evidence_paths)
    summary = policy.get("summary", {})
    status = str(summary.get("status"))
    score = int(summary.get("score", 0))

    expected = case["expected"]
    ok = status == expected["status"] and score == expected["score"]
    if not ok:
        return (
            False,
            (
                f"{case['name']} mismatch under {config_path}: "
                f"got status={status}, score={score} "
                f"expected status={expected['status']}, score={expected['score']}"
            ),
        )
    return (True, f"{case['name']} OK under {config_path}: status={status}, score={score}")


def main() -> int:
    p = argparse.ArgumentParser(description="AOI Council policy profile regression")
    p.add_argument("--config", required=True, help="Path to policy config/profile JSON")
    p.add_argument("--label", default="default", help="Profile label")
    args = p.parse_args()

    # ensure top-level profile overrides are loaded as-is
    runner._load_policy_config(args.config)

    print(f"[policy-regression] label={args.label}, config={args.config}")
    all_ok = True
    for case in CASES:
        ok, msg = run_case(case, args.config)
        print(msg)
        all_ok = all_ok and ok

    if all_ok:
        print("[policy-regression] PASS")
        return 0

    print("[policy-regression] FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
