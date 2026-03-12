# random PLAYBOOK V0.1

- **Purpose:** 혼재된 이슈를 임시로 받되, 반복 운영형/교차 토픽형 작업은 오래 머물지 않게 분류·배출하는 토픽.
- **Last updated:** 2026-03-12

## Recurring tasks (must not forget)
1) random에 들어온 이슈는 가능한 빨리 분류한다
2) 반복 운영형/멀티스텝 실행형이면 HF 또는 Ralph Loop task로 변환한다
3) random 본문에는 긴 실행 로그를 남기지 말고 pointer만 남긴다
4) compact 전후로 맥락 유실 위험이 보이면, random 안에 암묵적으로 두지 말고 **복구 포인트를 명시적으로 남긴다**
5) 즉시 실행이 어려운 건 “나중에 기억”으로 두지 말고 **tracked artifact(HF/SSOT/task)** 로 전환한다

## Compact / context-loss recovery rule (2026-03-12 apply)
- random은 임시 논의 토픽이지만, 실제로는 context overflow / compaction / 복구 이슈가 반복되기 쉬운 버퍼 토픽으로 취급한다.
- 아래 중 하나가 보이면 compact 전 복구 포인트를 남긴다:
  - 작업이 여러 단계로 길어짐
  - 여러 파일/링크/결정사항이 섞이기 시작함
  - 재개 시점에 무엇을 이어야 하는지 한 번에 말하기 어려움
- 복구 포인트 최소 단위:
  - 현재 목표 1줄
  - 이미 끝난 것
  - 다음 액션 1~3개
  - 산출물/파일/토픽 포인터
- 복구 포인트는 random 본문에 짧게 남기거나, 길어지면 HF/handoff로 분리한다.

## HF split rule (2026-03-12 apply)
아래 중 하나면 random에 계속 쌓지 말고 HF로 뺀다:
- 오늘 안에 끝나지 않을 가능성이 큼
- 산출물이 2개 이상 생김
- 재개 시 증빙/결정/막힌점 추적이 필요함
- random 바깥 토픽/레포/운영체계와 연결됨

HF로 뺄 때는:
1) random에는 요약 + pointer만 남긴다
2) `context/handoff/INDEX.md`에 ACTIVE로 등록한다
3) 다음 액션은 HF를 기준으로 갱신한다

## Ralph Loop triage split (2026-03-12 lock-in)
### stays in random
- 임시 잡담/보류/분류 전 메모
- 아직 목적지가 확정되지 않은 단발성 이슈

### moves to Ralph Loop
- 반복 운영 업무
- 교차 토픽 조정이 필요한 멀티스텝 작업
- proof routing / decomposition이 필요한 혼재 이슈

### linked Ralph Loop records
- `context/ralph-loop-random-triage-note-2026-03-12.md`
- `context/ralph_loop/ledger.json` → `RL-20260312-035`

## Where to record
- 진행중 작업: `context/handoff/INDEX.md` 및 개별 HF
- 토픽 공통 규칙/체크리스트: 이 Playbook
- compact 전/후 복구 포인트: random 본문 short note 또는 관련 HF
