# MAINTENANCE_LAUNCHD_AUDIT_REPORT_2026-03-08_V0_1

Scope: macOS launchd + OpenClaw cron/heartbeat 관련 주요 주기작업

## Executive summary
- launchd(plist) 기반 주기작업 다수가 **로드됨** 상태.
- 핵심 리포트(3h digest)와 notion digest는 **최근 proof artifact 존재**로 PASS.
- 일부 job은 `ProgramArguments`가 **agents/oracle/work/... 경로**를 가리켜 SSOT durability 관점에서 경로/권한 리스크가 있어 추후 정리 권장.

## Jobs (PASS/FAIL)

### 1) ai.aoi.maintenance_digest_3h — PASS
- Schedule: 00:01/03:01/06:01/09:01/12:01/15:01/18:01/21:01 KST
- Program: `_tg_alert_on_fail.sh maintenance_digest_3h env python3 scripts/maintenance_digest_3h.py`
- Loaded: `launchctl list` shows `ai.aoi.maintenance_digest_3h` (exit status present)
- Recent proof:
  - `artifacts/digest/digest_20260308_090116.txt`
  - `artifacts/digest/digest_20260308_070209.txt`

### 2) ai.aoi.notion_sync_digest_am_pm — PASS
- Schedule: 08:50 / 20:50 KST
- Program: `_tg_alert_on_fail.sh notion_sync_digest env python3 scripts/notion_sync_digest.py`
- Loaded: present in `launchctl list`
- Recent proof:
  - `artifacts/notion_digest/notion_sync_digest_20260308_085004.txt`

### 3) ai.aoi.knowledge_index_digest_0901 — CHECK
- Schedule: 09:01 KST
- Program: `_tg_alert_on_fail.sh knowledge_index_digest_0901 env python3 scripts/knowledge_index_digest.py`
- Loaded: present in `launchctl list`
- Proof: (이번 감사에서 파일 존재 확인을 아직 안 함) → 다음 run artifact 경로 확인 필요

### 4) ai.aoi.maintenance_daily_smoke — CHECK
- Schedule: 09:10 KST
- Program: `_tg_alert_on_fail.sh maintenance_daily_smoke scripts/maintenance_daily_smoke.sh`
- Loaded: present in `launchctl list`
- Proof: (이번 감사에서 파일 존재 확인을 아직 안 함) → 다음 run log artifact 경로 확인 필요

### 5) ai.aoi.ralph_loop_daily_scan_2300 — CHECK
- Schedule: 23:00 KST
- Program: `_tg_alert_on_fail.sh ralph_loop_daily_scan_2300 env python3 scripts/ralph_loop_daily_scan.py`
- Loaded: present in `launchctl list`
- Proof: 금일 23:00 이후 생성될 것(시간상 미도래)

### 6) ai.aoi.ralph_loop_sync_hourly — CHECK (path risk)
- Schedule: StartInterval=3600 (hourly)
- Program: `/bin/bash agents/oracle/work/aoi-md-vault/scripts/cron/ralph_loop_sync_hourly.sh`
- Loaded: present in `launchctl list`
- Risk: Program 경로가 `agents/oracle/work/...` 하위로 고정되어 있어, agents workspace 정리/변경 시 깨질 수 있음.

### 7) ai.aoi.state_snapshot_upload_daily — PASS (observed manual runs)
- Schedule: 09:20 KST
- Program: `/bin/bash agents/oracle/work/aoi-md-vault/scripts/cron/state_snapshot_upload_daily.sh`
- Loaded: present in `launchctl list`
- Recent proof (manual SAVE NOW runs):
  - GitHub release `state_snapshot__20260308_075804`
  - local tar: `artifacts/state_saves/state_snapshot__20260308_075804.tar.gz`
- Note: daily schedule run은 09:20 이후 proof 확인 가능

## Known issue
- `md-vault` push가 remote ahead로 reject되는 케이스가 관측됨. 스냅샷 업로드(`aoi-state-saves`)는 정상.

## Next actions
1) knowledge_index_digest / daily_smoke 의 proof artifact 경로를 SSOT에 명시 + PASS 확인
2) `agents/oracle/work/...`에 걸린 launchd ProgramArguments를 workspace의 안정 경로(`scripts/`/`context/automation/launchd/`)로 정리
