#!/usr/bin/env python3
"""Bazaar RFQ Demo Runner (report-only)

Creates a reproducible proof bundle for the Nexus Bazaar Aggregator concept.

Outputs (per aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md):
- quote_request.json
- merchant_profiles/<merchant_id>.merchant_profile.json (optional in demo)
- quotes/<merchant_id>.quote_response.json
- routing_report.json
- decision_summary.md
- proof_manifest.json
- sha256sum.txt
- run_log.txt

No live execution. No signing. No custody.

Usage:
  python3 scripts/bazaar_rfq_demo_runner.py \
    --pair USDC/ETH --side BUY --amount-in 1000 \
    --outdir context/proof_samples/bazaar_rfq_demo

"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from dataclasses import dataclass
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


@dataclass
class Quote:
    merchant_id: str
    price: float  # quote currency per base
    fee_bps: int
    latency_ms: int
    valid_sec: int
    status: str = "OK"
    reject_code: str | None = None
    reject_human: str | None = None

    def effective_price(self) -> float:
        # BUY: lower effective price better. fee increases cost.
        return self.price * (1.0 + self.fee_bps / 10000.0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pair", default="USDC/ETH")
    ap.add_argument("--side", choices=["BUY", "SELL"], default="BUY")
    ap.add_argument("--amount-in", type=float, default=1000.0)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--run-id", default=None)
    ap.add_argument(
        "--trust-mode",
        choices=["ignore", "prefer_verified"],
        default="prefer_verified",
        help="Ranking policy. prefer_verified excludes guardian_pass=false from recommendation and prefers sdna_verified=true.",
    )
    ap.add_argument(
        "--deadline-ms",
        type=int,
        default=2500,
        help="Quote response deadline. Quotes arriving after this are treated as TIMEOUT.",
    )
    args = ap.parse_args()

    outdir = Path(args.outdir)
    run_id = args.run_id or f"bazaar-rfq-{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Structure
    quotes_dir = outdir / "quotes"
    quotes_dir.mkdir(parents=True, exist_ok=True)

    # 1) Quote request
    quote_request = {
        "request_id": run_id,
        "pair": args.pair,
        "side": args.side,
        "amount_in": args.amount_in,
        "slippage_bps_max": 50,
        "deadline_ms": args.deadline_ms,
        "caller_context": "DEMO (report-only). No signing. Evidence-first RFQ comparison.",
        "generated_at": now_kst_iso(),
    }
    write_json(outdir / "quote_request.json", quote_request)

    # 2) Merchant quotes (demo data)
    # Simulate: 3 merchants, 2 OK, 1 reject.
    demo_quotes: list[Quote] = [
        Quote("merchant_silver_otc", price=3100.00, fee_bps=8, latency_ms=3200, valid_sec=20),
        Quote("merchant_blue_rfq", price=3096.50, fee_bps=12, latency_ms=180, valid_sec=15),
        Quote(
            "merchant_red_guarded",
            price=0.0,
            fee_bps=0,
            latency_ms=900,
            valid_sec=0,
            status="REJECT",
            reject_code="RISK_POLICY_BLOCK",
            reject_human="Blocked by merchant policy: pair temporarily disabled for demo.",
        ),
    ]

    # Trust flags (from merchant_profiles/* if present)
    # For demo: if file missing, assume unknown (treated as not verified).
    trust: dict[str, dict[str, Any]] = {}
    mp_dir = outdir / "merchant_profiles"
    if mp_dir.exists():
        for p in mp_dir.glob("*.merchant_profile.json"):
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
                mid = obj.get("merchant_id")
                if mid:
                    trust[mid] = obj.get("trust", {}) or {}
            except Exception:
                continue

    quote_responses: list[dict[str, Any]] = []
    for q in demo_quotes:
        # Freshness/timeout enforcement (B-2)
        if q.status == "OK" and q.latency_ms > args.deadline_ms:
            q.status = "REJECT"
            q.reject_code = "TIMEOUT"
            q.reject_human = f"Quote arrived after deadline_ms={args.deadline_ms}."

        if q.status == "OK" and q.valid_sec <= 0:
            q.status = "REJECT"
            q.reject_code = "QUOTE_EXPIRED"
            q.reject_human = "Quote validity window elapsed (valid_until_sec<=0)."

        if q.status == "OK":
            amount_out = args.amount_in / q.price if args.pair.endswith("/ETH") and args.side == "BUY" else None
            resp = {
                "request_id": run_id,
                "merchant_id": q.merchant_id,
                "status": "OK",
                "price": q.price,
                "fee_bps": q.fee_bps,
                "fee_estimate": args.amount_in * (q.fee_bps / 10000.0),
                "latency_ms": q.latency_ms,
                "valid_until_sec": q.valid_sec,
                "amount_out_estimate": amount_out,
                "settlement_options": ["x402", "invoice", "onchain-intent"],
                "received_before_deadline": q.latency_ms <= args.deadline_ms,
            }
        else:
            resp = {
                "request_id": run_id,
                "merchant_id": q.merchant_id,
                "status": "REJECT",
                "reject_reason_code": q.reject_code,
                "reject_reason_human": q.reject_human,
                "latency_ms": q.latency_ms,
                "received_before_deadline": q.latency_ms <= args.deadline_ms,
            }
        quote_responses.append(resp)
        write_json(quotes_dir / f"{q.merchant_id}.quote_response.json", resp)

    # 3) Routing decision + routing_report.json
    # Trust-aware ranking policy:
    # - Exclude guardian_pass=false from recommendation.
    # - Prefer sdna_verified=true when prices are close (implemented as sort key).
    ok_quotes = [q for q in demo_quotes if q.status == "OK"]

    def guardian_pass(mid: str) -> bool:
        return bool((trust.get(mid, {}) or {}).get("guardian_pass", False))

    def sdna_verified(mid: str) -> bool:
        return bool((trust.get(mid, {}) or {}).get("sdna_verified", False))

    eligible = ok_quotes
    excluded: list[Quote] = []
    if args.trust_mode == "prefer_verified":
        eligible = [q for q in ok_quotes if guardian_pass(q.merchant_id)]
        excluded = [q for q in ok_quotes if not guardian_pass(q.merchant_id)]

    if not eligible:
        # Fallback: if everything is unverified, still pick by price but mark as unverified.
        eligible = ok_quotes

    # Sort key:
    # - effective price (lower better)
    # - sdna_verified (True preferred) -> sort False after True
    # - latency
    eligible.sort(key=lambda x: (x.effective_price(), 0 if sdna_verified(x.merchant_id) else 1, x.latency_ms))
    best = eligible[0]

    # Build routing_report.json (standardized, machine-readable)
    def trust_obj(mid: str) -> dict[str, Any]:
        t = trust.get(mid, {}) or {}
        return {
            "guardian_pass": bool(t.get("guardian_pass", False)),
            "sdna_verified": bool(t.get("sdna_verified", False)),
            "core_temp": t.get("core_temp", None),
        }

    routing_merchants: list[dict[str, Any]] = []
    for q in demo_quotes:
        entry: dict[str, Any] = {"merchant_id": q.merchant_id}

        # Attach trust if present
        entry["trust"] = trust_obj(q.merchant_id)

        # Eligibility
        reasons: list[str] = []
        eligible_flag = True

        # Freshness/timeout-driven rejections are in the quote_response.json; duplicate reason codes here.
        # If quote was rejected in responses, mark ineligible.
        # (We recompute from q.status/q.reject_code since demo runner mutates Quote state.)
        if q.status != "OK":
            eligible_flag = False
            if q.reject_code:
                reasons.append(str(q.reject_code))

        # Trust exclusion
        if args.trust_mode == "prefer_verified" and not guardian_pass(q.merchant_id):
            # Exclude from recommendation unless already rejected.
            eligible_flag = False
            reasons.append("EXCLUDED_UNVERIFIED")

        entry["eligibility"] = {"eligible": eligible_flag, "reasons": sorted(set(reasons))}

        # Quote fields (when OK)
        if q.status == "OK":
            entry["status"] = "OK"
            entry["quote"] = {
                "price": q.price,
                "fee_bps": q.fee_bps,
                "effective_price": q.effective_price(),
                "latency_ms": q.latency_ms,
                "valid_until_sec": q.valid_sec,
            }
        else:
            entry["status"] = "REJECT"
            entry["reject"] = {"code": q.reject_code, "human": q.reject_human}

        routing_merchants.append(entry)

    # Decision reason codes
    decision_reasons = ["BEST_EFFECTIVE_PRICE", "TRUST_OK"]
    if args.trust_mode == "prefer_verified":
        decision_reasons.append("EXCLUDED_UNVERIFIED")
    if sdna_verified(best.merchant_id):
        decision_reasons.append("PREFERRED_SDNA")

    routing_report = {
        "run_id": run_id,
        "generated_at": now_kst_iso(),
        "pair": args.pair,
        "side": args.side,
        "amount_in": args.amount_in,
        "policies": {"trust_mode": args.trust_mode, "deadline_ms": args.deadline_ms},
        "merchants": routing_merchants,
        "decision": {
            "recommended_merchant_id": best.merchant_id,
            "reason_codes": decision_reasons,
            "notes": "Demo routing report. Report-only; no execution.",
        },
    }

    write_json(outdir / "routing_report.json", routing_report)

    best_gp = guardian_pass(best.merchant_id)
    best_sdna = sdna_verified(best.merchant_id)

    decision_md = f"""# RFQ Routing Decision (Demo)

