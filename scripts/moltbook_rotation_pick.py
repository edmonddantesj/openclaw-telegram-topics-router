#!/usr/bin/env python3
"""Pick daily Writer/Reviewers for Moltbook with weekly non-overlap.

- Random pick from member pool
- Constraint: same person shouldn't be assigned twice in the same ISO week
- Output JSON to stdout

State file (SSOT):
  context/state/moltbook_rotation.state.json

NOTE: members list must be filled with stable identifiers (e.g., telegram @handle or canonical team id).
"""

from __future__ import annotations

import datetime as dt
import json
import random
from pathlib import Path

STATE_PATH = Path("/Users/silkroadcat/.openclaw/workspace/context/state/moltbook_rotation.state.json")


def iso_week_key(now_kst: dt.datetime) -> str:
    y, w, _ = now_kst.isocalendar()
    return f"{y}-W{w:02d}"


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"version": "0.1", "weekStart": "Mon", "members": [], "history": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=9)))
    today = now.strftime("%Y-%m-%d")
    week = iso_week_key(now)

    state = load_state()
    members: list[str] = state.get("members") or []
    if len(members) < 3:
        raise SystemExit("moltbook_rotation.state.json: members must have >=3 entries")

    hist = state.setdefault("history", {})
    week_hist = hist.setdefault(week, {"assignments": []})
    used = set()
    for a in week_hist.get("assignments", []):
        used.update([a.get("writer"), *a.get("reviewers", [])])

    available = [m for m in members if m not in used]
    if len(available) < 3:
        # reset weekly used if pool exhausted (still deterministic rule, but avoids deadlock)
        used = set()
        available = list(members)

    random.shuffle(available)
    writer = available[0]
    reviewers = available[1:3]

    assignment = {"date": today, "writer": writer, "reviewers": reviewers}
    week_hist.setdefault("assignments", []).append(assignment)
    save_state(state)

    print(json.dumps({"week": week, **assignment}, ensure_ascii=False))


if __name__ == "__main__":
    main()
