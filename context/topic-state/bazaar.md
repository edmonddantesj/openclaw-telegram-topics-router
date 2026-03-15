# Topic State — bazaar

- Topic: `bazaar`
- Telegram topic id: `55`
- Status: ACTIVE
- Last saved: 2026-03-09 16:55 KST

## Current objective
- Nexus Bazaar / The Archive / NEXUS Arena 개발 메인 룸 운영.
- Execution Receipt / Proof-first execution engine 단일 주제 집중.

## Latest checkpoint
- API route 확장 및 DB/RLS 템플릿 반영 완료.
- Supabase(demo-receipts) 연동 및 백엔드 server.js 안정화 단계.
- ADP Recovery용 Tailscale host(`choi-macmini.tailc63c7c.ts.net`) 및 3010 포트 근거 확보.

## Decisions locked
- LIVE 실행은 승인 없이는 금지(L3 게이트).
- Bazaar는 DeFi aggregator 서사가 아니라 agent liquidity mesh 서사로 유지.
- 3/9 데모 기준: Archive UI는 증빙 제출/조회 무대, Bazaar/Arena는 TEASER로 제한.

## Next actions
1. launchd 자동화 적용 및 HF(`HF-20260308-BAZAAR-TOPIC55-ROLLUP.md`) 기반 운영 정착.
2. Supabase 키/URL 정확성(대시보드 URL 오입력) 상시 감시.
3. 3/9 데모용 증빙 파이프라인(JSONL/DB) 최종 검증.

## Key files
- Playbook: `context/topics/bazaar_PLAYBOOK_V0_1.md` (Synced from analyzer context)
- Handoff: `context/handoff/HF-20260308-BAZAAR-TOPIC55-ROLLUP.md`
- Topic map: `context/telegram_topics/thread_topic_map.json`
- Agent map: `context/telegram_topics/thread_agent_map.json` (Primary: 청뇌)

## Restore instructions
- `agents/analyzer/context/` 하위의 최신 ops/handoff 문서를 우선 참조한다.
- 복구 시 `Execution Receipt / Proof-first` 축을 최우선으로 리포트한다.

## Notes
- 청뇌(analyzer)의 로컬 컨텍스트와 글로벌 워크스페이스 컨텍스트 정합성을 맞춤.
- Bazaar 토픽의 primary agent는 청뇌로 확정됨.
- 단, **토론/검토/복구 판단이 필요한 경우 owner 1인 고정으로 닫지 않고 병렬 팀원 호출 가능**.
- explicit multi-call 트리거 예:
  - `토론해줘`
  - `같이 논의해줘`
  - `병렬로 봐줘`
  - `팀원 불러서 봐줘`
  - 특정 팀원 2명 이상 동시 호출
- 위 트리거 시 Bazaar는 청뇌 단독 응답보다 `병렬 검토 → 합의 요약`을 우선한다.
