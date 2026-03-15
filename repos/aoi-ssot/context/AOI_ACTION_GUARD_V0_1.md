# AOI_ACTION_GUARD_V0_1

## 목표
AOI Council 실행 전, 요청을 위험도 기준으로 분기 처리하는 전역 가드 레이어를 정의한다. 실행은 `ALLOW / REVIEW / BLOCK`의 3단계로 분류하며, AOI Core의 L1/L2/L3 정책 체계를 강제한다.

## 적용 범위
- 대상: AOI Council (프로덕트 공통), pilot/CLI/agent-runner의 모든 오케스트레이션 엔트리
- 현재 단계: 논리 스키마 + API/리포트 연동(오프체인) v0.1
- 제외: 실시간 on-chain 집행(개별 커넥터/스킬 계층), 결제/체결 모듈

## 핵심 규칙
1. `mode=pro`는 기본값 `conditional`이며 L3 요청(돈/지갑/온체인 서명/외부게시/irreversible)에서 무조건 `REVIEW` 이상.
2. `risk_score >= 80` 또는 정책 `hard_block=true`이면 `BLOCK`.
3. `risk_score >= warn_threshold`이면 `REVIEW`.
4. `policy_adjustments`가 존재하면 `REVIEW` 우선 처리(설정 위반 리스크가 낮아도).
5. 모든 결과는 `evidence` 항목에 추적 가능 경로 포함(`evidence_id`, `policy_profile`, `policy_version`, `policy_score_snapshot`).

## 입출력 스키마

### Input (AOI run wrapper)
```json
{
  "run_id": "council_...",
  "topic": "string",
  "mode": "lite|pro",
  "context": "string",
  "constraints": "string",
  "metadata": {
    "caller": "uuid|user",
    "source": "web|cli|api",
    "pro_access": "off|request|direct",
    "profile": "default|..."
  },
  "evidence": {
    "inputs_hash": "sha256:...",
    "artifact_paths": ["..."],
    "previous_run_id": "optional"
  }
}
```

### Output
```json
{
  "ok": true,
  "run_id": "...",
  "decision": "ALLOW|REVIEW|BLOCK",
  "risk_score": 0,
  "risk_band": "low|medium|high|critical",
  "policy_profile": "conservative|default|experimental",
  "policy_version": "AOI_COUNCIL_POLICY_ENGINE_PROFILE_*.json",
  "checks": [
    {"name":"policy_score", "result":"pass|warn|fail", "value": 72},
    {"name":"constraint_scan", "result":"pass|warn|fail", "detail":"..."}
  ],
  "evidence": {
    "evidence_id": "ag-YYYYMMDD-HHMMSS-xxxx",
    "policy_score_snapshot": {
      "summary_score": 72,
      "warn_threshold": 55,
      "block_threshold": 80
    }
  },
  "next_actions": [
    "run_council", "require_human_review", "notify_admin"
  ]
}
```

## 에러 코드
- `AG-001`: Missing policy profile
- `AG-002`: Invalid risk profile schema
- `AG-003`: Policy checker timeout
- `AG-004`: Evidence write failure
- `AG-005`: Policy deny (hard block)

## 의사결정 규칙 우선순위 (우선순위 높은 순)
1. L3 금지 규칙(외부 지갑 서명/판매/온체인 실행/irreversible)
2. 정책 hard block
3. 위험 점수 임계치
4. 검토 대상 정책 조정
5. 기본 게이트

## 테스트 케이스 (v0.1)
1. **TC-ACT-01 ALLOW:** 저위험 토픽 + 기본 제약, policy_profile=default => ALLOW
2. **TC-ACT-02 REVIEW:** 중간위험 + 사용자 제약 존재 => REVIEW
3. **TC-ACT-03 BLOCK:** high risk 또는 hard_block=true => BLOCK
4. **TC-ACT-04 PRO-L3:** mode=pro, constraints에 L3 항목 포함 => REVIEW
5. **TC-ACT-05 SCHEMA_FAIL:** 잘못된 profile 버전 => AG-001
6. **TC-ACT-06 TIMEOUT:** 정책 엔진 타임아웃 시 BLOCK fallback => AG-003

## 통합 포인트
- `repos/aoi-ssot/scripts/aoi_council_run.py`의 `_policy_check` 결과 소비 전단.
- `repos/aoi-ssot/scripts/council_web_pilot.py` 폴링 응답 필드 `policy`/`verdict`에 `decision`, `risk_score`, `evidence_id` 노출.
- `context/AOI_COUNCIL_POLICY_ENGINE_CONFIG_V0_1.json`의 threshold 값을 source-of-truth로 참조.

## 리스크(안전) 메모
- 보수적으로 보수: 정책 조회 실패는 **Fail-closed**로 처리
- 리스크 점수만으로 자동 실행하지 않음(최소 1개 정책 사유/근거 필요)

