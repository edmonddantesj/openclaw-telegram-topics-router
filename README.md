# OpenClaw Telegram Topics Router

One-click-ish setup for splitting a Telegram **Forum** group into topics (threads) and maintaining a `thread_id → topic_slug` routing map for OpenClaw.

## What you get
- A portable OpenClaw skill folder: `openclaw-telegram-topics-router/`
- Scripts to initialize SSOT and update mappings

## Install (as a skill)
Copy the skill folder into your workspace:

```bash
mkdir -p skills/public
cp -R openclaw-telegram-topics-router skills/public/
```

(Or package it into a `.skill` with your own tooling.)

## Quick start
```bash
python3 skills/public/openclaw-telegram-topics-router/scripts/init_topics_ssot.py
python3 skills/public/openclaw-telegram-topics-router/scripts/add_mapping.py --slug ops --thread-id 38
python3 skills/public/openclaw-telegram-topics-router/scripts/audit_map.py
```

## Notes
- Creating Telegram topics is typically done in the Telegram UI.
- Calibration: send a ping message inside each topic/thread, then record its `message_thread_id`.

## License
MIT
