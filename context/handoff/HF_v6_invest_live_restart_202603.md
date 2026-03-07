# HF: v6-invest 실투 재개발/운영 인수인계 (Topic 1029)

- **Status:** ACTIVE
- **Owner:** 청뇌
- **Last updated:** 2026-03-08 07:03 KST
- **Where:** Telegram topic **v6-invest=1029**

## Goal
- `/openclaw` 삭제/DB 부재 상태에서도 v6 투자 운영의 연속성을 복원.
- 이전 대화에서 확정된 규칙/실패 교정 지점을 SSOT화.
- V6 실투 엔진은 현재는 **재개발 전제**로 처리하고, 새 개발 포인트를 받으면 즉시 라이브 붙임.

## Current state (what works / what’s broken)
- **확정된 운영 방향**
  - Stage0 EV-max가 최종 방향. 매시 고정 50분이 아니라 EV 최대치 시점(T-10/-5/-2/-1)에서 판단.
  - 실매수는 기본적으로 T-5 또는 T-2 슬롯 + 조건 충족 시만.
  - 최근 Stage0 v0.2에서 `수수료/슬리피지/체결가 반영` 및 과도한 99센트 주문 제한 개선 반영.
- **현재 제약/이슈**
  - 현재 로컬/워크스페이스 기준으로 볼 때 **V6 실투 본체가 존재하지 않음** (repo 내 직접 실행 가능한 전략 코드 부재).
  - 과거 로그상 라이브 진입의 장벽: Portfolio 미생성 403, API 키 누락, 서명자 mismatch, Market approval 미완, smartwallet 모드/EOA 모드 혼선.
  - 사용자 확인 결과: 재시작 시 inbox-dev에서 새로 개발해 공지해 줄 예정.
- **현재 자동화 상태**
  - 기존 백업/대화상으로는 1시간 요약(`evmax` digest) 운영 의도가 있었음.
  - 이번 SSOT 정합성화 단계에서 `scripts/v6_invest_routine.sh` + launchd 스텁을 SSOT에 반영(루틴 로그 생성 목적)해 반복 점검 자동화 준비.

## Decisions made
- “기존 코드 복구”가 아니라 **재개발 전제**로 이어감.
- 큰 작업은 HF로 분리, 플레이북은 규칙/반복업무만 보관.
- 다음 inbox-dev 공지는 아래 템플릿으로 받되, 실제 운영 반영은 이 HF에 근거 연결.
  1) repo/branch/commit
  2) DRY_RUN/LIVE/approve entrypoint
  3) vault/env 경로 + 필요한 키
  4) 운영 규칙(커나리/일일 캡/스톱 조건)
- 서브세션/OPUS 요약은 원문 덮어쓰기 금지, 한국어 5~10줄 + 적용 항목 공유만.

## Next actions (ordered)
1) inbox-dev에서 전달될 새 V6 개발 공지 수신 후 즉시 통합:
   - 실행 루틴 매핑(실행 명령, env, approval)
   - 라이브/DRY_RUN 분기별 재확인
2) v6-invest SSOT 점검 루틴 1시간 주기 실행 검증:
   - `scripts/v6_invest_routine.sh`가 `artifacts/v6_invest_routine/`에 heartbeat log를 남기는지 확인
3) 실제 코어 재개발 완료 시, `status/Blocker/Proof` 기준으로 `HF`의 현재 상태를 DONE 또는 재개로 갱신.

## Commands / paths / proofs
- v6 playbook: `context/topics/v6-invest_PLAYBOOK_V0_1.md`
- handoff index: `context/handoff/INDEX.md`
- active HF: `context/handoff/HF_v6_invest_live_restart_202603.md`
- ops spec: `context/limitless/LIMITLESS_V6_OPS_SPEC_V0_1.md`
- launchd+루틴 스텁:
  - script: `scripts/v6_invest_routine.sh`
  - plist: `launchd/ai.aoi.v6-invest-routine.plist`
- 증빙 아티팩트(재개발 후): `artifacts/limitless_stage0_evmax/`, `artifacts/limitless_live_trades/`, `artifacts/limitless_autotrade_dryrun/`

## Risks / blockers
- V6 엔진과 스케줄러 코드를 아직 받지 못함(재개발 의존).
- 환경/지갑 모드 mismatch가 반복되면 첫 카나리 뒤에도 실패 가능.
- 루틴 스크립트는 SSOT 운영용 보조 장치이며, 거래 성패 판단에는 실제 실행 코어의 증빙이 우선.