## TL;DR
- Best route: **{best.merchant_id}**
- Reason: lowest effective price (price + fee) under trust policy (guardian_pass={best_gp}, sdna_verified={best_sdna}).

## Inputs
- pair: {args.pair}
- side: {args.side}
- amount_in: {args.amount_in}

## Quotes compared
"""

    for q in demo_quotes:
        if q.status == "OK":
            gp = guardian_pass(q.merchant_id)
            sv = sdna_verified(q.merchant_id)
            decision_md += (
                f"- {q.merchant_id}: price={q.price}, fee_bps={q.fee_bps}, "
                f"effective_price={q.effective_price():.6f}, latency_ms={q.latency_ms}, "
                f"guardian_pass={gp}, sdna_verified={sv}\n"
            )
        else:
            decision_md += f"- {q.merchant_id}: REJECT ({q.reject_code})\n"

    decision_md += f"""

## Trust policy
- trust_mode: `{args.trust_mode}`
- guardian_pass=false merchants are not recommended by default.
- sdna_verified=true is preferred when choosing between eligible quotes.

## Freshness policy
- deadline_ms: `{args.deadline_ms}`
- latency_ms > deadline_ms => REJECT(TIMEOUT)
- valid_until_sec <= 0 => REJECT(QUOTE_EXPIRED)

