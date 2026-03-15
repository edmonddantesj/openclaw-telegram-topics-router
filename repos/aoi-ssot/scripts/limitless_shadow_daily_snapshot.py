#!/usr/bin/env python3
"""Create a public-safe daily evidence bundle for the Limitless shadow experiment.

Inputs (local):
- /tmp/limitless_odds_btc_hourly.jsonl
- /tmp/limitless_settle_btc_hourly.jsonl

Outputs (repo):
- context/proof_samples/limitless_shadow_daily_<timestamp>/

Also runs an odds-based backtest over the last N hours (default 24) and stores metrics.

No secrets are copied.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

REPO = Path("/Users/silkroadcat/.openclaw/workspace/repos/aoi-ssot")
ODDS = Path("/tmp/limitless_odds_btc_hourly.jsonl")
SETTLE = Path("/tmp/limitless_settle_btc_hourly.jsonl")


def tail_lines(path: Path, n: int) -> list[str]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    return lines[-n:]


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, cwd=str(REPO), capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"cmd failed: {' '.join(cmd)}\n---\n{p.stdout}\n---\n{p.stderr}")
    return p.stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--tail", type=int, default=400)
    ap.add_argument("--p-floor", type=float, default=0.10)
    ap.add_argument("--slippage-bps", type=float, default=150.0)
    ap.add_argument("--max-bet-usd", type=float, default=1.0)
    args = ap.parse_args()

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = REPO / "context" / "proof_samples" / f"limitless_shadow_daily_{stamp}"
    outdir.mkdir(parents=True, exist_ok=True)

    counts = {
        "captured_at": stamp,
        "odds_exists": ODDS.exists(),
        "settle_exists": SETTLE.exists(),
        "odds_lines": sum(1 for _ in ODDS.open("r", encoding="utf-8", errors="ignore")) if ODDS.exists() else 0,
        "settle_lines": sum(1 for _ in SETTLE.open("r", encoding="utf-8", errors="ignore")) if SETTLE.exists() else 0,
    }
    (outdir / "counts.json").write_text(json.dumps(counts, ensure_ascii=False, indent=2), encoding="utf-8")

    (outdir / "odds_tail.jsonl").write_text("\n".join(tail_lines(ODDS, args.tail)) + "\n", encoding="utf-8")
    (outdir / "settle_tail.jsonl").write_text("\n".join(tail_lines(SETTLE, args.tail)) + "\n", encoding="utf-8")

    # Run backtest and capture the generated /tmp folder path from stdout.
    out = run(
        [
            "python3",
            "scripts/v6_limitless_hourly_odds_backtest.py",
            "--hours",
            str(args.hours),
            "--p-floor",
            str(args.p_floor),
            "--slippage-bps",
            str(args.slippage_bps),
            "--max-bet-usd",
            str(args.max_bet_usd),
        ]
    )

    (outdir / "repro.txt").write_text(
        "\n".join(
            [
                "# Commands",
                f"python3 scripts/v6_limitless_hourly_odds_backtest.py --hours {args.hours} --p-floor {args.p_floor} --slippage-bps {args.slippage_bps} --max-bet-usd {args.max_bet_usd}",
                "",
                "# Stdout",
                out.strip(),
                "",
            ]
        ),
        encoding="utf-8",
    )

    # Also store a tiny metrics json derived from stdout lines.
    metrics = {"hours": args.hours, "p_floor": args.p_floor, "slippage_bps": args.slippage_bps, "max_bet_usd": args.max_bet_usd}
    for line in out.splitlines():
        if line.startswith("wallet_start="):
            metrics["stdout"] = line.strip()
    (outdir / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: wrote {outdir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
