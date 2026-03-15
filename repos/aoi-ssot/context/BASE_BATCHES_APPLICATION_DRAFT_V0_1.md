# Base Batches / SKALE Credit Application Draft (AUTO-START)

> Purpose: Start the application flow immediately after EigenCloud completion.
> Note: "Base batches" likely refers to the post-hackathon credits request context in our ops log (SKALE x402 grant / DoraHacks). This draft is structured so it can be pasted to the official form once URL is opened.

## 1) 기본 정보 (fill once, then lock)
- Project: `7-dollar-bootstrap-x402`
- Team: `Aoineco & Co.` / Owner `Edmond`
- Repository: `https://github.com/edmonddantesj/7-dollar-bootstrap-x402`
- Demo/Artifact links:
  - GitHub repo: https://github.com/edmonddantesj/7-dollar-bootstrap-x402
  - Demo (if public): n/a (attach if available)
  - Proof bundle (if used): `https://github.com/edmonddantesj/7-dollar-bootstrap-x402`

## 2) 제출 본문(베이스 템플릿)
### 프로젝트 요약
- Problem: 기존 x402 결제/검증 데모에서 **신뢰 가능한 증빙 체계(Proof-first)**가 약함.
- Solution: `aoi-token-safety` + `aoi-squad-pro` 계열 구조를 활용해 **증빙 가능한 결제/검증 워크플로**를 구축.
- Edge: mock verifier를 넘어 실제 on-chain/검증 레이어로 이행 가능한 구조, 최소 단위 E2E 증빙(로그, runId, sha256)을 남길 수 있음.

### why credits
- 개발 초기 단계에서 인프라/테스트/실행 비용 최적화가 필요
- SKALE integration PoC의 비용 장벽을 줄여 실제 통합률을 높이고, 대회 산출물을 빠르게 고도화하려고 함

### 30/60/90 Day plan (짧게)
- 30d: Mock verifier 대체 모듈 설계, 최소 기능 계약 배포 플랜 수립
- 60d: SKALE-backed verification 모듈 PoC + demo 증빙 캡처
- 90d: 검증 파이프라인 정식 통합 + 공개 제출용 proof bundle 자동화

## 3) 첨부 체크리스트
- [ ] Eligibility 확인 (x402 participant / SKALE integration 가능 여부)
- [ ] Commit history: 최신 안정 commit
- [ ] Repo 구조: main entry, README, 실행 방법
- [ ] Proof/증빙: runId / proof_dir / sha256 샘플
- [ ] 팀 소개: 역할/연락창구
- [ ] 계약/보고 범위: 월간 크레딧 사용 계획
- [ ] IP/브랜딩 제한 동의 여부

## 4) 팀카운슬 권고 반영 항목
- Credits scope(무엇에 쓰는지) 확인
- 만료일/리포트 주기 확인
- continued development 기준 정의 후 동의
- 증빙 요구 항목 확정 (contract/address/tx/docs)

## 5) 즉시 제출 전 마지막 점검
- [ ] URL/폼 필드에 "Conditional Go" 근거(현재 상태: 기존 PoC + proof-first 기반)
- [ ] 현재 진행 상황을 CURRENT_STATE/memory에 기록
- [ ] 제출 후 증빙 링크(확인 메일/티켓번호 등) 저장