## Guardrails
- Report-only: no signing, no trade execution.
- Evidence-first: proof_manifest + sha256sum + run_log.
"""

    write_text(outdir / "decision_summary.md", decision_md)

    # 4) run_log
    run_log = "\n".join(
        [
            f"generated_at={now_kst_iso()}",
            f"run_id={run_id}",
            f"cmd=python3 scripts/bazaar_rfq_demo_runner.py --pair {args.pair} --side {args.side} --amount-in {args.amount_in} --outdir {outdir} --trust-mode {args.trust_mode} --deadline-ms {args.deadline_ms}",
            "mode=report-only",
        ]
    )
    write_text(outdir / "run_log.txt", run_log)

    # 5) proof manifest (self hash computed after write)
    manifest_path = outdir / "proof_manifest.json"
    manifest: dict[str, Any] = {
        "generated_at": now_kst_iso(),
        "run_id": run_id,
        "inputs_digest": sha256_file(outdir / "quote_request.json"),
        "exposure_tier": "TEASER",
        "approvals": [],
        "evidence_paths": [
            "context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md",
            "aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md",
        ],
        "files": [],
    }

    # Compute manifest self hash over canonical JSON **excluding** self_sha256.
    # (Avoids impossible self-referential fixed-point hashing.)
    def manifest_canonical_sha256(obj: dict[str, Any]) -> str:
        o = dict(obj)
        o.pop("self_sha256", None)
        b = json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(b).hexdigest()

    # First pass: write with files list (incl. manifest placeholder)
    write_json(manifest_path, manifest)
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # Second pass: refresh file hashes after manifest write
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    files_list = []
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        files_list.append({"path": rel, "sha256": sha256_file(p), "bytes": p.stat().st_size})
    manifest["files"] = files_list
    manifest["self_sha256"] = manifest_canonical_sha256(manifest)
    write_json(manifest_path, manifest)

    # 6) sha256sum
    lines = []
    all_files = sorted([p for p in outdir.rglob("*") if p.is_file()])
    for p in all_files:
        rel = p.relative_to(outdir).as_posix()
        lines.append(f"{sha256_file(p)}  {rel}")
    write_text(outdir / "sha256sum.txt", "\n".join(lines))

    print(str(outdir))


if __name__ == "__main__":
    main()
