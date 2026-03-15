#!/usr/bin/env python3
"""Generate registry_search_index.json from Bazaar registry (denormalized).

Input:
- registry_index_enriched.json (preferred) OR registry_index.json

Output:
- registry_search_index.json

Deterministic; report-only.

Usage:
  python3 scripts/bazaar_registry_search_index_generate.py \
    --registry context/proof_samples/nexus_bazaar_registry_v0_1/registry_index_enriched.json \
    --out context/proof_samples/nexus_bazaar_registry_v0_1/registry_search_index.json
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


def load(p: Path) -> dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def write(p: Path, obj: Any) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_float(x: Any) -> float | None:
    try:
        return float(x)
    except Exception:
        return None


def catalog_offers(catalog_path: str | None) -> list[dict[str, Any]]:
    if not catalog_path:
        return []
    p = Path(catalog_path)
    if not p.exists():
        return []
    try:
        j = load(p)
    except Exception:
        return []

    offers = []
    skills = j.get("skills") if isinstance(j, dict) else None
    if isinstance(skills, list):
        for s in skills:
            if not isinstance(s, dict):
                continue
            offers.append(
                {
                    "skill_id": s.get("skill_id"),
                    "name": s.get("name"),
                    "category": s.get("category"),
                    "pricing": s.get("pricing"),
                    "generated_at": j.get("generated_at"),
                }
            )
    return offers


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--run-id", default=None)
    args = ap.parse_args()

    reg_path = Path(args.registry)
    out_path = Path(args.out)
    reg = load(reg_path)

    bazaar = reg.get("bazaar") or {}
    merchants = reg.get("merchants") or []

    run_id = args.run_id or f"bazaar-search-index-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    items: list[dict[str, Any]] = []

    for m in merchants:
        if not isinstance(m, dict):
            continue
        stall_type = m.get("type")
        mid = m.get("merchant_id")

        core_temp = safe_float(m.get("core_temp"))
        badges = m.get("badges") if isinstance(m.get("badges"), list) else []
        trust = m.get("trust_snapshot") if isinstance(m.get("trust_snapshot"), dict) else None

        # derive merchant name from profile when possible
        name = None
        prof = m.get("profile_path")
        if prof and Path(prof).exists():
            try:
                pj = load(Path(prof))
                name = pj.get("name")
                if trust is None and isinstance(pj.get("trust"), dict):
                    trust = pj.get("trust")
            except Exception:
                pass

        pointers = {
            "profile_path": m.get("profile_path"),
            "catalog_path": m.get("catalog_path"),
            "policy_path": m.get("policy_path"),
            "proof_latest": m.get("latest_proof_sample"),
            "proof_samples": m.get("proof_samples"),
        }

        merchant_block = {
            "merchant_id": mid,
            "name": name,
            "core_temp": core_temp,
            "badges": badges,
            "trust": {
                "guardian_pass": bool((trust or {}).get("guardian_pass")) if trust else None,
                "guardian_tier": (trust or {}).get("guardian_tier") if trust else None,
                "sdna_verified": bool((trust or {}).get("sdna_verified")) if trust else None,
            },
        }

        offers = catalog_offers(m.get("catalog_path"))

        if stall_type == "FX_STALL":
            # RFQ offers are implicit; create one index item per merchant
            items.append(
                {
                    "item_id": f"FX_STALL:{mid}:rfq",
                    "stall_type": stall_type,
                    "merchant": merchant_block,
                    "offer": {
                        "kind": "rfq",
                        "category": "fx",
                        "pricing": None,
                        "generated_at": reg.get("generated_at"),
                    },
                    "pointers": pointers,
                }
            )
            continue

        if not offers:
            # fallback: one item per merchant
            items.append(
                {
                    "item_id": f"{stall_type}:{mid}:default",
                    "stall_type": stall_type,
                    "merchant": merchant_block,
                    "offer": {
                        "kind": "audit" if stall_type == "AUDIT_STALL" else "skill",
                        "category": "audit" if stall_type == "AUDIT_STALL" else "general",
                        "pricing": None,
                        "generated_at": reg.get("generated_at"),
                    },
                    "pointers": pointers,
                }
            )
            continue

        for o in offers:
            items.append(
                {
                    "item_id": f"{stall_type}:{mid}:{o.get('skill_id')}",
                    "stall_type": stall_type,
                    "merchant": merchant_block,
                    "offer": {
                        "kind": "audit" if stall_type == "AUDIT_STALL" else "skill",
                        "category": o.get("category"),
                        "pricing": o.get("pricing"),
                        "generated_at": o.get("generated_at"),
                    },
                    "pointers": pointers,
                }
            )

    out = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "source_registry": str(reg_path),
        "exposure": bazaar.get("exposure") or reg.get("bazaar", {}).get("exposure") or "TEASER",
        "schema": "context/NEXUS_BAZAAR_SEARCH_INDEX_SCHEMA_V0_1.md",
        "items": items,
    }

    write(out_path, out)
    print(str(out_path))


if __name__ == "__main__":
    main()
