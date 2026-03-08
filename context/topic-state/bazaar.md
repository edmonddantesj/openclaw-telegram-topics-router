# Topic State — bazaar

- Topic: `bazaar`
- Telegram topic id: `55`
- Status: ACTIVE
- Last saved: 2026-03-08 23:13 KST

## Current objective
- Nexus Bazaar / Guild 계열 작업을 시장 내러티브가 아니라 제품·데모·운영 단위로 재개 가능하게 관리한다.

## Latest checkpoint
- Nexus Bazaar는 DEX 라우팅이 아니라 Agent Liquidity Mesh(on-chain RFQ/intent)로 재정의된 바 있다. Source: memory/2026-03-05.md#L485-L503
- Public 3/9 데모는 report-only/simulation, LIVE 실행은 L3 승인 게이트가 고정 원칙이다. Source: memory/2026-03-05.md#L485-L503
- Bazaar/Guild 계열 결과와 템플릿 반영 이력이 있어, 이 토픽은 제품 서사·데모 경계·승인 게이트를 압축 기억해야 한다.

## Decisions locked
- LIVE 실행은 승인 없이는 금지.
- Bazaar는 DeFi aggregator 서사가 아니라 agent liquidity mesh 서사로 유지.
- 데모/패키징/서사는 해커톤/제품/운영 토픽과 겹치더라도 여기서 현재 목표를 분명히 둔다.

## Next actions
1. 현재 Bazaar 관련 데모/패키징/서사 작업이 있으면 목적과 blocker를 명시.
2. Guild 연계 작업은 관련 HF 또는 SSOT로 분리.
3. 외부 노출/라이브 액션이 끼면 승인 상태를 먼저 적는다.

## Key files
- Playbook: `context/topics/bazaar_PLAYBOOK_V0_1.md`
- Handoff: (없음)
- Topic map: `context/telegram_topics/thread_topic_map.json`

## Restore instructions
- 먼저 이 파일을 읽고, 실제 내용이 얇으면 Playbook과 관련 HF를 최소만 추가로 읽는다.
- 복구 응답은 `현재 목표 / 마지막 체크포인트 / 다음 액션` 순서로 짧게 재구성한다.

## Notes
- bazaar는 서사가 쉽게 퍼지므로 “지금 하는 게 데모인지, 설계인지, 라이브인지”를 반드시 써둔다.
