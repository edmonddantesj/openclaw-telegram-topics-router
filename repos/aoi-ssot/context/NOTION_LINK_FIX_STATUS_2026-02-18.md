# Notion Link Fix — Status (2026-02-18)

## What we did
- Used audit report: `/tmp/notion_link_audit.json`
- Applied safe patches (only where a canonical `?v=` view URL was already discoverable in existing links):
  - Ran: `python3 scripts/notion_link_fix.py --report /tmp/notion_link_audit.json --apply`
- Result artifact:
  - `/tmp/notion_link_fix_plan.json`

## Applied (patched)
- 3 successful patches (1 additional ref was a noop because it pointed to an already-patched block).
- Patched IDs:
  - `3039c616-de86-8180-9c52-e8bf8dbb4c9e` → `...?v=3039c616de8681f5b087000c8e4f0546`
  - `3009c616-de86-81d7-b388-dcc6a13d7e38` → `...?v=3009c616de8681b991d2000cef95912e`

## Pending (need canonical view URLs)
We cannot fabricate Notion database view URLs via API. For each DB/data_source below, we need ONE canonical view link copied from Notion UI (it must include `?v=`):

- `3059c616-de86-8117-baac-000b292ea18b` :: 🏆 Hackathon Master Archive (Unified)
- `3039c616-de86-8181-becb-000b8aef43df` :: Aoineco Project Kanban
- `3039c616-de86-8138-b7f9-000bc9da6bef` :: Aoineco Squad Activity Logs
- `3059c616-de86-8138-8bfe-000ba4a470b8` :: 🌐 Connectivity Sentry
- `3059c616-de86-816b-90a6-000b4a4a2452` :: 🌍 Community Activity Logs
- `3059c616-de86-8166-8c3b-000b1d988e7d` :: 🗳️ Squad Suggestion Box
- `3059c616-de86-81a9-86d7-000b630e3cc8` :: 💼 Outsourcing Logs
- `195cc36a-3526-4c05-acce-a1259787306b` :: 🗓️ Aoineco Roadmap
- `1bc9de94-4e8a-4144-b314-7bcfe0e8f675` :: 🧰 Skill Inventory
- plus 5 others marked as database-not-page / not found in `/tmp/notion_link_fix_plan.json`

## Next step
1) Edmond provides canonical `...?v=...` links for the pending DBs.
2) Add a local mapping file (SSOT): `context/NOTION_CANONICAL_VIEW_MAP_V0_1.md`
3) Rerun patcher to replace ALL raw DB links.
