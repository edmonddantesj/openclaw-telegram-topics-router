#!/usr/bin/env python3
"""V6 Backtest (24h) — Best Entry per Day (v0.1)

Purpose
- Simulate a $7 wallet that only places a single bet per day at a chosen run time.
- Evaluate 24h forward return.

Important
- This is a *simulation* (report-only). It does not place real trades.
- Two selection modes are produced:
  1) signal_best: choose the run with the highest *decision strength* using only info available at decision time.
  2) hindsight_best: choose the run that would have maximized realized 24h PnL (upper bound / lookahead).

Data sources
- V6 archives: `the-alpha-oracle/results/v6_*BTC-USD.json`
- Price series: yfinance `BTC-USD` (5m interval)

Outputs
- JSON + CSV summaries under /tmp

Assumptions
- Bet amount: min($7, $7 * position_size). If position_size=0 => no bet.
- Direction: LONG/SHORT from v6_enhanced.final_direction
- Fees: default 0.10% per side (entry+exit) = 0.20% total

Usage
  python3 scripts/v6_backtest_24h_best_entry.py --days 7

"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import math
import os
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

import pandas as pd
import yfinance as yf


@dataclass
class Run:
    ts_utc: pd.Timestamp
    day_utc: str
    direction: str
    position_size: float
    omega_conf: float
    omega_veto: bool
    var95: float
    entry_price: float
    path: str


def parse_ts(ts: str) -> pd.Timestamp:
    # timestamp includes offset
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
        day_utc = ts.strftime("%Y-%m-%d")

        v6 = d.get("v6_enhanced") or {}
        direction = v6.get("final_direction")
        pos = safe_float(v6.get("position_size"), 0.0)
        if direction not in ("LONG", "SHORT"):
            continue
        if pos <= 0:
            continue

        omega = d.get("omega_verdict") or {}
        omega_conf = safe_float(omega.get("confidence"), 0.0)
        omega_veto = bool(omega.get("veto_applied", False))

        var95 = safe_float(v6.get("var_95"), math.nan)
        entry_price = safe_float((d.get("market_snapshot") or {}).get("last_price"), math.nan)

        runs.append(
            Run(
                ts_utc=ts,
                day_utc=day_utc,
                direction=direction,
                position_size=pos,
                omega_conf=omega_conf,
                omega_veto=omega_veto,
                var95=var95,
                entry_price=entry_price,
                path=path,
            )
        )
    return runs


def fetch_prices(start_utc: pd.Timestamp, end_utc: pd.Timestamp) -> pd.Series:
    # yfinance uses date strings; fetch a bit wider
    start_date = (start_utc - pd.Timedelta(days=2)).date().isoformat()
    end_date = (end_utc + pd.Timedelta(days=2)).date().isoformat()
    df = yf.download("BTC-USD", start=start_date, end=end_date, interval="5m", progress=False)
    if df.empty:
        raise RuntimeError("yfinance returned empty price series")

    if isinstance(df.columns, pd.MultiIndex):
        close_s = df[("Close", "BTC-USD")]
    else:
        close_s = df["Close"]

    if close_s.index.tz is None:
        close_s.index = close_s.index.tz_localize("UTC")
    else:
        close_s.index = close_s.index.tz_convert("UTC")

    # trim
    close_s = close_s[(close_s.index >= start_utc - pd.Timedelta(hours=1)) & (close_s.index <= end_utc + pd.Timedelta(days=2))]
    return close_s


def price_at_or_after(prices: pd.Series, t: pd.Timestamp) -> float | None:
    idx = prices.index.values  # numpy datetime64
    vals = prices.to_numpy()
    key = t.to_datetime64()
    pos = idx.searchsorted(key)
    if pos >= len(idx):
        return None
    return float(vals[pos])


def decision_strength(r: Run) -> float:
    """Best-effort score using only decision-time info.

    Heuristic:
    - prefer higher omega confidence
    - prefer larger position_size
    - penalize veto and high VaR
    """
    score = r.omega_conf * max(r.position_size, 0.0)
    if r.omega_veto:
        score *= 0.1
    if not math.isnan(r.var95):
        # penalize very high var
        score *= max(0.0, 1.0 - max(0.0, r.var95) / 2.0)
    return score


def pnl_24h(r: Run, prices: pd.Series, wallet_usd: float, fee_per_side: float) -> tuple[float, float] | tuple[None, None]:
    entry = r.entry_price
    if math.isnan(entry):
        p = price_at_or_after(prices, r.ts_utc)
        if p is None:
            return (None, None)
        entry = p

    exit_t = r.ts_utc + pd.Timedelta(hours=24)
    exit_p = price_at_or_after(prices, exit_t)
    if exit_p is None:
        return (None, None)

    raw_ret = (exit_p - entry) / entry
    if r.direction == "SHORT":
        raw_ret = -raw_ret

    # fees: apply total fee on notional (entry+exit)
    total_fee = 2 * fee_per_side

    bet = min(wallet_usd, wallet_usd * r.position_size)
    pnl = bet * (raw_ret - total_fee)
    return (pnl, raw_ret)


def group_by_day(runs: Iterable[Run]) -> dict[str, list[Run]]:
    out: dict[str, list[Run]] = {}
    for r in runs:
        out.setdefault(r.day_utc, []).append(r)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallet", type=float, default=7.0)
    ap.add_argument("--fee-per-side", type=float, default=0.001)  # 0.10%
    ap.add_argument("--days", type=int, default=7, help="limit to last N days")
    ap.add_argument(
        "--results-glob",
        default=str(Path.home() / ".openclaw/workspace/the-alpha-oracle/results/v6_*BTC-USD.json"),
    )
    args = ap.parse_args()

    runs = load_runs(args.results_glob)
    if not runs:
        raise SystemExit("no runs found")

    runs = sorted(runs, key=lambda r: r.ts_utc)
    last_ts = runs[-1].ts_utc
    cutoff = last_ts - pd.Timedelta(days=args.days)
    runs = [r for r in runs if r.ts_utc >= cutoff]

    start_ts = min(r.ts_utc for r in runs)
    end_ts = max(r.ts_utc for r in runs)
    prices = fetch_prices(start_ts, end_ts)

    by_day = group_by_day(runs)

    rows = []
    for day, day_runs in sorted(by_day.items()):
        # signal_best
        signal_pick = max(day_runs, key=decision_strength)
        # hindsight_best
        best_pnl = None
        hindsight_pick = None
        for r in day_runs:
            pnl, raw_ret = pnl_24h(r, prices, args.wallet, args.fee_per_side)
            if pnl is None:
                continue
            if (best_pnl is None) or (pnl > best_pnl):
                best_pnl = pnl
                hindsight_pick = r

        # compute both
        sp_pnl, sp_ret = pnl_24h(signal_pick, prices, args.wallet, args.fee_per_side)
        hp_pnl, hp_ret = (None, None)
        if hindsight_pick is not None:
            hp_pnl, hp_ret = pnl_24h(hindsight_pick, prices, args.wallet, args.fee_per_side)

        rows.append(
            {
                "day_utc": day,
                "signal_pick_ts": str(signal_pick.ts_utc),
                "signal_pick_dir": signal_pick.direction,
                "signal_pick_pos": signal_pick.position_size,
                "signal_pick_omega_conf": signal_pick.omega_conf,
                "signal_pick_var95": signal_pick.var95,
                "signal_pick_pnl_usd": sp_pnl,
                "signal_pick_raw_ret": sp_ret,
                "hindsight_pick_ts": str(hindsight_pick.ts_utc) if hindsight_pick else None,
                "hindsight_pick_dir": hindsight_pick.direction if hindsight_pick else None,
                "hindsight_pick_pos": hindsight_pick.position_size if hindsight_pick else None,
                "hindsight_pick_pnl_usd": hp_pnl,
                "hindsight_pick_raw_ret": hp_ret,
            }
        )

    # aggregate
    def agg(key: str) -> dict[str, float]:
        vals = [r[key] for r in rows if isinstance(r[key], (int, float)) and r[key] is not None]
        if not vals:
            return {"n": 0}
        return {
            "n": len(vals),
            "sum_usd": float(sum(vals)),
            "avg_usd": float(sum(vals) / len(vals)),
            "win_rate": float(sum(1 for v in vals if v > 0) / len(vals)),
        }

    summary = {
        "meta": {
            "wallet_usd": args.wallet,
            "fee_per_side": args.fee_per_side,
            "days": args.days,
            "runs_used": len(runs),
            "days_count": len(rows),
            "cutoff_utc": str(cutoff),
            "last_ts_utc": str(last_ts),
            "note": "signal_pick uses decision-time heuristic; hindsight_pick is lookahead upper bound",
        },
        "signal_pick": agg("signal_pick_pnl_usd"),
        "hindsight_pick": agg("hindsight_pick_pnl_usd"),
        "rows": rows,
    }

    outdir = Path(f"/tmp/v6_backtest_24h_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    outdir.mkdir(parents=True, exist_ok=True)

    (outdir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    with (outdir / "daily.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print(f"OK: wrote {outdir}")
    print("signal_pick", summary["signal_pick"])
    print("hindsight_pick", summary["hindsight_pick"])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
