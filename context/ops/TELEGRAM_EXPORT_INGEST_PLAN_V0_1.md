# TELEGRAM_EXPORT_INGEST_PLAN_V0_1

목적: Telegram 전체 백업(HTML export + media)을 **정밀 분석 → 태그/토픽 분류 → SSOT/Playbook/HF로 승격**한다.

## Inputs
- Export root: `_inbox/telegram_export/ChatExport_2026-03-08_aoineco/ChatExport_2026-03-08 (16)/`
- Messages: `messages*.html`
- Media: `photos/`, `files/`, `video_files/`

## Output artifacts
1) Raw normalized log (machine-readable)
- `artifacts/telegram_ingest/normalized_messages.jsonl`

2) Tag index (for retrieval)
- `artifacts/telegram_ingest/tag_index.json`

3) Topic-tag summaries (human)
- `context/telegram_topics/EXPORT_SUMMARY_BY_TOPIC_V0_1.md`

4) SSOT updates
- Per-topic playbooks in `context/topics/*_PLAYBOOK_V0_1.md`
- Ongoing work → `context/handoff/HF_*.md` + `context/handoff/INDEX.md`

## Classification strategy (topic tagging)
- Use deterministic keyword→topic rules first (fast, controllable).
- Then refine with evidence-based clustering for ambiguous items.
- Never overwrite existing SSOT; only append with citations (message id/date + export file).

## Work stages
- Stage 0: Enumerate export + integrity stats
- Stage 1: Parse HTML → normalized JSONL (date, author, text, media refs)
- Stage 2: Topic tagging + confidence scoring
- Stage 3: Generate per-topic summaries + recurring tasks candidates
- Stage 4: Promote to SSOT/Playbook/HF + automation candidates
