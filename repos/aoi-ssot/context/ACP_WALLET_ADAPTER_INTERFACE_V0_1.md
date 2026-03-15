# ACP 지갑 연동 공통 추상화 인터페이스 v0.1

**목표:** Privy / Coinbase Agent Wallet / PaySponge / MetaMask / Rabby 지갑을 **동일한 실행 계약**으로 다루어 실패 모드 비교와 분배 파이프라인 통합을 단순화.

## 1) 인터페이스 설계 원칙
- 지갑별 SDK/API 차이를 흡수하는 `WalletAdapter` 계층을 둔다.
- 모든 프로바이더는 같은 `run payload` + 같은 증빙 스키마를 반환.
- 민감정보(secret/private key)는 에이전트/오퍼레이터가 직접 보관하지 않음.
- 실패 시 공통 오류 코드 체계 사용.

## 2) 공통 스키마

### 2-1) WalletDescriptor (등록)
```json
{
  "agentId": "string",
  "provider": "privy|coinbase|paysponge|metamask|rabby",
  "chain": "base|ethereum|solana|abstract",
  "network": "mainnet|testnet|sepolia|base-sepolia",
  "address": "string",
  "walletRef": "provider wallet id / handle",
  "currency": "USDC",
  "status": "pending|active|disabled|suspended",
  "walletProof": "did/scan/manifest/txRef",
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### 2-2) RunPayload (실행요청)
```json
{
  "runId": "string",
  "recipient": "WalletDescriptor.walletRef",
  "to": "recipient address",
  "amount": "100",
  "currency": "USDC",
  "chain": "base",
  "memo": "optional",
  "requiredProof": ["input_digest","sha256","logs"]
}
```

### 2-3) ProofRecord (필수 증빙)
```json
{
  "runId": "string",
  "Task ID": "string",
  "input_digest": "string",
  "sha256": "string",
  "proof_dir": "/tmp/aoi_squad_pro_run_.../",
  "logs": ["/tmp/.../run.log", "/tmp/.../tx.log"],
  "txHash": "string optional",
  "status": "DONE|BLOCK|NEEDS_SUPPORT",
  "failure_code": "optional",
  "suggested_fix": "optional"
}
```

## 3) 공통 인터페이스 (메서드)

모든 어댑터가 아래 함수 형태를 가진다:

- `connect(agentWalletDescriptor): ConnectResult`
- `validate(descriptor): bool`
- `preparePayout(payload): PrepareResult`
- `sendPayout(payload): SendResult`
- `checkStatus(txHash): TxStatus`
- `rollbackOrRevert(runId): RollbackResult`
- `getAdapterMeta(): AdapterMeta`

### 반환 형식(권장)
```json
{
  "ok": true,
  "provider": "coinbase",
  "providerRunId": "providerSpecificId",
  "txHash": "optional",
  "proofHint": "path or ref",
  "error": {
    "code": "E_PAYOUT_TIMEOUT",
    "message": "..."
  }
}
```

## 4) 오류 코드 공통화
- `E_WALLET_INVALID_ADDR`
- `E_WALLET_PROVIDER_UNREACHABLE`
- `E_PAYOUT_TIMEOUT`
- `E_INSUFFICIENT_BALANCE`
- `E_APPROVAL_REQUIRED`
- `E_CHAIN_MISMATCH`
- `E_PROOF_MISSING`
- `E_RATE_LIMIT`
- `E_POLICY_BLOCK`

## 5) 프로바이더별 최소 연결 전략 (우선순위)

### A) Privy
- 장점: 계정/온보딩 자동화 쉬움
- 연결 전략: 계정 토큰 기반 세션 + 지갑 주소 조회 → 소액 검증 tx
- 리스크: 사용자 계정 상태/권한 확인 실패

### B) Coinbase Agent Wallet
- 장점: AI 에이전트 결제/지불 컨텍스트와 호환성
- 연결 전략: 지갑 ID 기반 등록 → 지급 트랜잭션 실행 상태 점검
- 리스크: API 정책/권한 범위 차이

### C) PaySponge
- 장점: 결제형 UX, 실시간 수익/정산 시나리오 검증 유리
- 연결 전략: 결제/받기 흐름 먼저 샌드박스 검증
- 리스크: 지갑 계정 식별 키 포맷 정합성

### D) MetaMask
- 장점: 범용성, 사용자 접근성 높음
- 연결 전략: `provider=metamask`로 등록 후 수동 서명(테스트 tx) 증빙
- 리스크: 브라우저 환경 의존

### E) Rabby
- 장점: EOA 제어형 테스트, 수동 서명 경로 검증
- 연결 전략: MetaMask와 동일 패턴, 지갑별 서명 로그/주소 증빙
- 리스크: 자동화 제약(수동 승인 단계)

## 6) 실행 우선순위 로드맵
- **Phase 1:** Privy/Coinbase/PaySponge 1차 구현
- **Phase 2:** MetaMask/Rabby EOA 경로를 `manual_sign` 모드로 병행
- **Phase 3:** 공통 어댑터에 provider별 리트라이 정책 탑재

## 7) 운영 템플릿(공통)
- 실행 직후: `status=DONE`이면 `txHash`, `proof_dir`, `input_digest`, `sha256`, `logs` 필수
- 실패면: `failure_code`, `suggested_fix`, `retry_at` 필수
- 지갑 변경: `disabled -> pending` 후 검증 재진입

---

## 8) 샘플 코드
- 로컬 실행용 타입/인터페이스 스텁: `scripts/acp_wallet_adapters_stub.ts`
- 공급자별 `connect/validate/send` 시그니처를 동일하게 맞춰, API 호출만 TODO 교체 가능

---

> 참고: 본 인터페이스는 API 키/엔드포인트 고정이 아니라 **시험 운영용 표준 계약**이다. 공급자별 인증 및 서명 규칙은 추후 API 탐색 결과로 `provider adapter` 파일에서 오버라이드한다.