#!/usr/bin/env python3
"""Run SAVE NOW + (optional) upload newest snapshot to GitHub.

This is a thin wrapper around workspace scripts.

- Required: scripts/save_now.sh
- Optional: scripts/state_snapshot_upload_github.sh

Usage:
  python3 skills/private/aoi-backup-guardian/scripts/save_now_plus.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path

WS = Path.home() / ".openclaw" / "workspace"


def run(cmd: list[str]) -> int:
    print("RUN:", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> int:
    save_now = WS / "scripts" / "save_now.sh"
    if not save_now.exists():
        print(f"ERROR: missing {save_now}")
        return 2

    rc = run([str(save_now)])
    if rc != 0:
        print(f"ERROR: save_now failed rc={rc}")
        return rc

    uploader = WS / "scripts" / "state_snapshot_upload_github.sh"
    if uploader.exists():
        rc2 = run([str(uploader)])
        if rc2 != 0:
            print(f"WARN: snapshot upload failed rc={rc2}")
            # best-effort

    print("STATUS: done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
