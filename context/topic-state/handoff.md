# Topic State — handoff

- Topic: `handoff`
- Telegram topic id: `586`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- HF 중심 handoff/dispatch/compact로 컨텍스트 끊김을 막고 병렬 작업을 제어한다.

## Latest checkpoint
- ACTIVE/HOLD/DONE 정본은 `context/handoff/INDEX.md`이고, 큰 작업은 모두 `HF_*.md`로 관리하는 구조가 정착돼 있다.
- 장문/이전대화 인입은 끝까지 읽기 → 요약 → 분석/제안 → SSOT 저장 순서가 고정 규칙이다.
- 컨텍스트 60% 이상이면 compact/reset 권고를 함께 주는 운영 규칙도 여기와 연결된다.

## Decisions locked
- 큰 작업은 반드시 HF 1장으로 분리.
- 결정 3종 세트는 즉시 영구 저장.
- thread/topic 매핑은 병렬 라우팅의 전제다.

## Next actions
1. ACTIVE HF 우선순위를 checkpoint에 반영.
2. 새 에픽 시작 시 HF 생성 후 INDEX 등록.
3. compact/handoff 산출물 경로도 함께 남긴다.

## Key files
- Playbook: `context/topics/handoff_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_handoff_compact_reminder_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- handoff는 세부 내용보다 “어떤 HF를 먼저 읽어야 하는가”를 명확히 해주는 게 핵심이다.
