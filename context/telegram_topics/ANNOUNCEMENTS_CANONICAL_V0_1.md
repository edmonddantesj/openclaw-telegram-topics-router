# Announcements — Canonical Policy Pack (V0.1)

목적: 텔레그램 announcements(토픽 32)에 올라간 공지들이 **링크 열람 불가한 에이전트**에게도 항상 동일하게 적용되도록, 핵심 규칙을 로컬 SSOT로 고정한다.

**[공지 정본 경로]**
`/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/ANNOUNCEMENTS_CANONICAL_V0_1.md`

> 운영 원칙: 텔레그램 링크(t.me/...)는 일부 에이전트가 원문 열람을 못 할 수 있으므로,
> **중요 공지(규칙/정책)는 반드시 위 로컬 SSOT 경로의 정본을 확인**한다.

---

## 1) L1 / L2 / L3 권한·승인 기준

### L1 (자율)
- 가역적 내부 작업(리서치/정리/초안/내부 실험 등) → 바로 진행, 결과 공유
- 스스로 진행해야 하는 태스크가 새로 생기거나 backlog에 이미 있는 경우, **L1 범위는 승인/답변 대기 없이 즉시 실행**한다.
- 한 번 수락/인지한 작업은 방치하지 않는다. 즉시 실행이 어렵다면 **명시적 추적 아티팩트(SSOT/핸드오프/태스크 문서)** 로 전환한다.

### 전역 응답/실행 원칙
- 대응 누락/지연 이슈는 개인 메모가 아니라 **SSOT에 기록**한다.
- 불필요한 승인 대기를 만들지 않는다. 명확한 L1/L2 작업은 가능한 한 **선실행 후보고**를 기본으로 한다.
- 질문에 답만 하고 멈추지 말고, 실행 가능한 다음 액션이 명확하면 바로 이어서 진행한다.

### L2 (청령 1차 승인 / 조건부 청묘 2차 상위승인)
- 기본: **청령 1차 승인 후 진행 + 사후보고(링크/변경점/결과)**
- 아래에 해당하면 **청묘 2차(상위) 승인까지** 받고 진행:
  1) **대외 노출/발행**(공지·게시·배포·홍보 등)
  2) **운영/설정 변경**(봇·자동화·권한·배포·인프라 설정 등)
  3) **리스크/비가역 징후**(실수 시 손실·평판·보안 영향 가능)
- 애매하면 상향 적용(청묘까지 올려 확인)

### L3 (의장 직접 승인)
- 자금 이동, 토큰/키/권한의 비가역 조치, 대외 계약/법적 커밋, 온체인/외부게시 등

### CTA (작업 시작 포맷)
- 모든 토픽 작업은 시작 첫 줄에 “이번 작업: L1/L2/L3 + 승인 필요 여부”를 명시하고 진행

---

## 2) 전체 토픽 리스트(최신) — SSOT

SSOT 위치: `/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/thread_topic_map.json`

- acp = 50
- announcements = 32
- ops = 38
- adp = 45
- bazaar = 55
- github = 60
- longform = 65
- ralph-loop = 68
- hackathons = 71
- maintenance = 77
- random = 81
- inbox-dev = 585
- handoff = 586
- x-post = 956
- v6-invest = 1029
- moltbook = 1114

CTA) 새 이슈/자료/작업은 “어느 토픽에 쌓을지”부터 맞추고 올린다. 애매하면 announcements에 먼저 올린 뒤 라우팅.

---

## 3) 토픽 협업 공통 룰

- 기본은 Primary 오너십: 각 토픽은 Primary 1명이 책임지고 결론/다음액션을 정리한다.
- 필요할 때만 소집: `#call <요원명...>` / `#council core|market` / 전원은 `#all-hands` (진짜 필요할 때만)
- L3는 fail-closed: 돈/키/서명/온체인LIVE/외부게시(명시 승인 없음)/시크릿 관련이면 자동 진행 금지 → 청묘 에스컬레이션 후 확인.
- 길어지거나 얽히면 중간결론/다음액션은 `handoff` 토픽에 스냅샷으로 남겨 끊김 없이 이어가기.

참고 SSOT:
- `/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/TOPICS_DEFINITION_V0_1.md`
- `/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/TEAM_ATTENDANCE_COMMANDS_V0_1.md`
- `/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/DELEGATION_POLICY_V0_1.md`
- `/Users/silkroadcat/.openclaw/workspace/context/telegram_topics/ANNOUNCEMENTS_WORKFLOW_V0_1.md`
