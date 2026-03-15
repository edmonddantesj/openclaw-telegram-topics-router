# PRD v0.1 — Longform Triage Summarizer (Lite on ClawHub) + ACP Post Executor (Pro)

Status: Draft v0.1
Owner: Edmond (PO) + Aoineco (Builder)
Date: 2026-02-19

---

## 1) Problem
When PDFs/DOCX/longform articles arrive, the bottleneck is:
- Reading time + context loss
- Inconsistent handling (sometimes stored, sometimes not)
- Lack of operational guardrails (secrets/PII)
- Posting workflows require manual formatting + approval checks

We want a repeatable system that:
- Summarizes fast
- Classifies importance (S/A/B/C)
- Applies storage policy automatically
- Produces ready-to-post drafts (EN/KR)

---

## 2) Goals
### Lite (ClawHub public-safe)
1. Ingest longform input (PDF/DOCX/URL/plain text)
2. Produce summary (multi-length)
3. Auto-triage into S/A/B/C
4. Apply storage policy (local only / no-save) without posting
5. Output: internal brief + optional EN/KR drafts + approval question template

### Pro (ACP paid offering)
1. Accept a prepared draft + explicit approval token
2. Post to a single platform (Moltbook-first)
3. Return proof (post id/url, http code, log path, sha256 of input)

---

## 3) Non-goals (v0.1)
- No autonomous posting in Lite.
- No multi-platform posting in Pro (v0.1 is Moltbook-only).
- No full “timeline sync”/Notion DB automation inside Lite v0.1.
- No secret vault management UI.

---

## 4) Users / Personas
- Builder/Founder who receives many docs and wants:
  - quick extraction of “what matters”
  - operational next actions
  - drafts for community posting

---

## 5) Inputs (Supported)
### A) Local files
- `.pdf`
- `.docx`

### B) Links
- `http(s)://...` (article)

### C) Pasted text

---

## 6) Outputs (Lite)
### 6.1 Minimal output (always)
- Title guess
- Source URL (if any)
- **Importance: S/A/B/C + 1-line rationale**
- Summary (5–10 lines)
- “Next actions” (1–3)

### 6.2 Optional outputs (config)
- EN draft (neutral)
- KR draft (neutral polite)
- “Approval gate prompt” template:
  - “올릴까? (Moltbook Yes/No, 봇마당 Yes/No)”

---

## 7) Triage policy (S/A/B/C)
### S
- Money / security / legal / irreversible actions / external announcements
- Default: save local fulltext, strict masking, no external drafts unless requested

### A
- Product/ops/SOP/strategy directly applicable
- Default: save local fulltext + produce actionable summary

### B
- Benchmark/learning/ideas
- Default: **NO fulltext saving**. Instead, write a **detailed key-point brief**:
  - One-liner (1)
  - Key points (10–15 bullets, include numbers/constraints)
  - Claims / Evidence / Examples (3–5 each)
  - Apply-to-us ideas (3)
  - Risks / Caveats (3)
  - Source/meta

### C
- Light reading / low relevance
- Default: **no saving (local+Notion)**; keep only short summary (3–7 lines) + source link

---

## 8) Storage policy (Edmond final)
- **C:** no-save (local+Notion)
- **S/A:** local-only fulltext permitted; Notion only gets summary/metadata (no attachment)
- **B:** no fulltext saving (detailed key-point brief only)

Implementation note:
- Lite skill MUST be safe even without Notion integration.

---

## 9) Public-safe / Security gate (mandatory)
Before writing any stored artifact or generating external drafts:
- scan for secrets/PII patterns (keys, tokens, mnemonics, wallet privkeys)
- mask detected tokens
- record scan summary (PASS/WARN)

Fail-closed rules:
- If “secret-like token” detected AND output is external draft → block draft generation unless `--override`.

---

## 10) UX / CLI (Lite) — proposed
Command:
```bash
python3 longform_triage.py \
  --in /path/to/file.pdf \
  --source-url "https://..." \
  --out-dir /tmp/longform_triage \
  --mode lite
```

Outputs:
- `brief.md`
- `draft_moltbook_en.md` (optional)
- `draft_botmadang_kr.md` (optional)
- `scan.json`
- (optional) `fulltext.txt` (only for S/A; never for C)

---

## 11) ACP Pro offering (v0.1)
Offering name: `longform_post_executor_moltbook`

Requirements JSON (example):
```json
{
  "platform": "moltbook",
  "title": "...",
  "content": "...",
  "submolt_name": "general",
  "approval_token": "...",
  "source_url": "https://...",
  "public_safe": true
}
```

Rules:
- Must verify `approval_token` (issued only after user says Yes)
- Must enforce rate limit handling (429 → retry scheduling or fail with retry_after)
- Must return proof bundle:
  - input.json + response.json + sha256 + log path

---

## 12) Metrics / Success criteria
Lite:
- Time-to-brief < 60s for typical docs
- Correct S/A/B/C classification >70% user satisfaction (manual thumbs-up)
- Zero secret leaks in generated drafts

Pro:
- Posting success rate >95% (excluding rate limit windows)
- Proof bundle generated 100%

---

## 13) Release plan
### Phase 0 (this week)
- Implement Lite CLI with docx/pdf extraction + triage + summary
- Add public-safe scanner
- Add unit tests for S/A/B/C heuristic

### Phase 1
- ClawHub publish Lite (no keys, no posting)

### Phase 2
- Implement ACP Pro offering (Moltbook-only)
- Add approval token + VCP proof

---

## 14) Open questions
1) (RESOLVED) B 등급: fulltext 저장하지 않음. 대신 디테일 요점요약 포맷으로 남김.
2) Draft tone presets (Moltbook EN / Botmadang KR) 고정 vs 사용자 커스텀?
3) Approval token format: simple hash vs signed nonce?
