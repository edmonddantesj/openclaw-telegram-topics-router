#!/usr/bin/env python3
"""Two-step confirmation gate for destructive commands.

Goal: prevent accidental deletion of OpenClaw state (e.g. ~/.openclaw, workspace, repos).

This script DOES NOT execute commands. It only classifies and returns a gate decision.

Outputs one of:
- OK_TO_RUN
- NEEDS_CONFIRMATION
- BLOCKED

Usage:
  python3 .../guard_destructive_cmd.py --cmd "rm -rf ~/.openclaw"
  python3 .../guard_destructive_cmd.py --cmd "rm -rf ~/.openclaw" --confirm "I UNDERSTAND THIS WILL DELETE OPENCLAW STATE"
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass

REQUIRED_PHRASE = "I UNDERSTAND THIS WILL DELETE OPENCLAW STATE"


@dataclass
class Decision:
    status: str
    reason: str


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip())


def is_dangerous(cmd: str) -> bool:
    c = cmd.lower()

    # obvious removals
    if re.search(r"\brm\b", c) and (" -rf" in c or " -fr" in c or " -r" in c):
        # target patterns
        targets = [
            "~/.openclaw",
            "$home/.openclaw",
            "/.openclaw",
            ".openclaw/workspace",
            "openclaw/workspace",
            "~/library/application support/openclaw",
        ]
        if any(t in c for t in targets):
            return True

        # broad wipe patterns
        if re.search(r"rm\s+(-rf|-fr|-r)\s+(/users/|/home/|~)\S*\.openclaw", c):
            return True

    # dangerous recursive delete via find
    if "find " in c and "-delete" in c and ".openclaw" in c:
        return True

    # disk wipes (overkill, but safe)
    if "diskutil erase" in c or "mkfs" in c:
        return True

    return False


def decide(cmd: str, confirm: str | None) -> Decision:
    if not cmd.strip():
        return Decision("BLOCKED", "empty_cmd")

    if is_dangerous(cmd):
        if confirm and norm(confirm) == REQUIRED_PHRASE:
            return Decision("OK_TO_RUN", "confirmed_destructive")
        return Decision("NEEDS_CONFIRMATION", "destructive_cmd")

    return Decision("OK_TO_RUN", "not_destructive")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cmd", required=True)
    ap.add_argument("--confirm", default=None)
    args = ap.parse_args()

    d = decide(args.cmd, args.confirm)
    print(d.status)
    print(f"REASON: {d.reason}")

    if d.status == "NEEDS_CONFIRMATION":
        print("CONFIRM_PHRASE:")
        print(REQUIRED_PHRASE)

    # exit code is not a control signal; keep 0 to simplify pipelines
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
