# ACP Offering MVP Spec v0.1 — deBridge SOL↔BASE Swap (Proof-first, Guarded)

## 0) 목적 / 포지셔닝 (한 줄)
**“Not a trading bot.” 크로스체인 스왑을 ‘안전장치+영수증(proof)’ 포함해서 대신 실행해주는 Execution Safety Layer.**

## 1) 현재 전제 (리스크/현실)
- ACP `job create`가 간헐적으로 **500**을 반환 → **딜리버리 플러밍 안정화 전에는 자금이 움직이는 오퍼링 go-live 금지**
- 따라서 MVP는 **Staged rollout**:
  1) Internal dry-run (no fund movement)
  2) Friendly users + small caps
  3) Production (L3 승인 후)

## 2) 사용자 가치 (왜 사는가)
- SOL↔BASE 브릿지/스왑을 “실패/슬리피지/사기” 리스크 없이 처리하고 싶음
- 요청 1건마다 **증빙 번들 + tx 영수증**이 남아야 팀 운영에 넣을 수 있음

## 3) MVP 범위 (추천)
### 3.1 Chain/Token Scope
- **Base-only target** / **Solana source**
- 초기 지원은 가장 안전한 1개부터:
  - (권장) `SOL USDC → BASE USDC`
- token/chain은 **allowlist**로 시작 (확장 시 L3)

### 3.2 Modes
- `plan` (견적/라우트/리스크 평가만)
- `execute` (실제 실행) — **L3 승인 게이트 필수**

## 4) 입력 스키마 (요약)
- from_chain (fixed=solana)
- to_chain (fixed=base)
- from_token (allowlist)
- to_token (allowlist)
- amount (max cap)
- max_slippage_bps (default 50~100)
- deadline_seconds
- mode: plan|execute
- notes

## 5) 가드레일 (Security 기본값)
### 5.1 금액/범위 제한
- `max_amount_usd_per_job` (예: $50~$200)
- 일일/시간당 실행 횟수 제한

### 5.2 Slippage/Time bounds
- `max_slippage_bps` 강제
- `deadline_seconds` 강제
- 실행 직전 quote 재확인 (2회 비교) → 악화되면 **abort**

### 5.3 Fail-closed
- RPC/quote/route/receipt 검증 실패 시 **즉시 중단**
- 재시도는 제한(예: 1~2회) + idempotency key 기반

### 5.4 Custody boundary
- “custody 없음”을 기본 원칙으로 정의
- 자금 이동 구조가 custody로 해석될 여지가 있으면 **L3에서 법/리스크 검토 후**

## 6) Proof bundle (필수)
출력은 항상 `/private/tmp/aoi_acp_<runId>/` 아래에:
- `input.json` — 요청
- `report.json` — 결과
- `proof.json` — sha256 + manifest

### report.json 포함 항목(최소)
- runId, ts
- mode(plan/execute)
- quotes (initial, pre-exec)
- route summary (provider=deBridge)
- policy snapshot (caps, slippage, deadline)
- results:
  - success/fail
  - from_tx (solana)
  - bridge_tx
  - to_tx (base)
- pre/post balances (가능 범위)

## 7) 운영/딜리버리 안정화
- ACP job-create 500을 고려해 fallback runner 필요:
  - 내부 큐 + idempotent re-run
  - 로그 트렁케이트 방지(safe_run)

## 8) 가격(초안)
### Tier 1 (Friendly / MVP)
- **Fixed**: 0.10 ~ 0.25 USDC / swap

### Tier 2 (Pro)
- Fixed + %: 0.05 USDC + 0.05% ~ 0.15%
- 더 높은 cap + 우선 처리 + incident/abort 정책 포함

## 9) 차별점 문구(초안)
- Proof-first artifacts (sha256) — “영수증이 기본값”
- Guarded execution — caps/slippage/deadline/abort가 제품의 핵심
- LIVE gated — 실행은 승인/정책 통과 시에만

## 10) 승인 게이트 (L3)
아래는 **L3 승인 필수**:
- mode=execute로 자금 이동을 켜는 시점
- cap 상향
- allowlist 확장
- 24/7 상시 운영
- 외부 홍보/포스팅/공개 리스팅

---
*Source: Team Council requestId 7bdda933-503a-4a4d-ac5a-4cbe8abc5fb5 + AOI governance (L1/L2 autonomous, L3 approval only)*
