# ACP 바운티 고수익 스킬 로드맵 (버전 0.1)

## 1) 목표
1. ACP 상에서 **운영형 스킬 3개 이상** 등록/운영하여, 바운티를 수주/완료할 수 있는 자기완결형 서비스 체인을 구성한다.
2. 핵심 차별점은 `proof-first + audit bundle`로 증빙성을 높여 신뢰 기반 매출 기회를 확보한다.
3. 초기 2~4주 안에 **파일럿 바운티 3건 처리(성공 완료)**를 목표로 한다.

---

## 2) 전제/운영 원칙
- 모든 산출물은 `input` + `deliverable` + `evidence`
- 민감값(토큰/키/경로/IP)은 출력에서 redaction
- 단일 실행 산출물 크기 제한(너무 크면 실패 방지)
- 가격 정책: 저가-고속 체류로 신뢰 획득 후 점진적 고가 전환
- `requiredFunds=false`로 시작해서 입문 장벽 낮춤
- 실패 시 자동 취소/재시도 패턴은 1회만 + 명시적 이유 반환

---

## 3) 배포 대상 스킬 (우선순위 순)

### A. `bounty_scope_plan` (1순위)
**목적:** 바운티 설명서 템플릿화
- 입력: 목표, 제약, 결과물 포맷, 마감일
- 출력: 실행가능한 작업 분해(SOP), 평가 체크리스트, 산출물 스키마
- AC(수락기준):
  - 300자 내 핵심 요구에서 5개 하위작업 생성
  - 위험요인 3개 + 완화안 2개 반환
  - 증빙 필드 목록 제공

### B. `bounty_match_maker` (2순위)
**목적:** 바운티와 기존 에이전트/기술스택 매칭
- 입력: 요구 스킬 태그, 난이도, 예산
- 출력: 후보 스킬 추천 + 근거 + 진행 절차
- AC: 
  - 최소 3개 후보 스코어링
  - 각 후보별 적합점수(0~100), 리스크 레벨 포함

### C. `bounty_qc_packager` (3순위)
**목적:** 바운티 완료물 자동 점검 + 증빙 번들 생성
- 입력: 제출물 링크/내용, 기준서
- 출력: 규격 준수 점검표, 이슈 라인, 수정권고, proof bundle hash
- AC: 
  - 누락/규칙 위반 항목 정량화
  - `evidence.json` 형태로 최종 리포트

### D. `bounty_status_ledger` (선택)
**목적:** 바운티 상태 추적 + 정산 로그
- 입력: 바운티 ID, 단계 변경 이벤트
- 출력: 상태 타임라인 + KPI 대시보드
- AC:
  - posted/accepted/in_progress/delivered/paid/closed 6단계 추적
  - `cost_per_stage`, `risk_notes` 포함

### E. `postmortem_finisher` (옵션, 3주차)
**목적:** 완결 보고서 자동 생성(재수주용 레퍼런스)
- 입력: 바운티 산출물 + 로그
- 출력: 1페이지 회고 + 개선안
- AC:
  - 재수주 가능한 판매형 요약 150자/500자 2개 버전

---

## 4) 실행 일정 (2주 기준 집중 스프린트)

### Week 1
- **D1~D2:** 기반 정비
  - 기존 ACP 오퍼링 구조 분석, 공통 유틸 `redact`, `sha256` 템플릿 확정
  - AC 템플릿(입력/출력 스키마 v0.1) 확정
  - `bounty_scope_plan` handler/offering.json 구현
- **D3:** `bounty_scope_plan` 테스트
  - 샘플 3개 요구사항으로 산출물 QA
  - 리포트 포맷 통일
- **D4~D5:** `bounty_match_maker` 구현
  - 후보 스코어링 규칙 작성(태그 매칭, 과거성공률, SLA)
- **D6~D7:** 내부 배포/리허설
  - `acp sell create` dry-run
  - 내부 사용자 2명으로 수주 시뮬레이션

### Week 2
- **D8~D9:** `bounty_qc_packager` 구현
  - 산출물 검증 규칙 + evidence JSON 구조
- **D10:** 3개 스킬 동시 등록/테스트
  - 각 스킬 1건씩 시뮬레이션 요청-처리
- **D11:** 가격/설명문 최적화
  - fee 조정(0.02~0.08 USDC)
  - 템플릿 언어 최적화(한국어/영어)
- **D12~D14:** 바운티 1차 론칭
  - 실제 바운티 1개 등록, 1개 매칭 수락 시도
  - 성공/실패 로그 수집 후 v1 수정

---

## 5) 4주 확장 버전
- **Week 3:** `bounty_status_ledger` + 대시보드 메시지 템플릿 강화
- **Week 4:** 상위 수익 바운티 대응 가드레일(복잡요건 분해, 타임박스, 리스크 조정) 추가
- 각 스킬별 리뷰 템플릿/FAQ 추가

---

## 6) 제안할 오퍼링 가격안 (초기)
- `bounty_scope_plan`: 0.03 fixed
- `bounty_match_maker`: 0.05 fixed
- `bounty_qc_packager`: 0.08 fixed
- `bounty_status_ledger`: 0.02 fixed

---

## 7) 필수 제출/리뷰 문구(고정 템플릿)
- `Schema`: `aoi.acp.<offering_name>.v0.1`
- 필수 출력 필드:
  - `result_schema`, `input_digest`, `steps`, `findings`, `risk`, `next_actions`, `self_audit`
- 증빙 필드:
  - `sha256`, `generated_at`, `runtime`, `version`

---

## 8) 즉시 시작 체크리스트 (오늘)
1. Git checkout/branch: `chore/workspace-cleanup-20260217` 기준으로 새 브랜치 생성
2. `skills/openclaw-acp/src/seller/offerings/` 아래 3개 디렉토리 생성
   - `bounty_scope_plan`
   - `bounty_match_maker`
   - `bounty_qc_packager`
3. 각 offering.json + handlers.ts 초안 작성
4. `acp sell create <offering>`로 등록
5. 내부 1차 dry-run 바운티 호출

---

## 9) 성공 지표 (KPI)
- 2주차 말: 오퍼링 3개 등록
- 3주차 말: 내부 바운티 3건 성공 처리(최소 1건 실결제)
- 4주차 말: 실패율 20% 이하, 1회 당 평균 리턴 시간이 10분 이하

---

## 10) 지금 바로 다음 액션(네가 승인하면 바로 실행)
1) `bounty_scope_plan` 우선 구현
2) 1개 샘플 바운티 스펙 확정
3) `handlers.ts` 템플릿 작성
4) 2시간 내 첫 커밋
