#!/usr/bin/env bash
set -euo pipefail

# Install & bootstrap launchd job for x-post tick.
# Safe: creates/overwrites ONLY the target plist in ~/Library/LaunchAgents.

SRC="/Users/silkroadcat/.openclaw/workspace/context/automation/launchd/com.aoineco.xpost.tick.plist"
DST="$HOME/Library/LaunchAgents/com.aoineco.xpost.tick.plist"

mkdir -p "$HOME/Library/LaunchAgents" 
mkdir -p /Users/silkroadcat/.openclaw/workspace/logs/launchd

cp "$SRC" "$DST"

UID_NUM=$(id -u)
DOMAIN="gui/${UID_NUM}"

# If already loaded, bootout first to ensure the new plist is applied.
launchctl bootout "$DOMAIN" "$DST" >/dev/null 2>&1 || true
launchctl bootstrap "$DOMAIN" "$DST"
launchctl enable "$DOMAIN/com.aoineco.xpost.tick" >/dev/null 2>&1 || true

# Optional: run once immediately (non-blocking best-effort)
launchctl kickstart -k "$DOMAIN/com.aoineco.xpost.tick" >/dev/null 2>&1 || true

echo "OK: installed+bootstrapped com.aoineco.xpost.tick"
launchctl print "$DOMAIN/com.aoineco.xpost.tick" | head -n 40 || true
