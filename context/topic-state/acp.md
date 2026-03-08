# Topic State — acp

- Topic: `acp`
- Telegram topic id: `50`
- Status: ACTIVE
- Last saved: 2026-03-08 23:08 KST

## Current objective
- Topic 50(ACP)에서의 모든 운영을 “증빙/승인/자동화” 기준으로 지속가능하게 굴리기 위한 규칙/반복업무/체크리스트 SSOT.

## Latest checkpoint
- ACP 전용 워룸 규칙(증빙/승인/자동화, 시크릿 금지, proof-first)이 Playbook에 고정됨.
- Dispatch 운영, 지갑/키 운영, offer 운영의 기본 원칙과 기록 위치가 정리됨.
- 진행중 이슈는 HF_acp_ops / HF_acp_dispatch_002로 분리되어 있음.

## Decisions locked
- 모든 토픽은 기본적으로 `context/topic-state/<slug>.md`를 가진다.
- 반복 규칙은 Playbook, 열린 이슈는 HF, 즉시 복구 요약은 topic-state에 둔다.

## Next actions
1. 진행중 ACP 작업은 관련 HF 기준으로 이어가기.
2. 새 규칙은 Playbook에, 실행 이슈는 HF에 반영.
3. 구매/온체인/외부 게시 등 승인 게이트 작업은 선승인 확인.

## Key files
- Playbook: `context/topics/acp_PLAYBOOK_V0_2.md`
- Handoff: `context/handoff/HF_acp_dispatch_002_202603.md`, `context/handoff/HF_acp_ops_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ACP는 시크릿/결제/외부행동이 섞이므로 topic-state만 보고 성급히 실행하지 말고 HF/승인 상태까지 확인.
