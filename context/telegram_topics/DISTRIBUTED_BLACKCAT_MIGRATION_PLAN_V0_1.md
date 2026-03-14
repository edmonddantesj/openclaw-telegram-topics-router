# DISTRIBUTED BLACKCAT MIGRATION PLAN V0.1

## Goal
`cat-strategic`(topic 6062)에서 **청묘 서버**와 **흑묘 서버**가 각자 자기 본체/자기 Telegram bot으로 직접 대화하는 분산 2본체 구조로 전환.

## Current confirmed state
- 청묘 bot(`@Mercedes_cyrano1_bot`)는 청묘 서버에서 정상 동작.
- 흑묘 bot(`@Mercedes_cyrano_3_bot`)는 이미 그룹/토픽 참여 가능.
- 청묘 서버에 붙였던 임시 흑묘 연결은 철거 완료.
- topic 6062의 owner/turn-taking/playbook/router SSOT는 이미 존재.

## Success criteria
1. 흑묘 bot 토큰은 **흑묘 서버에서만** 사용한다.
2. topic 6062에서:
   - 청묘 질문 → 청묘 bot 응답
   - 흑묘 질문/차례 → 흑묘 bot 응답
3. 흑묘 DM이 기존처럼 유지된다.
4. 두 서버가 같은 규칙(playbook/router spec)을 공유한다.

## Migration steps
### Phase 1 — 흑묘 서버 준비
- OpenClaw 설치/기동 확인
- `@Mercedes_cyrano_3_bot` token을 흑묘 서버 OpenClaw에만 연결
- strategist persona/workspace/AGENTS/SOUL/USER 반영
- telegram binding: topic 6062 -> strategist/heukmyo

### Phase 2 — shared rules sync
- 아래 파일을 흑묘 서버에도 동일 반영:
  - `context/topics/cat-strategic_PLAYBOOK_V0_1.md`
  - `context/topic-state/cat-strategic.md`
  - `context/AOINECO_ROUTER_SPEC_V0_1.md`
  - `context/AOINECO_ROUTER_OWNER_SELECTION_LOGIC_V0_1.md`
  - `context/AOINECO_AGENT_TO_AGENT_DIALOGUE_RUNTIME_V0_1.md`
  - `context/CAT_STRATEGIC_ROUTER_CHECKLIST_V0_1.md`

### Phase 3 — live verification
- 단일 owner 테스트
- reply-target 테스트
- `둘이 논의해` dual turn-taking 테스트
- DM survival test

## Guardrails
- 같은 Telegram bot token을 두 서버에서 동시에 polling 금지
- 한쪽에서 테스트 중이면 다른 쪽 연결 금지
- edgecase는 `AOINECO_ROUTER_EDGECASE_LOG_V0_1.md`에 기록

## Immediate next actions
1. 흑묘 서버 접근 경로/호스트 확인
2. 흑묘 서버 OpenClaw 상태 확인
3. strategist 파일셋 이식
4. 흑묘 서버에 token+binding 적용
5. topic 6062 실전 검증
