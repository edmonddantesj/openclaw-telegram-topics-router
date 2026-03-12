#!/usr/bin/env python3
"""Mock router -> orchestrator dispatch for internal alpha testing.

Purpose:
- prove topic-aware dispatch from a Telegram topic into a local runtime artifact
- keep everything local/file-based for alpha verification
- no Telegram API writes

Usage:
  python3 openclaw-telegram-topics-router/scripts/mock_orchestrator_dispatch.py \
    --chat-id telegram:-1003732040608 \
    --thread-id 6062 \
    --message "이곳에서 테스트해볼 수 있도록 진행시켜"
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


def _find_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "context" / "telegram_topics").exists():
            return parent
    return here.parents[4]


ROOT = _find_root()
TOPICS_DIR = ROOT / "context" / "telegram_topics"
RUNTIME_DIR = TOPICS_DIR / "runtime" / "orchestrator_alpha_lab"
THREAD_TOPIC_MAP = TOPICS_DIR / "thread_topic_map.json"
THREAD_AGENT_MAP = TOPICS_DIR / "thread_agent_map.json"
SKILL_DIR = ROOT / "repos" / "aoi-skills" / "skills" / "aoi-squad-orchestrator-lite"
SKILL_JS = SKILL_DIR / "skill.js"


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _slug_for_thread(thread_id: int) -> str | None:
    data = _load(THREAD_TOPIC_MAP)
    for slug, mapped in data.items():
        if str(mapped) == str(thread_id):
            return slug
    return None


def _agent_entry(slug: str) -> dict:
    data = _load(THREAD_AGENT_MAP)
    entry = data.get(slug)
    if not isinstance(entry, dict):
        return {}
    return entry


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chat-id", required=True)
    ap.add_argument("--thread-id", required=True, type=int)
    ap.add_argument("--message", required=True)
    ap.add_argument("--preset", default="planner-builder-reviewer")
    args = ap.parse_args()

    slug = _slug_for_thread(args.thread_id)
    if not slug:
        print(json.dumps({"ok": False, "error": "THREAD_NOT_MAPPED", "thread_id": args.thread_id}, ensure_ascii=False))
        return 1

    agent = _agent_entry(slug)
    primary = agent.get("primary")
    collaborators = agent.get("collaborators", [])

    run_ts = int(time.time())
    created_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(run_ts))
    thread_dir = RUNTIME_DIR / f"thread_{args.thread_id}"
    latest_dir = thread_dir / "latest"
    runs_dir = thread_dir / "runs"
    run_key = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime(run_ts))
    run_dir = runs_dir / run_key

    run_dir.mkdir(parents=True, exist_ok=True)
    latest_dir.mkdir(parents=True, exist_ok=True)

    dispatch_record = {
        "schema": "openclaw.telegram.orchestrator_alpha_dispatch.v0_1",
        "chat_id": args.chat_id,
        "thread_id": args.thread_id,
        "slug": slug,
        "primary": primary,
        "collaborators": collaborators,
        "preset": args.preset,
        "message": args.message,
        "created_at": created_at,
        "run_key": run_key,
    }
    dispatch_json = json.dumps(dispatch_record, indent=2, ensure_ascii=False) + "\n"
    (run_dir / "dispatch.json").write_text(dispatch_json, encoding="utf-8")
    (latest_dir / "dispatch.json").write_text(dispatch_json, encoding="utf-8")

    cmd = [
        "node",
        str(SKILL_JS),
        "run",
        "--preset",
        args.preset,
        "--task",
        args.message,
    ]
    proc = subprocess.run(cmd, cwd=str(SKILL_DIR), capture_output=True, text=True)

    (run_dir / "stdout.json").write_text(proc.stdout, encoding="utf-8")
    (run_dir / "stderr.log").write_text(proc.stderr or "", encoding="utf-8")
    (latest_dir / "stdout.json").write_text(proc.stdout, encoding="utf-8")
    (latest_dir / "stderr.log").write_text(proc.stderr or "", encoding="utf-8")

    out = {
        "ok": proc.returncode == 0,
        "thread_id": args.thread_id,
        "slug": slug,
        "primary": primary,
        "collaborators": collaborators,
        "run_key": run_key,
        "thread_dir": str(thread_dir),
        "dispatch_path": str(run_dir / "dispatch.json"),
        "stdout_path": str(run_dir / "stdout.json"),
        "stderr_path": str(run_dir / "stderr.log"),
        "latest_dispatch_path": str(latest_dir / "dispatch.json"),
        "latest_stdout_path": str(latest_dir / "stdout.json"),
        "latest_stderr_path": str(latest_dir / "stderr.log"),
        "returncode": proc.returncode,
    }
    print(json.dumps(out, ensure_ascii=False))
    return 0 if proc.returncode == 0 else proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
