# HF_sprint_loop_handoff_20260308

Owner: 청정(maintainer) / Control: ralph-loop(Topic 68)
Last updated: 2026-03-08

## 1) Goal (3줄)
- 1:1 DM Telegram export(HTML+media)에서 반복업무/결정/증빙을 **토픽별 SSOT(Playbook/HF)**로 내재화한다.
- 반복업무를 **launchd(고정주기) vs Ralph Loop(처리량/백로그)**로 분류해 자동화 후보를 만들고, 가능한 것은 운영에 붙인다.
- 최종적으로 토픽에 ‘작은 패치(Safe Promotion)’로 배포하고 **ADOPT/HOLD/CONFLICT** 회신으로 충돌 없이 병합한다.

## 2) Current State (Sprint status)

### Sprint 1 — DONE (회신 대기)
- Topics: ops / maintenance / inbox-dev / github
- Shadow Ingest: DONE (Playbook에 Imported 섹션 + Proof)
- Automation candidates doc: DONE
- launchd audit report: DONE (maintenance 토픽 발행)
- Safe Promotion patches: 발행 완료 → ADOPT/HOLD/CONFLICT 회신 대기
- Proof:
  - Commits: `2602b51`, `daf5645`, `67fdf76`
  - Safe Promotion msgs: ops=3190, github=3191, maintenance=3192, inbox-dev=3193
  - Audit post: maintenance(77) msgId=3189

### Sprint 2 — DONE (회신 대기)
- Topics: acp / adp / handoff / ralph-loop
- Shadow Ingest: DONE
- Automation candidates doc: DONE
- Safe Promotion patches: 발행 완료 → ADOPT/HOLD/CONFLICT 회신 대기
- Proof:
  - Commit: `23a08cb`
  - Safe Promotion msgs: acp=3194, adp=3195, handoff=3196, ralph-loop=3198

### Sprint 3 — NEXT
- Topics: v6-invest / x-post / longform / hackathons
- Target deliverables:
  1) Shadow Ingest → per-topic playbook Imported 섹션 시드 + Proof 1+
  2) `context/ops/AUTOMATION_CANDIDATES_SPRINT3_V0_1.md`
  3) Safe Promotion patches(4개) 발행 + 회신 수집

### Sprint 4 — NEXT
- Topics: bazaar / moltbook / random / none/untagged triage
- Same deliverables

### Sprint Loop backlog SSOT (canonical)
- `context/ralph_loop/SPRINT_LOOP_BACKLOG_V0_1.md` (commit: `9c1ae28`)

## 3) Routing Rules (DM export → topic)

### Primary rule
- **Shadow Ingest 먼저(로컬 SSOT 적재)** → Safe Promotion(토픽 패치) 순서. (덮어쓰기 금지)
- (none/미분류)는 Ralph Loop로 oldest-first triage.

### Tagging / 분류 구현(현 상태)
- 정규화/태깅은 로컬 아티팩트 기반:
  - normalized: `artifacts/telegram_ingest/normalized_messages.jsonl`
  - tagged: `artifacts/telegram_ingest/tagged_messages.jsonl`
- 1차 keyword 룰(수정 가능): `context/ops/tools/topic_tagging_rules.json`
- 태깅 스크립트: `context/ops/tools/topic_tag.mjs`
- HTML 파서: `context/ops/tools/telegram_export_parse.mjs`

### Important patterns (high-signal)
- Notion/GitHub 연동: ‘표(속성) 업데이트’ vs ‘본문 append’ 분리 실패 패턴(DoD로 고정)
- 운영/주기작업: launchd(plist) + proof artifact 경로가 있으면 ops/maintenance 우선
- ADP: 명칭(ADP) 고정 + local/tailnet URL 구분 + hung restart
- ACP: UI job 미노출은 지갑/에이전트 컨텍스트 불일치 우선

