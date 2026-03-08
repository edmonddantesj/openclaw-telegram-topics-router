# DM_EXPORT_SHADOW_INGEST_AND_SAFE_PROMOTION_POLICY_V0_1

Status: SSOT

## Goal
1:1 DM Telegram export(HTML+media)에서 추출한 지식을 **토픽 운영(Forum topics)**에 안전하게 이식한다.
- 중복/충돌/추측을 방지
- “서버 삭제 이전 운영방식” + “현재 추가된 운영내용”을 최적으로 병합

## Definitions
- **Input (DM Export)**: Telegram Desktop export (messages*.html + photos/files/video_files)
- **Shadow Ingest**: DM에서 나온 내용을 **토픽에 바로 발행하지 않고**, 로컬 SSOT에만 먼저 적재/정리하는 단계
- **Safe Promotion**: Shadow Ingest 산출물 중 충돌 없는 최소 단위만 골라, 각 토픽(Forum topic)로 ‘패치’ 형태로 발행/이식하는 단계

## Golden rules (must)
1) **Proof-first**: 모든 주장/반복업무/결정은 최소 1개의 증빙을 가진다.
   - 메시지(날짜/파일) / 첨부 파일 경로 / 실행 로그 / commit hash 등
2) **No overwrite in Phase A**: Shadow Ingest 단계에서 기존 SSOT 섹션을 덮어쓰지 않는다.
3) **Patch-only promotion**: Safe Promotion은 ‘작은 패치’만 허용한다.
   - 예: 체크리스트 1개, 금지사항 1개, 자동화 후보 1개
4) **Conflict is explicit**: 충돌/중복 가능성이 있으면 반드시 `CONFLICT/CHOICE`로 표기하고, 토픽 Primary가 결정한다.

## Artifact locations
- Shadow Ingest output:
  - Per-topic playbooks: `context/topics/*_PLAYBOOK_V0_1.md`
    - 섹션: `## Imported from DM export (Shadow Ingest)`
  - Ongoing work: `context/handoff/HF_*.md` + `context/handoff/INDEX.md`
  - Compact snapshots: `context/telegram_topics/compact/DAILY_COMPACT_YYYY-MM-DD.md`

## Safe Promotion workflow (recommended)
1) 토픽별 Playbook에서 “Imported from DM export” 섹션 중 **promotion candidate**를 선택
2) 각 candidate는 다음 필드를 가진다:
   - Title
   - What changes (patch)
   - Proof
   - Risk / Conflict check
   - Owner
3) 토픽(Forum)에는 6-line Context Card + patch 내용 + proof를 함께 게시

## Sprint batching (4 topics per sprint)
- 4개 토픽을 1 sprint로 묶어 병렬 처리
- Primary 중복 시 청령이 collaborator 재배정

## Exit criteria
- Phase A 완료(1차): 주요 토픽 5개(ops/github/acp/maintenance/inbox-dev)에서 반복업무 Top N + 대표 Proof 1개씩 확보
- Phase B 완료(정밀): 전 토픽에 대해 중복 제거 + 증빙 보강 + 자동화 적용(launchd/Ralph Loop) 운영화
