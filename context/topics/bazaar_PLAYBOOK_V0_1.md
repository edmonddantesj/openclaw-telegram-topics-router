# Topic-55 운영 Playbook v0.2

> SSOT 기준: topic:55 백업 + handoff + topic-state + 2026-03-13 agent-wide announcement 반영

## 1) 역할 / 범위 (Scope)
- **토픽 고정:** `topic:55` = `NEXUS Bazaar / The Archive / NEXUS Arena` 개발 메인 룸
- **owner:** 청뇌 (`analyzer`)
- **bazaar가 보유하는 truth:**
  - 제품 범위 / 데모 경계
  - listing / receipt / checkout / review 관련 구현 선택
  - 최종 deliverable acceptance
  - live 노출 여부에 대한 최종 판단 초안
- **human gate 전용 영역:**
  - login
  - identity confirmation
  - payment / signing
  - final public deployment approval
  - external publishing / outward message send

## 2) 현재 핵심 방향
- Bazaar는 단순 데모가 아니라 **trust-aware marketplace skeleton** 쪽으로 확장 중
- 현재 중심축:
  - listing submit / review / publish 흐름
  - listing detail 중심 구조화
  - trust/category/pricing/review metadata
  - checkout / receipt 연결 문맥 강화
- 단, **라이브는 보수적**으로 운영
  - Bazaar는 `local-test-first`
  - `archive.aoineco.ai`는 live production surface

## 3) 응답 / 운영 기본 규칙
1. 기본 응답 포맷은 가능하면 **오늘 할 일(P0) / 블로커 / 다음 액션**
2. 반복 규칙/결정/핵심 상태는 chat에만 두지 말고 durable 문서로 승격
3. 공지 확인 시 bazaar 문맥으로 필요한 운영 규칙을 topic-state/playbook에 반영
4. `bazaar ping` 규격은 `pong + market / worker / api` 상태 3줄 포맷을 기준으로 유지
5. 길어지는 작업은 HF / handoff / proof artifact로 분리

## 4) Live / local 구분 규칙 (중요)
Archive/Bazaar 상태를 말할 때는 아래를 절대 섞지 않는다:
- code changed
- local build succeeded
- local preview verified
- live site updated

### 고정 status bucket
- `LOCAL_ONLY`
- `LOCAL_VERIFIED`
- `STAGING_ONLY`
- `LIVE_CONFIRMED`

### 규칙
- `archive.aoineco.ai`를 직접 확인하기 전엔 **LIVE_CONFIRMED**라고 말하지 않음
- `nexus-bazaar-webapp` 로컬 성공은 live 반영을 뜻하지 않음
- live 변경은 실제 live-source repo/path 기준으로만 판단

참조 SSOT:
- `context/ops/ARCHIVE_BAZAAR_DEPLOYMENT_AND_LIVE_GATING_PROTOCOL_V0_1.md`

## 5) 보안 / 노출 규칙
승인 전 라이브 금지:
- admin surfaces
- internal review workflows
- hidden routes / moderation controls
- payout / treasury topology
- live checkout/payment beyond approved safe scope
- receipt internals / trust weighting internals
- STEALTH / TOP SECRET 분류 내용

즉:
- public-safe copy/UI polish는 제한적으로 가능
- incomplete commerce/admin/security-sensitive paths는 local/staging 유지

## 6) Ralph Loop split (L2 ACTIVE)
`bazaar`는 build/domain room이고, 반복 내부 실행은 Ralph Loop로 보낸다.

### L2 고정 recurring task shape
- RL-BZ-01 backlog slicing
- RL-BZ-02 checkpoint packet generation
- RL-BZ-03 proof/evidence routing
- RL-BZ-04 scope guard before premature live exposure

### cadence
- Bazaar 구현 묶음이 생길 때마다
- scope/live/local 혼선이 생길 때마다
- 반복 패키징/체크포인트 작업이 필요할 때마다

### trigger
- 새 구현 burst
- 상태 요약이 필요한 시점
- live reflection 요청
- backlog가 커져서 task slicing이 필요한 시점

### packet format
- `today`
- `blocker`
- `next`
- 필요 시 추가:
  - target repo
  - deployment status bucket
  - proof path

### proof / artifact paths
- `context/topic-state/bazaar.md`
- `context/topics/bazaar_PLAYBOOK_V0_1.md`
- `context/ralph-loop-bazaar-transfer-2026-03-12.md`
- `context/handoff/`
- analyzer `context/handoff/`
- 관련 proof / decision artifacts

### return rule to source topic
아래는 다시 `bazaar`에서 결정한다:
- 제품 범위 변경
- 데모 경계 재설정
- 구현 방향 선택
- 최종 acceptance
- live 노출 여부 판단

### escalation rule
아래는 main-session / human gate로 올린다:
- production deployment approval
- login / identity / payment / signing
- 외부 게시 / outward message send
- security-sensitive live exposure
- repo-to-live mapping 불명확

## 7) 현재 구현 우선순위
현 시점 우선순위는 아래 순서:
1. listing detail → actual checkout / receipt connection
2. admin review → structured edit / metadata control
3. runbook / operational stabilization
4. chunk / vendor split 같은 최적화는 blocker 아닐 때 후순위

## 8) current-state에 반드시 남길 key points
- Bazaar는 local-test-first
- `the-archive-webapp`는 live-source repo 계열
- `nexus-bazaar-webapp`는 active local Bazaar expansion stream
- live 반영 여부는 직접 확인 전까지 추정 금지
- listing은 real일 수 있어도 일부 engagement metric은 demo일 수 있음

## 9) durability / mirror rule
- active authoritative working layer는 local workspace `context/`
- durable knowledge layer는 `md-vault` / private GitHub mirror도 고려
- local-only / ephemeral 문서는 명시적으로 그렇게 표시

## 10) key linked files
- `context/topic-state/bazaar.md`
- `context/ralph-loop-bazaar-transfer-2026-03-12.md`
- `context/telegram_topics/TOPIC_STATUS_INDEX_V0_1.md`
- `context/ops/ARCHIVE_BAZAAR_DEPLOYMENT_AND_LIVE_GATING_PROTOCOL_V0_1.md`
- `context/handoff/HF-20260308-BAZAAR-TOPIC55-ROLLUP.md`

## 11) re-entry rule
Bazaar 관련 작업 재진입 시 검색 순서:
1. topic-state
2. playbook
3. handoff / HF
4. deployment/live gating SSOT
5. proof / decision artifacts

기억이나 분위기로 이어가지 말고, durable state부터 읽고 이어간다냥.

## 12) Heukmyo support routing
- 리서치/비교표/체크리스트/운영 문서화/market skeleton 정리처럼 범위를 나눠서 보조 산출물이 필요할 때는 `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md` 기준으로 흑묘팀 지원 요청을 구조화한다.
- 기술성 높은 요청(배포 경계, repo/live 매핑, incident/recovery, 구현 리스크)은 optional extension field(`Affected scope`, `Failure mode`)를 함께 붙인다.
- final public deployment approval / outward message send / payment / signing은 계속 human gate로 남긴다.
