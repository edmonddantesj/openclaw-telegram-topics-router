# ACP 자동행동 플래그(즉시/대기/리포트) + 승인 게이트 (v0.1)

## 목적
사용자가 자는 동안에도 ACP 관련 작업을 **최대한 자동으로 전진**시키되,
**돈/키/온체인/외부게시 같은 L3는 절대 자동 실행하지 않고** “승인 대기열 + 아침 1페이지 브리핑”으로 정리한다.

---

## 1) 액션 모드 3단계 (SSOT)
모든 ACP 액션(구매/교환/전송/등록/배포)은 아래 `action_mode` 중 하나를 반드시 가진다.

### A. `report_only` (리포트 전용)
- 실행: ❌
- 하는 일: 정보 수집/견적/리스크/필요 파라미터/시뮬레이션 결과를 정리해서 보고서로 남김
- 예시:
  - “이 에이전트 오퍼링 가격/평판/리뷰 요약”
  - “스왑 예상 수수료/슬리피지/실패 확률”

### B. `queue_for_approval` (대기/승인 큐)
- 실행: ❌ (자동으로는 안 함)
- 하는 일: 실행 계획을 **승인요청 객체(Approval Request)** 로 생성하고 큐에 쌓음
- 승인되면: 사람이 OK 하면 그때 실행 (또는 별도 run)

### C. `execute_if_preapproved` (사전승인 조건부 실행)
- 실행: ✅ 단, **사전승인 룰**을 100% 만족할 때만
- 사전승인 실패 시: 자동으로 `queue_for_approval`로 강등

---

## 2) 사전승인(Pre-Approval) 룰 — 최소 안전 세트
사전승인으로 자동 실행 가능한 건 **오직 아래 조건을 전부 만족할 때**만.

### 필수 조건
- (1) **자금 이동/온체인 tx 없음** (또는 0원 승인된 소액)
- (2) 키/시드/프라이빗키를 절대 다루지 않음 (지갑 연결/서명 포함)
- (3) 외부 게시 없음 (Moltbook/봇마당/X/ClawHub publish)
- (4) 증빙(Proof) 템플릿을 선행 생성 가능

### 금액/리스크 제한(기본)
- `max_usd_per_tx`: 0 (기본은 0으로 잠금)
- `max_usd_per_day`: 0
- `allowed_assets`: []

> NOTE: 이 값이 0이면 사실상 “자동 실행 금지”이고,
> 사전승인을 켜고 싶으면 의장이 숫자를 명시해야 한다.

---

## 3) 승인요청(Approval Request) 표준 포맷
- 저장 위치(권장): `aoi-core/state/approvals/` 아래 JSON
- 상태:
  - `PENDING_APPROVAL`
  - `APPROVED`
  - `REJECTED`
  - `EXPIRED`

### 필수 필드
- `id` (예: `acp-20260220-0001`)
- `created_at` (KST ISO)
- `action` (buy/swap/transfer/register/offering 등)
- `provider`
- `action_mode`
- `why_now` (왜 지금 해야 하는지)
- `risk_level` (LOW/MED/HIGH)
- `cost_estimate` (USD + 수수료)
- `required_inputs` (지갑/계정/파라미터 목록)
- `proof_plan` (어떤 증빙을 남길지)
- `dry_run_result` (가능하면)

---

## 4) “네가 잘 때” 권장 동작(오토 루틴)
- ACP 관련 이벤트가 생기면:
  1) 실행 가능한 건 `report_only`로 정보 수집
  2) 실행이 필요한 건 `queue_for_approval`로 승인요청 JSON 생성
  3) 아침 브리핑에 **1페이지 요약**으로 묶어서 올림

### 아침 1페이지 요약 포맷
- DONE(정보수집): N건
- PENDING_APPROVAL: N건 (id 목록)
- BLOCK: N건 (증빙/입력 누락)
- Next action(의장 1줄 액션):
  - ex) “acp-... 승인(OK) / 금액 상한 지정 / 거절”

---

## 5) 이 문서의 범위
- 정책(룰)과 데이터(승인요청/로그)는 분리한다.
  - 정책 SSOT: `aoi-core/state/acp_automation_policy_v0_1.json`
  - 실행요청 SSOT: `aoi-core/state/approvals/*.json`
