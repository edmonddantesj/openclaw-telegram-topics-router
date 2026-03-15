#!/usr/bin/env python3
"""Query Nexus Bazaar registry_search_index.json (deterministic, local).

Examples:
  python3 scripts/bazaar_query.py --index context/proof_samples/nexus_bazaar_registry_v0_1/registry_search_index.json \
    --stall FX_STALL --sort core_temp:desc

  python3 scripts/bazaar_query.py --index ... --category audit
  python3 scripts/bazaar_query.py --index ... --price-max 0.02 --currency USDC

Output:
- prints a compact table-like text (markdown-ish)

"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(p: Path) -> dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def safe_float(x: Any) -> float | None:
    try:
        return float(x)
    except Exception:
        return None


def get_nested(d: dict[str, Any], path: str) -> Any:
    cur: Any = d
    for part in path.split('.'):
        if not isinstance(cur, dict):
            return None
        cur = cur.get(part)
    return cur


def match(item: dict[str, Any], args) -> bool:
    if args.stall and item.get("stall_type") != args.stall:
        return False

    if args.merchant:
        m = item.get("merchant") or {}
        hay = f"{m.get('merchant_id','')} {m.get('name','')}".lower()
        if args.merchant.lower() not in hay:
            return False

    if args.category:
        cat = (item.get("offer") or {}).get("category")
        if (cat or "").lower() != args.category.lower():
            return False

    if args.currency or args.price_min is not None or args.price_max is not None:
        pricing = (item.get("offer") or {}).get("pricing")
        if not isinstance(pricing, dict):
            return False
        if args.currency and (pricing.get("currency") != args.currency):
            return False
        amt = safe_float(pricing.get("amount"))
        if amt is None:
            return False
        if args.price_min is not None and amt < args.price_min:
            return False
        if args.price_max is not None and amt > args.price_max:
            return False

    if args.temp_min is not None or args.temp_max is not None:
        temp = safe_float((item.get("merchant") or {}).get("core_temp"))
        if temp is None:
            return False
        if args.temp_min is not None and temp < args.temp_min:
            return False
        if args.temp_max is not None and temp > args.temp_max:
            return False

    if args.sdna is not None:
        sd = ((item.get("merchant") or {}).get("trust") or {}).get("sdna_verified")
        if bool(sd) != bool(args.sdna):
            return False

    if args.guardian is not None:
        gp = ((item.get("merchant") or {}).get("trust") or {}).get("guardian_pass")
        if bool(gp) != bool(args.guardian):
            return False

    return True


def sort_items(items: list[dict[str, Any]], spec: str | None) -> list[dict[str, Any]]:
    if not spec:
        return items
    key, _, direction = spec.partition(':')
    direction = (direction or 'asc').lower().strip()
    reverse = direction == 'desc'

    def k(it: dict[str, Any]):
        v = get_nested(it, key)
        f = safe_float(v)
        if f is not None:
            return f
        if v is None:
            return ""
        return str(v)

    return sorted(items, key=k, reverse=reverse)


def render(items: list[dict[str, Any]], limit: int) -> str:
    out = []
    out.append(f"count={len(items)}")
    out.append("")
    out.append("stall_type | merchant | temp | badges | category | price | proof")
    out.append("--- | --- | ---: | --- | --- | --- | ---")

    for it in items[:limit]:
        m = it.get("merchant") or {}
        offer = it.get("offer") or {}
        ptr = it.get("pointers") or {}

        badges = " ".join(m.get("badges") or [])
        temp = m.get("core_temp")
        temp_s = f"{float(temp):.1f}" if isinstance(temp, (int, float)) else "-"

        price = "-"
        pricing = offer.get("pricing")
        if isinstance(pricing, dict) and pricing.get("amount") is not None:
            price = f"{pricing.get('amount')} {pricing.get('currency','')}"

        proof = ptr.get("proof_latest") or ""

        out.append(
            " | ".join(
                [
                    str(it.get("stall_type") or ""),
                    str(m.get("name") or m.get("merchant_id") or ""),
                    temp_s,
                    badges,
                    str(offer.get("category") or ""),
                    price,
                    str(proof),
                ]
            )
        )

    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--stall", default=None)
    ap.add_argument("--merchant", default=None, help="substring match on id/name")
    ap.add_argument("--category", default=None)
    ap.add_argument("--currency", default=None)
    ap.add_argument("--price-min", type=float, default=None)
    ap.add_argument("--price-max", type=float, default=None)
    ap.add_argument("--temp-min", type=float, default=None)
    ap.add_argument("--temp-max", type=float, default=None)
    ap.add_argument("--sdna", action="store_true", default=None)
    ap.add_argument("--no-sdna", dest="sdna", action="store_false")
    ap.add_argument("--guardian", action="store_true", default=None)
    ap.add_argument("--no-guardian", dest="guardian", action="store_false")
    ap.add_argument("--sort", default=None, help="e.g. merchant.core_temp:desc or offer.pricing.amount:asc")
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()

    idx = load(Path(args.index))
    items = idx.get("items") or []
    items = [it for it in items if isinstance(it, dict)]

    filtered = [it for it in items if match(it, args)]
    filtered = sort_items(filtered, args.sort)

    print(render(filtered, args.limit))


if __name__ == "__main__":
    main()
