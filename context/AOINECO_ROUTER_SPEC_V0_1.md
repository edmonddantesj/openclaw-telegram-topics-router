# AOINECO ROUTER SPEC V0.1

## 1. Purpose
Aoineco의 다중 에이전트 운영을 **저소음 / 저비용 / 고명확성** 구조로 바꾸는 중앙 라우팅 규격.

목표:
- 여러 봇이 동시에 있어도 방이 시끄럽지 않게
- 누가 답해야 하는지 자동으로 정하고
- 사람 중심 흐름을 유지하고
- 향후 2명에서 N명까지 무리 없이 확장 가능하게 하는 것

---

## 2. Core Principles

### 2.1 Single speaker by default
기본값은 **한 번에 한 에이전트만 말한다**.
- 멀티 응답은 예외
- 기본은 대표 1명 응답
- 나머지는 내부 검토 또는 침묵

### 2.2 Router-first
모든 메시지는 먼저 라우터가 본다.
- 에이전트가 제멋대로 튀어나와 답하지 않음
- 라우터가 발화권을 배정
- 필요 없으면 아무도 안 부름

### 2.3 Human-first
에드몽 메시지가 최우선.
- 자율대화 중이어도 즉시 중단 가능
- 사람이 다시 말하면 사람 우선 모드 복귀

### 2.4 Silence is valid
대답하지 않는 것도 정상 동작.
- 이미 답이 충분할 때
- 인간끼리 대화 중일 때
- 호출할 가치가 없을 때
→ 침묵이 정답일 수 있음

### 2.5 Cost-aware
모든 메시지에 모든 에이전트를 붙이지 않는다.
- 최대한 적은 수만 호출
- 전체 브로드캐스트 금지
- 야간에는 더 엄격하게 제한

---

## 3. Components

### 3.1 Router
중앙 판단 계층.

역할:
- 메시지 분류
- 발화 필요 여부 판단
- 담당 에이전트 선택
- 멀티응답 허용 여부 판단
- 야간/비용 정책 적용
- 최종 출력 정책 결정

### 3.2 Agents
전문화된 역할 수행자.

예시:
- 청묘: 운영 / 구조화 / 실행 / 우선순위
- 흑묘: 전략 / 방향성 / 반론 / 큰 그림
- 청검: 보안 / 리스크 / 정책 점검
- 청비: 문서화 / SSOT / 기록 정리
- 청기: DevOps / 자동화 / 인프라 / 장애
- 청성: 성장 / 마케팅 / GTM
- 청안: 리서치 / 탐색 / 기회 스카우팅

### 3.3 Shared State
공유 컨텍스트 저장소.

예:
- topic-state
- playbook
- handoff
- thread/topic mapping
- 최근 결정 요약

이게 있어야 에이전트 수가 늘어나도 서로 안 꼬임.

---

## 4. Input Classification
라우터는 메시지를 최소 아래 6종으로 분류한다.

1. **Direct-tag** — 특정 에이전트 직접 태그
2. **Reply-targeted** — 특정 에이전트 메시지에 대한 답글
3. **Explicit multi-call** — 둘 이상을 명시적으로 호출 (`둘이 논의해` 등)
4. **General request** — 무태그 일반 질문/지시
5. **Human-human flow** — 사람끼리 대화 흐름
6. **Low-value/no-action** — 답할 실익이 거의 없는 메시지

---

## 5. Speaking-right Rules

### 5.1 Direct tag
- 특정 에이전트 태그 시 그 에이전트만 응답
- 다른 에이전트는 침묵

### 5.2 Reply priority
- 특정 에이전트 메시지에 답글이면 그 에이전트만 응답
- 다른 에이전트는 침묵

### 5.3 Explicit multi-call
다음과 같은 표현에서만 복수 에이전트 허용 가능:
- `둘이 논의해`
- `청묘 흑묘 둘 다 봐`
- `보안도 같이`

### 5.4 Untagged general messages
라우터가 메시지 성격으로 담당자를 선정.
- 운영/정리/실행 → 청묘
- 전략/방향성/사업구조 → 흑묘
- 보안/리스크 → 청검
- 문서/기록/SSOT → 청비
- 자동화/장애/시스템 → 청기
- 성장/홍보/GTM → 청성

### 5.5 Silence conditions
다음이면 응답 생략 가능:
- 이미 충분한 답 있음
- 인간 대화 흐름을 끊음
- 새 정보 없음
- 가치 없는 반복
- 야간에 긴급도 낮음

---

## 6. Response Modes

### Mode A: Single-owner
기본 모드.
- 한 에이전트만 응답
- 가장 싸고 깔끔함

### Mode B: Dual-response
두 명이 각각 짧게 응답.
허용 조건:
- 역할이 명확히 상보적일 때
- 전략+실행 같이 봐야 할 때
- 사용자가 명시적으로 허용/요청할 때

