# v6-invest PLAYBOOK V0.1 (Topic 1029)

- **Purpose:** V6/Limitless 운영의 결정·검증·반복업무를 SSOT로 고정하고, 운영 중단 없이 이어받을 수 있게 유지한다.
- **Last updated:** 2026-03-08
- **Where:** `context/topics/v6-invest_PLAYBOOK_V0_1.md`

## Recurring rules (must not forget)
1. **큰 작업은 HF 1장 분리**
   - 결정/막힘/실험 결과/변경 이유는 `context/handoff/HF_*.md`에만 누적한다.
   - 대화에서는 핵심 요약 + 다음 액션만 공유.

2. **Live 전환은 증빙 우선**
   - 재시작/재개발이든 재시도든 `Proof` 없이 판단을 못 받는다.
   - 최소 증빙: 로그/스크립트 결과/tx hash/폴더 아티팩트 위치.

3. **거래 룰은 고정 값이 아니라 정책 기반**
   - 초기 고정시간(`매시 50분`)은 폐기, **EV 최대 타임 슬롯 선택**으로 운영.
   - 기본 진입 후보: T-10 / T-5 / T-2 / T-1, 실매수는 T-5/T-2 한정.

4. **Fail-closed/가드 먼저**
   - `EV > 0`, 허들/신뢰조건 통과, 지갑/포트폴리오/서명 체인/승인 상태를 먼저 통과 후 주문.
   - 기본 카나리 한도는 재검토 없이 올리지 않는다.

5. **OPUS/거대 리뷰 결과는 한국어 요약만 공유**
   - 영문 원문 재게시로 인한 혼선 금지.
   - 변경 항목(무엇을/왜/어디서)만 HF+채팅에 반영.

6. **중복 메시지/작동 불일치 대응**
   - 동일 서브세션 알림이 반복되면 원문 재공유 대신 “중복 알림 건너뛰기 + 기존 HF/요약만 유지”.

## Active work record
- **Canonical:** `context/handoff/INDEX.md`
- **Current active HF:** `context/handoff/HF_v6_invest_live_restart_202603.md`

## Operational workflow (replay)
1. **재개발 전제면 우선 순위는 보존**
   - 코드/브랜치/커밋이 없는 상태면 즉시 재개발 가정으로 전환한다.
   - 새로 들어오는 개발 공지는 아래 형식으로 받는다.
     - repo / branch / commit
     - dryrun entrypoint / live entrypoint / approve entrypoint
     - vault/env path + 필수키 목록
2. **라이브 전 점검 체크리스트 (최소 세트)**
   - Limitless Portfolio 상태 (created)
   - EOA↔SmartWallet 모드 정합성
   - API 키·PRIVATE_KEY 로딩
   - approval / collateral / cap 적용
3. **자동화(반복업무)**
   - `scripts/v6_invest_routine.sh` + launchd `launchd/ai.aoi.v6-invest-routine.plist`로
     1시간 단위 루틴 로그(최신 아티팩트/핸드오프 상태)를 생성.
   - 주기 로그만으로 HF 갱신 여부를 점검한다.

## Automation (launchd)
- Script: `scripts/v6_invest_routine.sh`
- Plist: `launchd/ai.aoi.v6-invest-routine.plist`
- Start:
  - `mkdir -p ~/Library/LaunchAgents`
  - `ln -sf /Users/silkroadcat/.openclaw/workspace/launchd/ai.aoi.v6-invest-routine.plist ~/Library/LaunchAgents/ai.aoi.v6-invest-routine.plist`
  - `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.aoi.v6-invest-routine.plist`
  - `launchctl print gui/$(id -u)/ai.aoi.v6-invest-routine`
- Stop/debug:
  - `launchctl bootout gui/$(id -u)/ai.aoi.v6-invest-routine`
  - `tail -n 50 logs/launchd/v6-invest-routine.out.log`
  - `tail -n 50 logs/launchd/v6-invest-routine.err.log`

## Where to record / proof paths
- 진행중 작업: `context/handoff/HF_*.md` (기록 우선)
- 규칙/운영: 이 문서(`v6-invest_PLAYBOOK_V0_1.md`)
- 증빙 루트: `artifacts/limitless_stage0_evmax/` (재개발 완료 후), `artifacts/limitless_live_trades/`, `artifacts/limitless_autotrade_dryrun/`
- 자동화 로그: `artifacts/v6_invest_routine/` 및 `logs/launchd/v6-invest-routine.*.log`
- 운영 거버넌스: `context/handoff/HANDOFF_POLICY_V0_1.md`, `context/ops/TEAM_STATUS_DASHBOARD_V0_1.md`