## 4) SSOT Paths (must-read canon)
- Merge policy: `context/ops/DM_EXPORT_SHADOW_INGEST_AND_SAFE_PROMOTION_POLICY_V0_1.md`
- Sprint backlog: `context/ralph_loop/SPRINT_LOOP_BACKLOG_V0_1.md`
- Ingest plan: `context/ops/TELEGRAM_EXPORT_INGEST_PLAN_V0_1.md`
- Export topic summary: `context/telegram_topics/EXPORT_SUMMARY_BY_TOPIC_V0_1.md`
- Topic maps:
  - thread→topic: `context/telegram_topics/thread_topic_map.json`
  - topic→agent: `context/telegram_topics/thread_agent_map.json`
- Playbooks (Sprint 1/2 touched):
  - `context/topics/ops_PLAYBOOK_V0_1.md`
  - `context/topics/maintenance_PLAYBOOK_V0_1.md`
  - `context/topics/inbox-dev_PLAYBOOK_V0_1.md`
  - `context/topics/github_PLAYBOOK_V0_1.md`
  - `context/topics/acp_PLAYBOOK_V0_1.md`
  - `context/topics/adp_PLAYBOOK_V0_1.md`
  - `context/topics/handoff_PLAYBOOK_V0_1.md`
  - `context/topics/ralph-loop_PLAYBOOK_V0_1.md`
- Launchd audit report: `context/ops/MAINTENANCE_LAUNCHD_AUDIT_REPORT_2026-03-08_V0_1.md`

## 5) Automation (what’s running + what to add)

### launchd (loaded) — key ones
- `ai.aoi.maintenance_digest_3h` (00:01/03:01/.../21:01) → digest proof in `artifacts/digest/digest_*.txt`
- `ai.aoi.notion_sync_digest_am_pm` (08:50/20:50) → proof in `artifacts/notion_digest/notion_sync_digest_*.txt`
- `ai.aoi.knowledge_index_digest_0901` (09:01)
- `ai.aoi.maintenance_daily_smoke` (09:10)
- `ai.aoi.ralph_loop_daily_scan_2300` (23:00)
- `ai.aoi.ralph_loop_sync_hourly` (StartInterval=3600) — **path risk**: `agents/oracle/work/...`
- `ai.aoi.state_snapshot_upload_daily` (09:20) — **path risk**: `agents/oracle/work/...`

### What to add (candidates)
- Sprint 3/4에서 도출되는 반복업무를 launchd vs Ralph Loop로 계속 분류(문서: `context/ops/AUTOMATION_CANDIDATES_SPRINT*_V0_1.md`).

## 6) Safe Promotion (회신/처리 규칙)
- Safe Promotion은 토픽에 “작은 패치”로 발행하고, **Primary에게 ADOPT/HOLD/CONFLICT 1개로만 회신** 요청.
- CONFLICT면: “현행 SOP/작업과 충돌하는 지점 1줄”만 받아서 SSOT에 `CONFLICT/CHOICE`로 표기 후 조정.
- 진행상태는 `context/ralph_loop/SPRINT_LOOP_BACKLOG_V0_1.md`에 반영.

## 7) Next 3 (청정 즉시 실행)
1) **Sprint 1/2 회신 수집** (ADOPT/HOLD/CONFLICT) → backlog SSOT 업데이트
   - Proof: `context/ralph_loop/SPRINT_LOOP_BACKLOG_V0_1.md`에 상태 업데이트 + commit
2) **Sprint 3 Shadow Ingest 실행**
   - 대상: `context/topics/v6-invest_PLAYBOOK_V0_1.md`, `x-post_PLAYBOOK_V0_1.md`, `longform_PLAYBOOK_V0_1.md`, `hackathons_PLAYBOOK_V0_1.md`
   - Proof: 각 playbook에 Imported 섹션 + Proof(msgId/file) + commit
3) **Sprint 3 Safe Promotion patches 발행** (토픽별 1개씩) + 회신 요청
   - Proof: 각 토픽 messageId + backlog SSOT에 기록
