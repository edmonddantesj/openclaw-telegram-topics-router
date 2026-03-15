#!/usr/bin/env python3
"""V6 × Limitless Hourly Backtest using REAL odds snapshots (shadow logs) — v0.1

What this fixes
- Uses Limitless odds (prices) instead of even-odds.
- Computes PnL based on market price p:
  - Spend S to buy YES at price p => shares=S/p
    - if outcome YES: profit = S*(1/p - 1)
    - if outcome NO:  profit = -S
  - Similarly for NO using price q.

Inputs
- V6 runs: `the-alpha-oracle/results/v6_*BTC-USD.json`
- Odds snapshots (JSONL): `/tmp/limitless_odds_btc_hourly.jsonl`
- Settlements (JSONL): `/tmp/limitless_settle_btc_hourly.jsonl`

Hourly market mapping
- We assume you can bet at hour start (UTC or KST converted to UTC internally).
- For each hour H (start), we pick the market whose `deadline_utc == H+1h`.
- We pick the odds snapshot closest to hour start (within a tolerance window).

Outputs
- /tmp/v6_limitless_odds_backtest_<timestamp>/summary.json + hourly.csv

Safety
- Report-only. No wallet actions.

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


V6_GLOB_DEFAULT = str(Path.home() / ".openclaw/workspace/the-alpha-oracle/results/v6_*BTC-USD.json")
ODDS_JSONL_DEFAULT = "/tmp/limitless_odds_btc_hourly.jsonl"
SETTLE_JSONL_DEFAULT = "/tmp/limitless_settle_btc_hourly.jsonl"


@dataclass
class V6Run:
    ts_utc: pd.Timestamp
    hour_utc: pd.Timestamp
    direction: str  # LONG/SHORT
    agreement: str
    position_size: float
    omega_conf: float
    veto: bool
    path: str


@dataclass
class Market:
    slug: str
    deadline_utc: pd.Timestamp
    outcome: str  # YES/NO


@dataclass
class Odds:
    slug: str
    captured_at_utc: pd.Timestamp
    yes_price: float
    no_price: float


def parse_ts_iso(s: str) -> pd.Timestamp:
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
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


def load_v6_runs(glob_pat: str) -> list[V6Run]:
    runs: list[V6Run] = []
    for path in sorted(glob.glob(glob_pat)):
        try:
            d = json.load(open(path, "r", encoding="utf-8"))
        except Exception:
            continue
        ts = pd.Timestamp(datetime.fromisoformat(d.get("timestamp")).astimezone(timezone.utc))
        hour = ts.floor("h")

        v6 = d.get("v6_enhanced") or {}
        direction = v6.get("final_direction")
        if direction not in ("LONG", "SHORT"):
            continue
        pos = safe_float(v6.get("position_size"), 0.0)
        if pos <= 0:
            continue
        agreement = v6.get("agreement") or "?"

        omega = d.get("omega_verdict") or {}
        omega_conf = safe_float(omega.get("confidence"), 0.0)
        veto = bool(omega.get("veto_applied", False))

        runs.append(
            V6Run(
                ts_utc=ts,
                hour_utc=hour,
                direction=direction,
                agreement=agreement,
                position_size=pos,
                omega_conf=omega_conf,
                veto=veto,
                path=path,
            )
        )
    return runs


def load_settlements(path: str) -> dict[pd.Timestamp, Market]:
    """Map deadline_utc -> Market"""
    out: dict[pd.Timestamp, Market] = {}
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        d = json.loads(line)
        dl = parse_ts_iso(d["deadline_utc"])
        out[dl] = Market(slug=d["slug"], deadline_utc=dl, outcome=d["outcome"].upper())
    return out


def load_odds(path: str) -> dict[str, list[Odds]]:
    out: dict[str, list[Odds]] = {}
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
        if not line.strip():
            continue
        d = json.loads(line)
        cap = parse_ts_iso(d["captured_at_utc"])
        market = d.get("market") or {}
        slug = market.get("slug")
        prices = market.get("prices") or []
        if not slug or len(prices) < 2:
            continue
        yes_p = safe_float(prices[0], math.nan)
        no_p = safe_float(prices[1], math.nan)
        if math.isnan(yes_p) or math.isnan(no_p):
            continue
        out.setdefault(slug, []).append(Odds(slug=slug, captured_at_utc=cap, yes_price=yes_p, no_price=no_p))

    # sort by time
    for slug in list(out.keys()):
        out[slug] = sorted(out[slug], key=lambda o: o.captured_at_utc)
    return out


def decision_strength(r: V6Run) -> float:
    score = r.omega_conf * max(r.position_size, 0.0)
    if r.veto:
        score *= 0.05
    return score


def pick_best_run(runs: list[V6Run]) -> V6Run | None:
    if not runs:
        return None
    return max(runs, key=decision_strength)


def pick_odds_near(odds_list: list[Odds], target: pd.Timestamp, tol_min: int) -> Odds | None:
    # find closest captured_at to target
    best = None
    best_dt = None
    for o in odds_list:
        dt = abs((o.captured_at_utc - target).total_seconds())
        if best is None or dt < best_dt:
            best = o
            best_dt = dt
    if best is None:
        return None
    if best_dt is not None and best_dt > tol_min * 60:
        return None
    return best


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


def profit_shares_spend(spend: float, price: float, won: bool) -> float:
    """Prediction-market style PnL with shares.

    Spend S at price p => shares=S/p.
    If win: profit=S*(1/p - 1)
    If lose: profit=-S

    Note: fees/slippage should be reflected by using an *effective* price.
    """
    if spend <= 0:
        return 0.0
    if not won:
        return -spend
    price = clamp(price, 1e-6, 1 - 1e-6)
    return spend * (1.0 / price - 1.0)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallet", type=float, default=7.0)
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--min-omega-conf", type=float, default=0.58)
    ap.add_argument("--allowed-agreement", default="STRONG,WEAK")
    ap.add_argument("--require-no-veto", action="store_true", default=True)
    ap.add_argument("--odds-tolerance-min", type=int, default=15)

    # realism knobs
    ap.add_argument("--p-floor", type=float, default=0.05, help="skip bets when chosen side price < p-floor")
    ap.add_argument("--slippage-bps", type=float, default=100.0, help="adverse price move in bps applied to entry price")
    ap.add_argument("--max-bet-usd", type=float, default=1.0, help="hard cap per-hour spend")

    ap.add_argument("--v6-glob", default=V6_GLOB_DEFAULT)
    ap.add_argument("--odds-jsonl", default=ODDS_JSONL_DEFAULT)
    ap.add_argument("--settle-jsonl", default=SETTLE_JSONL_DEFAULT)

    args = ap.parse_args()

    v6 = load_v6_runs(args.v6_glob)
    if not v6:
        raise SystemExit("no v6 runs")

    settlements = load_settlements(args.settle_jsonl)
    odds = load_odds(args.odds_jsonl)

    # window based on latest settlement deadline
    latest_deadline = max(settlements.keys())
    end_hour = (latest_deadline - pd.Timedelta(hours=1)).floor("h")
    start_hour = end_hour - pd.Timedelta(hours=args.hours)

    allowed_agreements = {x.strip() for x in args.allowed_agreement.split(",") if x.strip()}

    # group v6 by hour
    by_hour: dict[pd.Timestamp, list[V6Run]] = {}
    for r in v6:
        if r.hour_utc < start_hour or r.hour_utc > end_hour:
            continue
        by_hour.setdefault(r.hour_utc, []).append(r)

    wallet = args.wallet
    rows = []

    for hour in pd.date_range(start_hour, end_hour, freq="h", tz="UTC"):
        hour = pd.Timestamp(hour)
        deadline = hour + pd.Timedelta(hours=1)
        mkt = settlements.get(deadline)
        if not mkt:
            rows.append({"hour_utc": str(hour), "action": "NO_MARKET", "wallet_before": wallet, "wallet_after": wallet})
            continue

        # odds snapshot near hour start
        olist = odds.get(mkt.slug, [])
        o = pick_odds_near(olist, hour, args.odds_tolerance_min)
        if not o:
            rows.append({"hour_utc": str(hour), "action": "NO_ODDS", "slug": mkt.slug, "wallet_before": wallet, "wallet_after": wallet})
            continue

        # pick v6 run
        pick = pick_best_run(by_hour.get(hour, []))
        if not pick:
            rows.append({"hour_utc": str(hour), "action": "NO_SIGNAL", "slug": mkt.slug, "wallet_before": wallet, "wallet_after": wallet})
            continue

        # filters
        passes = True
        if pick.agreement not in allowed_agreements:
            passes = False
        if pick.omega_conf < args.min_omega_conf:
            passes = False
        if args.require_no_veto and pick.veto:
            passes = False

        if not passes:
            rows.append({
                "hour_utc": str(hour),
                "action": "SKIP_FILTER",
                "slug": mkt.slug,
                "wallet_before": wallet,
                "wallet_after": wallet,
                "omega_conf": pick.omega_conf,
                "pos": pick.position_size,
                "agreement": pick.agreement,
                "veto": pick.veto,
            })
            continue

        spend = min(wallet, wallet * max(0.0, min(1.0, pick.position_size)))
        spend = min(spend, args.max_bet_usd)
        if spend <= 0:
            rows.append({"hour_utc": str(hour), "action": "SKIP_ZERO", "wallet_before": wallet, "wallet_after": wallet})
            continue

        # map LONG->YES, SHORT->NO
        side = "YES" if pick.direction == "LONG" else "NO"
        raw_price = o.yes_price if side == "YES" else o.no_price

        # Liquidity/slippage proxy: avoid extreme low-p tails (often low liquidity) and apply adverse entry slippage.
        if raw_price < args.p_floor:
            rows.append({
                "hour_utc": str(hour),
                "action": "SKIP_P_FLOOR",
                "slug": mkt.slug,
                "side": side,
                "raw_price": raw_price,
                "p_floor": args.p_floor,
                "wallet_before": wallet,
                "wallet_after": wallet,
            })
            continue

        slip = args.slippage_bps / 10000.0
        eff_price = clamp(raw_price + slip, 1e-6, 1 - 1e-6)

        won = (mkt.outcome == side)
        pnl = profit_shares_spend(spend, eff_price, won)
        wallet2 = wallet + pnl

        rows.append({
            "hour_utc": str(hour),
            "action": "BET",
            "slug": mkt.slug,
            "side": side,
            "odds_yes": o.yes_price,
            "odds_no": o.no_price,
            "raw_price": raw_price,
            "eff_price": eff_price,
            "p_floor": args.p_floor,
            "slippage_bps": args.slippage_bps,
            "max_bet_usd": args.max_bet_usd,
            "outcome": mkt.outcome,
            "won": won,
            "spend": spend,
            "pnl_usd": pnl,
            "wallet_before": wallet,
            "wallet_after": wallet2,
            "omega_conf": pick.omega_conf,
            "pos": pick.position_size,
            "agreement": pick.agreement,
            "veto": pick.veto,
            "v6_path": pick.path,
            "odds_captured_at_utc": str(o.captured_at_utc),
        })

        wallet = wallet2

    bets = [r for r in rows if r.get("action") == "BET"]
    wins = [r for r in bets if r.get("won") is True]

    summary = {
        "meta": {
            "wallet_start": args.wallet,
            "wallet_end": wallet,
            "roi": wallet / args.wallet - 1.0,
            "window_hours": args.hours,
            "hour_start_utc": str(start_hour),
            "hour_end_utc": str(end_hour),
            "min_omega_conf": args.min_omega_conf,
            "allowed_agreement": sorted(list(allowed_agreements)),
            "require_no_veto": args.require_no_veto,
            "odds_tolerance_min": args.odds_tolerance_min,
            "p_floor": args.p_floor,
            "slippage_bps": args.slippage_bps,
            "max_bet_usd": args.max_bet_usd,
            "note": "PnL uses real Limitless prices (odds snapshots). Adds p-floor + adverse slippage proxy + max bet cap. Still a simplified model (no orderbook depth simulation).", 
        },
        "stats": {
            "bets": len(bets),
            "wins": len(wins),
            "win_rate": (len(wins) / len(bets)) if bets else None,
            "sum_pnl": sum(r.get("pnl_usd", 0.0) for r in bets),
        },
        "rows": rows,
    }

    outdir = Path(f"/tmp/v6_limitless_odds_backtest_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    with (outdir / "hourly.csv").open("w", newline="", encoding="utf-8") as f:
        fieldnames = sorted({k for r in rows for k in r.keys()})
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"OK: wrote {outdir}")
    print(f"wallet_start={args.wallet:.2f} wallet_end={wallet:.4f} ROI={summary['meta']['roi']*100:.3f}%")
    print(f"bets={summary['stats']['bets']} win_rate={(summary['stats']['win_rate']*100 if summary['stats']['win_rate'] is not None else None)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
