# ACP 에이전트 지갑 방식 실험 계획 v0.1

**목표:** ACP 운영에서 다양한 에이전트 지갑 레이어(Privy / Coinbase Agent Wallet / PaySponge)를 동시에 검증해, AOI Squad Pro 증빙·감사 체계와 결합 가능한 운영형 결제 분배 패턴 확립

## 1) 실험 목표
- 팀원별 개별 지갑 방식 수용성 검증 (등록→입금→분배→정산 증빙)
- 다중 지갑 프로바이더 간 실패 패턴 비교
- 중앙 풀(청묘 운영) 기준 분배 자동화 파이프라인 호환성 검증
- 0일차 기준 지표: 성공률/실패율/지연시간/증빙 누락

## 2) 실험 범위 및 참여자
- 총 대상: 11명(실험 그룹 4개)
- **Group A (Privy):** 청음, 청안, 청비
- **Group B (Coinbase Agent Wallet):** 청묘, 청검, 청섬
- **Group C (PaySponge):** 청령, 청성, 청기
- **Group D (MetaMask):** 인간-MM(휴먼-EOA-1)
- **Group E (Rabby):** 인간-RB(휴먼-EOA-2)
- **참고:** 청정은 운영 감시 및 롤백 검증 역할(분배 노드 제외)

## 3) 프로바이더별 표기 규칙 (스키마 통일)
모든 지갑 등록은 공통 스키마 사용.

```json
{
  "agentId": "청음",
  "provider": "privy|coinbase|paysponge",
  "chain": "base|solana|ethereum",
  "network": "mainnet|testnet",
  "address": "string (provider-specific)",
  "walletRef": "provider wallet id/reference",
  "currency": "USDC",
  "status": "pending|active|disabled|suspended",
  "walletProof": "did/manifest/scan file",
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### 규칙
- 개인 키를 본 시스템이 보관하지 않는다.
- 주소/계정 변경은 `disabled -> pending`로 재검증 필수.
- 지갑 등록은 실사용 전 1회 소액 tx(또는 검증값)로 유효성 확인.

## 4) 실험 플로우(1회 런)
1. **등록**: 각 멤버 지갑 정보 제출(필수: 증빙)
2. **검증**: `wallet state=active`
3. **테스트 과제 분배**: 동일 분배액(예: 100 USDC 등가)로 시뮬레이션
4. **집중 모니터링**:
   - 지갑 라우팅 성공/실패
   - 분배 tx 발생 시간
   - tx hash/receipt 수집
   - 분배 실패 사유 코드 기록
5. **정산 마감**: 각 멤버 미수령액 정산 완료 또는 `failure_code`
6. **리포트 산출**: 표준 템플릿 + 증빙 번들

## 5) 측정 지표 (KPI)
- `registration_success_rate` = 등록 성공률
- `payout_success_rate` = 분배 완료율
- `e2e_latency_ms` = 등록→분배 완료 소요 시간(평균)
- `proof_completeness` = proof_dir/input_digest/sha256/logs 충족률(필수 항목)
- `failure_rate_by_provider` = 프로바이더별 실패율(차트)

## 6) 실패 코드 정의
- `E_WALLET_INVALID_ADDR` : 주소/네트워크 불일치
- `E_WALLET_PROVIDER_UNREACHABLE` : 공급자 API/네트워크 실패
- `E_PAYOUT_TIMEOUT` : 분배 tx 미완료(지정 TTL 초과)
- `E_INSUFFICIENT_BALANCE` : 풀 잔액/수수료 부족
- `E_PROOF_MISSING` : 증빙 파일 미제출
- `E_POLICY_BLOCK` : 정책 위반(자금 이동/보안 조건)

## 7) 증빙 템플릿(필수)
각 완료/실패 건은 아래 필수 필드 채움:
- `runId`
- `Task ID`
- `provider`
- `agentId`
- `walletAddress`
- `input_digest`
- `sha256`
- `txHash`
- `status`
- `failure_code` (if any)
- `logs`
- `next_action`

## 8) 실험 종료 조건
- 모든 그룹이 1회 이상 분배 라운드를 종료
- 실패율 < 10% (그룹별), 증빙 누락 0%
- 기준 충족 시 `v0.2 운영형` 전환 승인

## 9) 운영 주의(보안)
- L3 규칙: 자금 이동/파생키 공유/외부 노출 금지, 파괴적 작업은 즉시 중단
- 월 1회 분배 규칙 감사(정산액/tx hash 대조)
- 정산은 기본적으로 청묘 오퍼레이션 승인 경로를 거침

## 10) 담당 배정
- 청묘: 운영 총괄 및 분배 실행 트리거
- 청령: 데이터 수집·집계·실패 원인 분석
- 청검: 보안 정책 + 실패 룰 리뷰
- 청안: 공지/로그 포맷 점검
- 청비: 지갑 등록증빙 저장소 관리


## 보완 규칙: MetaMask / Rabby 실험 적용
- MetaMask와 Rabby는 EOA 기반 수동 서명형 지갑이므로 분배 오퍼레이터는 `provider`를 `metamask`/`rabby`로 등록한다.
- 공통 규격은 동일: address/network/walletProof(input 주소 증빙 또는 서명 로그)/signature 또는 tx 증빙을 필수로 붙인다.
- 휴먼 계정은 1회성 소액 트랜잭션(검증 tx) 후 분배 대상 포함 여부 판단.
- 실패 처리 방식은 기존 실패 코드(`E_WALLET_INVALID_ADDR`, `E_WALLET_PROVIDER_UNREACHABLE`, `E_PAYOUT_TIMEOUT` 등)를 그대로 적용.