#!/usr/bin/env python3
"""Resolve primary agent for a Telegram thread_id using SSOT.

Reads:
- context/telegram_topics/thread_agent_map.json

Example:
  python3 .../resolve_primary_agent.py --thread-id 38

Output:
  {"ok":true,"thread_id":38,"primary":"Blue-Gear","collaborators":[...]}
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _find_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "context" / "telegram_topics").exists():
            return parent
    return here.parents[4]


ROOT = _find_root()
CTX_DIR = ROOT / "context" / "telegram_topics"
MAP_PATH = CTX_DIR / "thread_agent_map.json"
TOPIC_MAP_PATH = CTX_DIR / "thread_topic_map.json"


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_entry(thread_id: int) -> dict | None:
    data = _load_json(MAP_PATH)

    # v0.1 thread-based schema
    threads = data.get("threads")
    if isinstance(threads, dict):
        return threads.get(str(thread_id))

    # slug-based legacy schema + thread_topic_map.json
    if not TOPIC_MAP_PATH.exists():
        return None

    topic_map = _load_json(TOPIC_MAP_PATH)
    slug = None
    for k, v in topic_map.items():
        if str(v) == str(thread_id):
            slug = k
            break

    if not slug:
        return None

    entry = data.get(slug)
    if isinstance(entry, dict):
        return entry

    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--thread-id", required=True, type=int)
    args = ap.parse_args()

    if not MAP_PATH.exists():
        raise SystemExit(f"Missing SSOT: {MAP_PATH}")

    entry = _resolve_entry(args.thread_id)

    if not entry:
        print(json.dumps({"ok": False, "error": "NOT_FOUND", "thread_id": args.thread_id}, ensure_ascii=False))
        return 0

    out = {
        "ok": True,
        "thread_id": args.thread_id,
        "primary": entry.get("primary"),
        "collaborators": entry.get("collaborators", []),
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
