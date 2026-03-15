# Notion Target — Decision Log DB (SSOT)

Last updated: 2026-02-20 (KST)
Status: ACTIVE

## Purpose
Canonical Notion destination for decisions (mirroring local SSOT decisions).

## Target
- Notion DB: **Decision Log**
- URL: https://www.notion.so/22efd166397c4804af859c38ddfd1f44?v=9b8cb9689d9a42cda64819247561bdb5
- Database ID: 22efd166397c4804af859c38ddfd1f44
- View ID: 9b8cb9689d9a42cda64819247561bdb5

## What gets mirrored
- Skill scouting decisions: `context/skill_scouting/decisions/*.md`
- Strategy TFT outputs (when marked READY): `context/strategy_tft/**`
- Core decisions from `CURRENT_STATE.md` when promoted.

## Notes
- Do NOT upload raw longform documents unless explicitly approved.
- Mirror should store: summary + evidence paths + exposure tier + approval status.
