#!/usr/bin/env python3
"""V6 × Limitless-style Hourly YES/NO Simulation (24h) — v0.1

Goal
- Simulate a Limitless-like hourly market:
  - At each hour start t, you may place at most ONE bet (YES/LONG or NO/SHORT) or skip.
  - Settlement at t+1h: price_up => YES wins, price_down => NO wins.
- Track wallet curve over a 24h window.
- Avoid "doubling down" by construction: only one bet per hour; no overlapping positions.

Data
- Signals: V6 archives `the-alpha-oracle/results/v6_*BTC-USD.json`
  - Use `v6_enhanced.final_direction` as YES/NO direction proxy.
  - Use `omega_verdict` confidence/veto and `v6_enhanced.agreement` for filters.
- Prices: yfinance BTC-USD hourly candles (1h)

Payout model (simple even-odds)
- If correct:  wallet += bet * (1 - fee_total)
- If wrong:    wallet -= bet * (1 + fee_total)
Where fee_total defaults to 0.002 (0.2% round trip).

Bet sizing
- Default: bet = wallet * position_size (capped by wallet)
- position_size from `v6_enhanced.position_size` (0..1)

Selection per hour
- Many V6 runs can occur within the same hour.
- We pick ONE candidate run per hour by "decision strength":
  score = omega_conf * position_size
  (penalize veto heavily)

Skip rule (recommended)
- Only bet when the selected run passes filters:
  - agreement in {STRONG, WEAK} (configurable)
  - omega_conf >= threshold (default 0.58)
  - veto_applied == False
  - position_size > 0

Outputs
- Writes JSON + CSV to /tmp

Usage
  python3 scripts/v6_limitless_hourly_24h_sim.py --hours 24

"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import math
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd
import yfinance as yf


@dataclass
class Run:
    ts_utc: pd.Timestamp
    hour_utc: pd.Timestamp
    direction: str  # LONG/SHORT
    agreement: str
    position_size: float
    omega_conf: float
    veto: bool
    entry_price: float | None
    path: str


def parse_ts(ts: str) -> pd.Timestamp:
    dt = datetime.fromisoformat(ts)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return pd.Timestamp(dt.astimezone(timezone.utc))


def safe_float(x: Any, default: float = 0.0) -> float:
    try:
        if x is None:
            return default
        return float(x)
    except Exception:
        return default


def load_runs(results_glob: str) -> list[Run]:
    runs: list[Run] = []
    for path in sorted(glob.glob(results_glob)):
        try:
            d = json.load(open(path, "r", encoding="utf-8"))
        except Exception:
            continue

        ts = parse_ts(d.get("timestamp", ""))
        hour = ts.floor("h")

        v6 = d.get("v6_enhanced") or {}
        direction = v6.get("final_direction")
        agreement = v6.get("agreement") or "?"
        pos = safe_float(v6.get("position_size"), 0.0)
        if direction not in ("LONG", "SHORT"):
            continue
        if pos <= 0:
            continue

        omega = d.get("omega_verdict") or {}
        omega_conf = safe_float(omega.get("confidence"), 0.0)
        veto = bool(omega.get("veto_applied", False))

        entry_price = (d.get("market_snapshot") or {}).get("last_price")
        entry_price = safe_float(entry_price, math.nan)
        if math.isnan(entry_price):
            entry_price = None

        runs.append(
            Run(
                ts_utc=ts,
                hour_utc=hour,
                direction=direction,
                agreement=agreement,
                position_size=pos,
                omega_conf=omega_conf,
                veto=veto,
                entry_price=entry_price,
                path=path,
            )
        )

    return runs


def fetch_hourly_prices(start_utc: pd.Timestamp, end_utc: pd.Timestamp) -> pd.DataFrame:
    start_date = (start_utc - pd.Timedelta(days=2)).date().isoformat()
    end_date = (end_utc + pd.Timedelta(days=2)).date().isoformat()
    df = yf.download("BTC-USD", start=start_date, end=end_date, interval="1h", progress=False)
    if df.empty:
        raise RuntimeError("yfinance hourly series empty")

    if isinstance(df.columns, pd.MultiIndex):
        # normalize
        df = pd.DataFrame(
            {
                "Open": df[("Open", "BTC-USD")],
                "Close": df[("Close", "BTC-USD")],
            }
        )
    else:
        df = df[["Open", "Close"]].copy()

    if df.index.tz is None:
        df.index = df.index.tz_localize("UTC")
    else:
        df.index = df.index.tz_convert("UTC")

    return df


def decision_strength(r: Run) -> float:
    score = r.omega_conf * max(r.position_size, 0.0)
    if r.veto:
        score *= 0.05
    return score


def pick_run_for_hour(runs: list[Run]) -> Run | None:
    if not runs:
        return None
    return max(runs, key=decision_strength)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallet", type=float, default=7.0)
    ap.add_argument("--fee-total", type=float, default=0.002)
    ap.add_argument("--hours", type=int, default=24)

    ap.add_argument("--min-omega-conf", type=float, default=0.58)
    ap.add_argument("--require-no-veto", action="store_true", default=True)
    ap.add_argument("--allowed-agreement", default="STRONG,WEAK")
    ap.add_argument(
        "--results-glob",
        default=str(Path.home() / ".openclaw/workspace/the-alpha-oracle/results/v6_*BTC-USD.json"),
    )

    args = ap.parse_args()

    runs = load_runs(args.results_glob)
    if not runs:
        raise SystemExit("no V6 runs found")

    runs = sorted(runs, key=lambda r: r.ts_utc)
    end_ts = runs[-1].hour_utc
    start_ts = end_ts - pd.Timedelta(hours=args.hours)

    # filter to window
    window = [r for r in runs if (r.hour_utc >= start_ts and r.hour_utc <= end_ts)]
    if not window:
        raise SystemExit("no runs in window")

    prices = fetch_hourly_prices(start_ts, end_ts + pd.Timedelta(hours=2))

    allowed_agreements = {x.strip() for x in args.allowed_agreement.split(",") if x.strip()}

    # group by hour
    by_hour: dict[pd.Timestamp, list[Run]] = {}
    for r in window:
        by_hour.setdefault(r.hour_utc, []).append(r)

    wallet = args.wallet
    rows = []

    for hour in pd.date_range(start_ts, end_ts - pd.Timedelta(hours=1), freq="h", tz="UTC"):
        hour = pd.Timestamp(hour)
        hour_runs = by_hour.get(hour, [])
        pick = pick_run_for_hour(hour_runs)

        # default skip
        action = "SKIP"
        bet = 0.0
        correct = None
        pnl = 0.0

        # outcome prices
        if hour not in prices.index or (hour + pd.Timedelta(hours=1)) not in prices.index:
            # missing price candle
            rows.append(
                {
                    "hour_utc": str(hour),
                    "action": "NO_PRICE",
                    "direction": None,
                    "bet": 0.0,
                    "wallet_before": wallet,
                    "pnl": 0.0,
                    "wallet_after": wallet,
                    "omega_conf": None,
                    "position_size": None,
                    "agreement": None,
                    "veto": None,
                }
            )
            continue

        open_p = float(prices.loc[hour, "Open"])
        close_p = float(prices.loc[hour + pd.Timedelta(hours=1), "Open"])  # next hour open as settlement anchor

        up = close_p > open_p

        if pick is not None:
            passes = True
            if pick.agreement not in allowed_agreements:
                passes = False
            if pick.omega_conf < args.min_omega_conf:
                passes = False
            if args.require_no_veto and pick.veto:
                passes = False

            if passes and wallet > 0:
                action = "BET"
                bet = min(wallet, wallet * max(0.0, min(1.0, pick.position_size)))
                # Map LONG->YES(up), SHORT->NO(down)
                predict_up = pick.direction == "LONG"
                correct = (predict_up and up) or ((not predict_up) and (not up))

                if correct:
                    pnl = bet * (1.0 - args.fee_total)
                else:
                    pnl = -bet * (1.0 + args.fee_total)

                wallet2 = wallet + pnl
            else:
                wallet2 = wallet

            rows.append(
                {
                    "hour_utc": str(hour),
                    "action": action,
                    "direction": pick.direction,
                    "bet": bet,
                    "wallet_before": wallet,
                    "pnl": pnl,
                    "wallet_after": wallet2,
                    "omega_conf": pick.omega_conf,
                    "position_size": pick.position_size,
                    "agreement": pick.agreement,
                    "veto": pick.veto,
                    "open": open_p,
                    "settle": close_p,
                    "up": up,
                    "correct": correct,
                    "run_path": pick.path,
                }
            )

            wallet = wallet2
        else:
            rows.append(
                {
                    "hour_utc": str(hour),
                    "action": "NO_SIGNAL",
                    "direction": None,
                    "bet": 0.0,
                    "wallet_before": wallet,
                    "pnl": 0.0,
                    "wallet_after": wallet,
                    "omega_conf": None,
                    "position_size": None,
                    "agreement": None,
                    "veto": None,
                    "open": open_p,
                    "settle": close_p,
                    "up": up,
                    "correct": None,
                    "run_path": None,
                }
            )

    # summarize
    bets = [r for r in rows if r.get("action") == "BET"]
    wins = [r for r in bets if r.get("correct") is True]

    summary = {
        "meta": {
            "window_hours": args.hours,
            "wallet_start": args.wallet,
            "wallet_end": wallet,
            "roi": (wallet / args.wallet - 1.0) if args.wallet else None,
            "fee_total": args.fee_total,
            "min_omega_conf": args.min_omega_conf,
            "allowed_agreement": sorted(list(allowed_agreements)),
            "require_no_veto": args.require_no_veto,
            "note": "Settlement uses next-hour OPEN; payout is even-odds simplified.",
        },
        "stats": {
            "bets": len(bets),
            "wins": len(wins),
            "win_rate": (len(wins) / len(bets)) if bets else None,
        },
        "rows": rows,
    }

    outdir = Path(f"/tmp/v6_limitless_hourly_24h_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    with (outdir / "hourly.csv").open("w", newline="", encoding="utf-8") as f:
        fieldnames = list(rows[0].keys())
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"OK: wrote {outdir}")
    print(f"wallet_start={args.wallet:.2f} wallet_end={wallet:.4f} ROI={summary['meta']['roi']*100:.3f}%")
    print(f"bets={len(bets)} win_rate={(summary['stats']['win_rate']*100 if summary['stats']['win_rate'] is not None else None)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
