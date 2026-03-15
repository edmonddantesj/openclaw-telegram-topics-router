# AOI_PERMISSION_SCOPE_V0_1

## 목표
AI가 직접 실행 가능한 작업을 **최소 권한 원칙**으로 제한하는 권한 명세를 정의한다. AOI Core에서 권한을 `scope`로 바인딩해 사고 확산을 막고, 긴급 취소 경로를 보장한다.

## 적용 범위
- AOI Council 기반 제안/실행 트랜잭션 생성
- 오케스트레이터가 외부 스킬/스마트컨트랙트 호출을 유도할 수 있는 위치
- v0.1: 오프체인 정책 평가와 실행 의도 서술에 한정 (온체인 enforcement는 확장 단계)

## 권한 모델
### Scope 오브젝트
```json
{
  "permission_id": "perm-...",
  "subject": "agent_id or user_id",
  "audience": "skill|contract|api",
  "target": "string",
  "action": "read|propose|execute|approve",
  "method": "http|contract_method|cli_command",
  "constraints": {
    "max_amount": "optional amount",
    "max_value_usd": 500,
    "allowed_networks": ["bsc", "opbnb", "base"],
    "allowed_contracts": ["0x..."],
    "allowed_methods": ["transfer", "vote", "propose"],
    "ttl_seconds": 3600,
    "single_use": false,
    "rate_per_minute": 20
  },
  "state": "active|paused|revoked|expired",
  "revocation": {
    "revoked_by": "user|admin",
    "revoked_at": "ISO8601"
  },
  "not_before": "ISO8601",
  "expires_at": "ISO8601"
}
```

## 핵심 규칙
1. 기본 상태는 권한 없음 (`default deny`).
2. 모든 실행 제안은 적어도 하나의 유효한 `permission` 매칭 필요.
3. `single_use=true` 권한은 한 번 소비 후 비활성.
4. TTL 만료, revoked, paused면 즉시 실행단에서 거절.
5. 예외/이상치(권한 미스매치, 만료, 금지 네트워크/메소드) 기록은 자동 감사 이벤트로 남김.

## 실행 판정 상태
- `permission_status`: `GRANTED / DENIED / EXPIRED / REVOKED / NOT_FOUND / OUT_OF_SCOPE`
- `enforcement`: `allow|hold|deny`

## 에러 코드
- `PS-001`: Permission missing
- `PS-002`: Permission expired
- `PS-003`: Permission revoked
- `PS-004`: Scope mismatch (target/action/method)
- `PS-005`: Amount/cost exceeds limit
- `PS-006`: Rate limit exceeded

## 테스트 케이스 (v0.1)
1. **TC-PERM-01** 유효 권한으로 in-scope execute => GRANTED
2. **TC-PERM-02** 만료된 권한 => EXPIRED + deny
3. **TC-PERM-03** 허용 목록 외 컨트랙트 호출 => OUT_OF_SCOPE
4. **TC-PERM-04** single_use 재사용 시도 => REVOKED/EXHAUSTED
5. **TC-PERM-05** 금액 초과 => deny + PS-005
6. **TC-PERM-06** 권한 취소 중재자 호출 => immediate deny

## 구현 인터페이스(권장)
- 정책/권한 저장: `~/.aoi/permissions/*.json` 또는 `aoi-core/state/permission_registry.json`
- 조회/검증 API: `POST /api/permissions/inspect`
- 취소 API: `POST /api/permissions/revoke`
- 감사 로그: `permission_events.ndjson` or JSONL

## AOI 통합 지점
- council_pro_adapter 실행 직전: 제안된 `action_intent`를 Scope로 치환 후 검사
- web_pilot/CLI에서 `policy.gate` 결과와 함께 노출
- `manifest`에 `permission_audit`: `{permission_id, status, matched_rule, denied_reason}` 추가

## 통제 전략
- 첫 판에서는 실사용 커넥터별 전체 권한 대신 최소 세트(읽기 전용 + 제안 생성)만 허용
- 자동 실행은 L3에서 기본차단(수동 승인 없으면 deny)