### Mode C: Internal debate → one spokesperson
권장 모드.
- 내부적으로 2~3명 검토
- 외부에는 대표 1명만 답변

### Mode D: Silent-log
- 외부 답변 없음
- 내부 기록만 남김

---

## 7. Autonomous Dialogue Protocol

### 7.1 Start triggers
다음 표현이 오면 자율대화 허용:
- `둘이 논의해`
- `둘이 얘기해`

### 7.2 Participation scope
기본은 청묘+흑묘 2인부터 시작.
향후 다자 확장 가능하되 기본 동시 참여 인원은 제한.

### 7.3 End conditions
다음 중 하나면 종료:
- 에드몽이 다시 메시지 보냄
- 결론/다음 액션 도출 완료
- 반복 논점 진입
- 야간 턴 제한 도달

### 7.4 Safeguards
- 무한 핑퐁 금지
- 같은 주장 반복 금지
- 새 정보 없으면 종료
- 밤에는 극단적으로 짧게

---

## 8. Night Mode

### 8.1 Time window
기본 제안: 23:00 ~ 08:00 KST

### 8.2 Principles
- 최소 발화
- 최소 호출
- 꼭 필요한 논의만
- 결론 나면 종료

### 8.3 Limits
- 자율대화: 1~3턴 이내
- 멀티 호출: 매우 제한적
- 긴 브레인스토밍 금지
- 농담/잡담 최소화

### 8.4 One-line rule
> 밤에는 “토론”보다 “정리와 결론” 중심으로만 움직인다.

---

## 9. Cost Control Policy

### 9.1 Call caps
- 일반 메시지: 최대 1명
- 중요 메시지: 최대 2명
- 내부 검토: 최대 3명
- 전체 브로드캐스트: 금지

### 9.2 No duplicate replies
- 같은 메시지에 유사 응답 반복 금지
- 이미 충분한 답이 있으면 추가 응답 금지

### 9.3 Re-call limits
- 같은 주제로 연속 호출 금지
- 새 정보/새 쟁점이 있을 때만 추가 호출

### 9.4 Night cost reduction
- 야간엔 multi-call 기준 상향
- 긴 응답보다 결론형 응답 선호

---

## 10. Routing Priority Order
라우터 판단 우선순위:
1. 시스템 규칙
2. 직접 태그
3. 답글 대상
4. 명시적 멀티 호출
5. 에드몽의 최신 운영 지시
6. 토픽 SSOT
7. 역할 기반 자동 분류
8. 침묵 판단

즉, 태그와 답글이 가장 강함.

---

## 11. Shared State Requirements
라우터는 최소한 아래 상태를 공유 컨텍스트로 유지해야 함:
- 최근 질문
- 최근 결론
- 최근 담당자
- 열린 논점
- 다음 액션
- 현재 모드(일반/자율/야간)
- 발화 제한 상태

이건 `topic-state` + `playbook` 구조와 결합하는 것을 권장.

---

## 12. Expansion Strategy

### Phase 1
2에이전트:
- 청묘
- 흑묘

### Phase 2
핵심 4에이전트:
- 청묘
- 흑묘
- 청검
- 청비

### Phase 3
운영형 스쿼드:
- 청기
- 청성
- 청안 추가

### Phase 4
내부 합의형 응답:
- 내부 소규모 논의
- 외부 대표 1명 응답

핵심은 늘어날수록 개별 자율 발화가 아니라 라우터 통제 강도를 높이는 것.

---

## 13. Failure Modes and Mitigations

### Failure 1: Everyone talks
원인: 라우팅 없음 / 역할 겹침
대응: single-owner 기본값 / 멀티응답 예외화

### Failure 2: Nobody talks
원인: 책임 불명확
대응: 라우터가 owner 지정 / fallback owner 두기

### Failure 3: Infinite ping-pong
원인: 서로 말에 계속 반응
대응: 자율대화 턴 제한 / 결론 나오면 종료 / 밤에는 더 짧게

### Failure 4: Cost explosion
원인: 전원 호출 / 긴 내부 토론
대응: 호출 상한 / silent-log 활용 / 대표 응답 선호

### Failure 5: Disrupting human conversation
원인: 맥락 없는 끼어들기
대응: human-human flow 감지 / 침묵 허용 강화

---

## 14. V0 Minimum Implementation
처음부터 필요한 최소 구현:
- 태그 감지
- 답글 대상 감지
- 야간 모드 적용
- owner 1명 선택
- 멀티호출 최대 2명
- 침묵 결정
- topic-state 읽기
- 최근 결정 반영

---

## 15. Operating Slogan
> 모두가 항상 말하는 팀이 아니라, 필요한 순간에 필요한 팀원만 정확히 나오는 팀.

---

## 16. Recommended Framing
- 봇 = 채팅 참가자
이 아니라
- 봇 = 라우터가 깨우는 전문 역할자

이 전환이 되면 확장성, 비용, 운영 통제가 모두 좋아진다.
