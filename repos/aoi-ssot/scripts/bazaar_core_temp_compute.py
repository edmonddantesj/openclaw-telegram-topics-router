#!/usr/bin/env python3
"""Compute Core-Temperature for Bazaar registry entries (deterministic, report-only).

Reads:
- registry_index.json
- merchant profile JSONs referenced by registry entries

Writes:
- registry_index_enriched.json (same shape + computed fields)
- core_temp_report.json (summary)

No external calls. No mutations of input files.

Usage:
  python3 scripts/bazaar_core_temp_compute.py \
    --registry context/proof_samples/nexus_bazaar_registry_v0_1/registry_index.json \
    --outdir  context/proof_samples/nexus_bazaar_registry_v0_1

"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any


def now_kst_iso() -> str:
    utc = datetime.now(timezone.utc)
    kst = utc + timedelta(hours=9)
    return kst.strftime("%Y-%m-%dT%H:%M:%S+09:00")


def read_json(p: Path) -> dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def write_json(p: Path, obj: Any) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def clamp_temp(x: float) -> float:
    if x < 0:
        return 0.0
    if x > 99.9:
        return 99.9
    return round(x, 1)


def compute_temp(profile: dict[str, Any], merchant_entry: dict[str, Any]) -> tuple[float, list[str]]:
    trust = (profile.get("trust") or {}) if isinstance(profile, dict) else {}

    guardian_pass = bool(trust.get("guardian_pass"))
    guardian_tier = str(trust.get("guardian_tier") or "").upper().strip()
    sdna_verified = bool(trust.get("sdna_verified"))

    temp = 0.0
    badges: list[str] = []

    has_proof = bool(merchant_entry.get("latest_proof_sample")) or bool(merchant_entry.get("proof_samples"))

    if guardian_pass:
        temp += 10
        badges.append("🛡️Guardian")
        if guardian_tier == "T2":
            temp += 5
        elif guardian_tier == "T3":
            temp += 10

    if sdna_verified:
        temp += 6
        badges.append("🧬S-DNA")

    if has_proof:
        temp += 4

    return clamp_temp(temp), badges


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()

    reg_path = Path(args.registry)
    outdir = Path(args.outdir)

    reg = read_json(reg_path)
    merchants = reg.get("merchants") or []

    enriched = dict(reg)
    enriched["core_temp"] = {
        "spec": "context/NEXUS_BAZAAR_CORE_TEMP_SPEC_V0_1.md",
        "computed_at": now_kst_iso(),
        "version": "0.1",
        "story": {"boot": 0.0, "human_baseline": 36.5},
    }

    report = {
        "computed_at": now_kst_iso(),
        "registry": str(reg_path),
        "count": len(merchants),
        "results": [],
    }

    out_merchants = []
    for m in merchants:
        m2 = dict(m)
        prof_path = m.get("profile_path")
        profile = {}
        if prof_path:
            try:
                profile = read_json(Path(prof_path))
            except Exception:
                profile = {}

        temp, badges = compute_temp(profile, m)
        m2["core_temp"] = temp
        m2["badges"] = badges

        # also embed a minimal trust snapshot for rendering
        trust = (profile.get("trust") or {}) if isinstance(profile, dict) else {}
        m2["trust_snapshot"] = {
            "guardian_pass": bool(trust.get("guardian_pass")),
            "guardian_tier": trust.get("guardian_tier"),
            "sdna_verified": bool(trust.get("sdna_verified")),
        }

        out_merchants.append(m2)
        report["results"].append(
            {
                "merchant_id": m.get("merchant_id"),
                "type": m.get("type"),
                "core_temp": temp,
                "badges": badges,
            }
        )

    enriched["merchants"] = out_merchants

    write_json(outdir / "registry_index_enriched.json", enriched)
    write_json(outdir / "core_temp_report.json", report)

    print(str(outdir / "registry_index_enriched.json"))


if __name__ == "__main__":
    main()
