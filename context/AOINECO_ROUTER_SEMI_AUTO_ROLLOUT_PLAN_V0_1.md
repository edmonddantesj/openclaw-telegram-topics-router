# AOINECO ROUTER SEMI-AUTO ROLLOUT PLAN V0.1

## 1. Purpose
완전 자동 라우터를 바로 만드는 것이 아니라,
현재 OpenClaw + Telegram 토픽 구조 위에 **반자동 라우터**를 단계적으로 얹는 적용안.

핵심 목표:
- 규칙 오작동 줄이기
- 중복 응답 줄이기
- 야간 토크비용 줄이기
- 나중에 N-agent로 확장 가능한 구조 만들기

---

## 2. What to Automate in V0.1
처음부터 판단이 명확한 것만 자동화.

### A. Direct-tag detection
- 특정 봇 태그면 그 봇만 owner
- 다른 봇 silent

### B. Reply-target detection
- 특정 봇 메시지에 대한 답글이면 그 봇 우선
- 다른 봇 silent

### C. Night mode detection
- 23:00~08:00 KST 자동 적용
- dual 기준 강화
- silent 허용 폭 확대

### D. First-pass owner recommendation
- 무태그 메시지 간단 분류:
  - 전략형 → 흑묘
  - 실행형 → 청묘
  - 애매함 → 청묘 fallback

### E. Silent recommendation
- 이미 충분한 답 있음
- 가치 낮음
- 인간끼리 대화 흐름
→ silent 추천

---

## 3. What to Keep Manual in V0.1
아직 운영 규칙/수동 보정으로 두는 영역.

### A. Mixed-intent messages
- 전략 + 운영 + 리스크가 섞인 복합 질문

### B. Final dual-response approval
- 자동 추천은 가능
- 실제 듀얼 발화는 보수적으로

### C. Topic-specific overrides
- cat-strategic 같은 특수 규칙은 playbook override 유지

### D. Long autonomous dialogue
- 자동 시작은 가능해도 길이/턴 수는 강하게 제한

---

## 4. Inputs
반자동 라우터가 참조할 입력.
- 메시지 본문
- reply context
- topic id
- current time
- topic-state
- playbook / router spec / owner logic / edgecase log

---

## 5. Outputs
최소 출력 필드.
- `mode`: single / dual / silent
- `owner`
- `secondary` (optional)
- `reason`
- `confidence`: low / medium / high

예시:
- `single | 청묘 | null | 실행형 질문 | high`
- `dual | 흑묘 | 청묘 | 전략+실행 혼합 | medium`
- `silent | null | null | 이미 충분한 답 있음 | high`

---

## 6. Runtime Flow
1. 메시지 수신
2. 라우터가 direct-tag / reply-target / night mode / multi-call / owner category 빠르게 판별
3. `single` / `dual` / `silent` 결정
4. 그 결과를 실제 발화 규칙에 반영

---

## 7. Recommended Operating Mode
완전 자동보다 **추천 + 강한 기본 규칙** 구조 권장.
- 라우터가 내부적으로 판단
- 결과는 강한 운영 가이드처럼 적용
- 아직은 절대 자동보다 반자동 강제 가이드에 가깝게 운영

---

## 8. Why cat-strategic first
- 이미 규칙이 문서화돼 있음
- 청묘/흑묘 2봇 구조가 명확함
- 전략/실행 분기 테스트에 좋음
- 야간 모드 필요성이 이미 확인됨

즉, 이 토픽을 v0 shadow/soft-enforcement 실험장으로 사용.

---

## 9. Deployment Phases

### Phase A — Shadow mode
- 라우터가 내부적으로만 판단
- 실제 발화는 기존 규칙대로 유지
- 목적: 오판 패턴 수집 / edgecase 축적

### Phase B — Soft enforcement
- 명확한 규칙부터 실질 적용
  - 태그
  - 답글
  - 야간 single 우선
  - silent 추천

### Phase C — Owner-assisted mode
- 무태그 메시지에도 owner 추천이 실전 영향력을 가짐

### Phase D — Semi-auto stable
- 반자동 라우터를 사실상 기본 운영 계층으로 사용

---

## 10. Success Criteria
- 태그/답글 오작동 감소
- 잘못 끼어드는 빈도 감소
- 밤시간 과잉 대화 감소
- 무태그 owner 선택 일관성 증가
- edgecase가 문서 기준으로 수정 가능해짐

---

## 11. Failure Signals
- reply-target인데 다른 봇이 계속 끼어듦
- 전략/실행 분류가 자주 뒤집힘
- 야간인데 dual/장문이 계속 나옴
- silent여야 할 메시지에 자꾸 반응
- owner 추천이 지나치게 자주 애매함

---

## 12. Recommended Next Actions
1. cat-strategic에서 shadow mode처럼 운영
2. 엣지케이스 3~5개 수집
3. owner logic v0.2 수정
4. soft enforcement 선언
5. 이후 다른 토픽으로 확장

---

## 13. One-line Summary
- 태그/답글/야간은 자동
- 복잡한 혼합 질문은 반자동
- cat-strategic에서 먼저 shadow 운영
- edgecase가 쌓이면 v0.2로 진화
