#!/usr/bin/env python3
"""Render registry_index.json to a human-readable README.md.

Usage:
  python3 scripts/bazaar_registry_render_md.py \
    --registry context/proof_samples/nexus_bazaar_registry_v0_1/registry_index.json \
    --out context/proof_samples/nexus_bazaar_registry_v0_1/README.md
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--registry", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    reg_path = Path(args.registry)
    out_path = Path(args.out)
    reg = load(reg_path)

    bazaar = reg.get("bazaar", {})
    merchants = reg.get("merchants", [])

    lines: list[str] = []
    lines.append(f"# {bazaar.get('name','Nexus Bazaar')} — Registry (v{bazaar.get('version','0.1')})")
    lines.append("")
    lines.append(f"- generated_at: {reg.get('generated_at')}")
    lines.append(f"- run_id: {reg.get('run_id')}")
    lines.append(f"- exposure: {bazaar.get('exposure')}")
    lines.append("")

    # Group by type
    grouped: dict[str, list[dict[str, Any]]] = {}
    for m in merchants:
        grouped.setdefault(m.get("type", "UNKNOWN"), []).append(m)

    for t in sorted(grouped.keys()):
        lines.append(f"## {t}")
        lines.append("")
        for m in grouped[t]:
            mid = m.get("merchant_id")
            temp = m.get("core_temp")
            badges = m.get("badges") if isinstance(m.get("badges"), list) else []
            badge_txt = (" " + " ".join(badges)) if badges else ""
            if isinstance(temp, (int, float)):
                label = " (Booting)" if float(temp) == 0.0 else ""
                lines.append(f"- **{mid}** — 🌡️ {float(temp):.1f}°C{label}{badge_txt}")
            else:
                lines.append(f"- **{mid}**{badge_txt}")
            lines.append(f"  - profile: `{m.get('profile_path')}`")
            if m.get("catalog_path"):
                lines.append(f"  - catalog: `{m.get('catalog_path')}`")
            if m.get("policy_path"):
                lines.append(f"  - policy: `{m.get('policy_path')}`")
            if m.get("proof_samples") and isinstance(m.get("proof_samples"), list):
                # Prefer explicit PASS/FAIL samples when present
                ps = m.get("proof_samples")
                if len(ps) == 1:
                    lines.append(f"  - proof (sample): `{ps[0]}`")
                elif len(ps) >= 2:
                    lines.append(f"  - proof bundles: PASS `{ps[0]}` / FAIL `{ps[1]}`")
            if m.get("latest_proof_sample"):
                lines.append(f"  - proof (latest): `{m.get('latest_proof_sample')}`")
        lines.append("")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(str(out_path))


if __name__ == "__main__":
    main()
