# PixelOffice local control plane (MVP)

This is a minimal SwarmWatch-style local-first event bus to power PixelOffice overlay prototypes.

## What you get
- HTTP ingest: `POST /event`
- HTTP state: `GET /state`
- WebSocket broadcast: `ws://127.0.0.1:4100`
- Watcher that emits events from:
  - `context/handoff/HF_*.md`
  - `logs/launchd_*.out.log` (tick detection)

## Install
```bash
cd ~/.openclaw/workspace
npm i ws
```

## Run
Terminal A:
```bash
node scripts/pixeloffice/control_plane.mjs
```

Terminal B:
```bash
node scripts/pixeloffice/watch_emit.mjs
```

## Quick test
```bash
curl -sS http://127.0.0.1:4100/health
curl -sS http://127.0.0.1:4100/state | jq 'keys'
```
