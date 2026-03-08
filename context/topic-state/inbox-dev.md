# Topic State — inbox-dev

- Topic: `inbox-dev`
- Telegram topic id: `585`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- 긴급개발/핫픽스/데드라인 대응을 proof-first와 식별자 우선 원칙 아래 처리한다.

## Latest checkpoint
- 긴급건은 식별자 먼저, 모든 P0는 proof-first, 멈추기 전 Next 3 남기기가 고정 규칙이다.
- 현재 대표 active HF는 `context/handoff/HF_inbox_dev_urgent_202603.md`다.
- 외부 서비스/SDK 상태 오류는 재스캔/재조회가 1차 대응 패턴으로 남아 있다.

## Decisions locked
- HF 없이 추측 실행 금지.
- 배포 URL/PR/로그/재현 스텝 중 최소 1개 proof 확보.
- auth 이상 시 환경변수 오염부터 확인.

## Next actions
1. 새 P0 발생 시 HF 또는 토픽+키워드 식별자를 먼저 박는다.
2. 중단 전 Next 3를 반드시 남긴다.
3. 긴급 대응 결과는 proof와 함께 축약 보고한다.

## Key files
- Playbook: `context/topics/inbox-dev_PLAYBOOK_V0_1.md`
- Handoff: `context/handoff/HF_inbox_dev_urgent_202603.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- inbox-dev는 속도보다 “헛다리 안 짚기”가 중요하다. 식별자 없는 긴급 대응은 사고 난다.
