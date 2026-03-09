# Topic-55 운영 Playbook v0.1

> SSOT 기준: topic:55 대화 백업(2026-03-08) 기반

## 1) 역할/범위(Scope)
- **토픽 고정:** `topic:55` = `NEXUS Bazaar / The Archive / NEXUS Arena` 개발 메인 룸.
- **핵심 주제(3/9 데모):** `Execution Receipt / Proof-first execution engine` 단일 주제.
- **금지(우선순위):** 데모에서 범위를 확장하는 기능(시장/결제/복잡한 아레나 기능)은 1순위 증빙 파이프라인 완성 뒤에만 접목.

## 2) 운영 규칙(반복 규칙, 영구 적용)
1. 기본 응답 포맷: **오늘 할 일(P0) / 블로커 / 다음 액션**
2. 큰 작업/긴급건은 **HF 문서 1장**에 누적: 상태/결정/증빙/Next
3. 공지 대응 규칙: 새 공지 확인 시 `announcements(32)`에서 확인 후, 각 토픽에서 `확인했다냥`으로 회신
4. 반복 ping 규격: `bazaar ping`은 `pong + market / worker / api` 3줄 상태 포맷(필요 시 명령어 분기)
5. SSOT 원칙: 진행상태 1줄 요약은 `CURRENT_STATE.md`(또는 없으면 동일 역할 파일) + 결정/증빙은 `ops/items/` 혹은 HF 본문에 고정 보관
6. 배치형 데모 운영: `Archive UI`는 증빙 제출/조회 데모 무대, `Bazaar/Arena`는 TEASER 1줄 위주로 제한
7. 보안 고정: `SUPABASE_SERVICE_ROLE_KEY`는 프론트에 노출 금지(서버 단독), admin 승인 동작은 비밀번호(ENV)로 가드
8. 증빙 규칙: 제출은 append-only 감사 추적(권장: JSONL), 상태 변경도 로그로 남김

## 3) 의사결정 규칙(Decision Rules)
- A → B → C 순서
  - A) Archive MVP(3/9 Proof-first)
  - B) Bazaar Market/Queue/Settlement 안정화
  - C) Arena Loop 정의
- 각 단계는 공통으로 다음을 준수: **Done 정의 + 산출물(증빙) + Next**
- 실행 전 1~3개 옵션 질문이 생기면 `1개만` 확정 질문으로 수렴
- 최종 확정 후에는 즉시 문서(S SOT) + 작업 카드(P0)로 정리 후 실행

## 4) 3/9 실행 기준(Receipt-first 정합)
- **Submit 방식:** 웹 폼(텍스트/URL) 고정
- **저장 구조:** DB + JSONL
  - DB: 즉시 조회/필터/상태변경 UX
  - JSONL: append-only 감사로그
- **승인 방식:** Admin UI 페이지로 1개 화면에서 승인/거절 처리
- **공개 정책:** 공개 UI는 approved만 노출(또는 해당 동치 처리)
- **개발 스택(현재):** Vite + React Router(프론트) + Node `server.js`(API)

## 5) 기술 스택/저장소 약속
- Supabase 데모 프로젝트: `nexus-bazaar-demo-receipts` (데모 전용)
- API 엔드포인트(필수):
  - `POST /api/receipts` (anon 제출)
  - `GET /api/receipts?item_slug=...` (공개 조회: 승인 데이터)
  - `POST /api/receipts/:id/status` (admin + 비밀번호 + service_role)
- 테이블 정책(요약):
  - anon: insert only, status write 금지
  - 공개 read: 승인 데이터만
  - status update/delete: 서비스 권한 경로에서만

## 6) 체크포인트(필수)
- Supabase SQL/RLS 적용 후 API Smoke 테스트 4종
  - 제출→공개 조회(미승인/빈 배열 정상)→승인→공개 조회(반영)
- 서버 재시작: 코드 변경 후 `server.js` 재시작 필수
- 에러 추적: API 응답은 `{ok,error,code,details,hint}` 형태로 남겨 원인 즉시 추적

## 7) 반복 작업 자동화 규칙(Launchd)
- 매일 09:30 KST: Topic-55 현재 상태 스냅샷을 handoff 폴더에 한 건 남김
- 새 백업 유입 감지 시: raw 백업 보존 + 백업 기반 요약/핵심 규칙 추출 갱신
- 수동 개입 포인트 최소화: 백업 파일 배치 후 5분 안에 자동 파서가 `context/handoff/INDEX.md`/`TEAM_STATUS` 반영을 시도

## 8) 파일 네이밍 규칙
- 핸드오프: `context/handoff/HF-YYYYMMDD-<slug>.md`
- 상태: `context/ops/TEAM_STATUS_DASHBOARD_V0_1.md`
- 정책/규칙: `context/handoff/HANDOFF_POLICY_V0_1.md`
- 백업 원본: `context/archives/topic55_<date>_backup_raw.md`

## 9) 보존 원칙
- 모든 진행중 큰 작업은 HF로 분리하고, 결정은 playbook/hf의 링크로 수렴.
- 대화/작업 로그는 보존하고, 정리본은 SSOT만 운영 기준으로 사용.
