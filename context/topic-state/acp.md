# Topic State — acp

- Topic: `acp`
- Telegram topic id: `50`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- ACP 오퍼 운영, Dispatch(Bought & Analyzed), 지갑/증빙 체계를 승인 게이트 아래 지속가능하게 굴린다.

## Latest checkpoint
- ACP Wave/Dispatch 공개 방향은 “완료 리포트”보다 Progress + Proof 중심이 SSOT 방향이다.
- Public/Internal 2레일, 승인 게이트, 시크릿 비공개, HQ Brief 톤 원칙이 고정돼 있다. Source: memory/2026-03-05.md#L470-L489
- 현재 active HF는 `context/handoff/HF_acp_ops_202603.md`, `context/handoff/HF_acp_dispatch_002_202603.md`이며, 오퍼 운영/Dispatch #002 준비를 여기서 이어받는다.

## Decisions locked
- ACP 전용 워룸은 topic 50으로 고정.
- 구매/온체인/offer 등록/외부 게시 = 승인 필수.
- SSOT에는 주소/포인터만 저장하고 키/시크릿은 저장하지 않는다.
- Dispatch는 주 1회 투고, 과도한 빈도 금지.

## Next actions
1. 현재 Dispatch #002의 today-ready 여부와 blocker를 HF에서 확인.
2. 오퍼/지갑 상태 점검이 필요하면 주소 컨텍스트와 proof부터 맞춘다.
3. 규칙 변경은 Playbook, 진행 이슈는 HF, 빠른 재개 요약은 topic-state에 반영.

## Key files
- Playbook: `context/topics/acp_PLAYBOOK_V0_2.md`
- Handoff: `context/handoff/HF_acp_dispatch_002_202603.md`, `context/handoff/HF_acp_ops_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- ACP는 승인 게이트와 증빙이 핵심이라, action 전 반드시 “승인 필요 여부 / proof 경로 / wallet context” 3가지를 확인.
