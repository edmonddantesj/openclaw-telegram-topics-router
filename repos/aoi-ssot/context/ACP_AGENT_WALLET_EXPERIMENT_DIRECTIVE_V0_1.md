# AOI Squad Pro — ACP 에이전트 지갑 실험 즉시 시행 지시문 (v0.1)

## 목적
`ACP_AGENT_WALLET_EXPERIMENT_V0_1.md`를 실행 단계로 전환한다.

## 1) 청묘(오퍼레이터) 즉시 실행 지시
- 본문 공지: 실험 대상 총 11명(운영 노드 제외 1명) 기준 시행
- 그룹은 5개로 운영: A/B/C(기존) + D/ E(휴먼 지갑 2명)
- 10분 이내 응답 수집, 미응답은 재요청 1회
- 공통 필수 제출: `Task ID`, `provider`, `agentId`, `walletAddress`, `walletProof`, `input_digest`, `sha256`, `logs`

```text
AOI Squad Pro: 에이전트 지갑 실험 즉시 실행
그룹별 방식:
- Group A(Privy): 청음/청안/청비
- Group B(Coinbase): 청묘/청검/청섬
- Group C(PaySponge): 청령/청성/청기
- Group D(MetaMask): 인간-EOA-MM
- Group E(Rabby): 인간-EOA-RB

10분 내 다음 템플릿으로 회신
- Task ID:
- provider:
- agentId:
- status: DONE/BLOCK/NEEDS_SUPPORT
- walletAddress:
- walletProof:
- input_digest:
- sha256:
- logs:
- failure_code:
- suggested_fix:

규칙:
- 증빙 미기재면 DONE 금지(BLOCK)
- L3 항목(자금 이동/키 유출/파괴작업) 발견 시 즉시 중단 + 경보
- 완료 시 txHash와 정산 증빙 첨부
```

## 2) 청령(총괄) 즉시 실행 지시
- 수집 규칙
  - 제출 미완/미응답 1회=재요청
  - 2회 미응답=그룹 상태 BLOCK + 대체 슬롯 이동
- 집계 라인: 총건/Done/Block/Needs Support/증빙누락/실패코드
- 최종 판정: 실험 1회전 완료 후 `v0.2 운영형` 권고 여부

## 3) 청렴(확인) 규칙
- `proof_dir`, `input_digest`, `sha256`, `logs` 미제출 = 자동 BLOCK
- `failure_code` + `suggested_fix` 동반 제출 필수
- 지갑 변경은 `disabled -> pending` 재승인 루트만 허용

## 4) 분배 오퍼레이션(청묘)
- 중앙풀 기준 동일 액면(예: 100 단위) 시나리오로 분배 실행
- 실패건은 즉시 원인 분류(E_*) 후 다음 라운드 재시도

## 5) 종료 후 산출물
- `runs` 로그, KPI 표, 실패 패턴, provider별 성공률 비교표
- 다음 단계: `ACP_AGENT_WALLET_EXPERIMENT_V0_2_OPERATIONAL` 작성


## 6) 청령 집계 템플릿(복붙)

```text
[AOI Squad Pro 1차 지갑 실험 집계]
총 대상: 11명(분배대상 10명, 청정 감시 모드)
시작: {start_time} / 종료: {end_time}

| 구분 | agentId | provider | Task ID | 상태 | walletAddress | proof_dir | sha256 | 입력 증빙(input_digest) | logs | 실패코드 | 제안조치 | 증빙 누락 여부 | 다음 액션 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Privy-01 | 청음 | privy | | DONE/BLOCK/NS | | | | | | | | 0/1 | |
| Privy-02 | 청안 | privy | | DONE/BLOCK/NS | | | | | | | | | |
| Privy-03 | 청비 | privy | | DONE/BLOCK/NS | | | | | | | | | |
| Coinbase-01 | 청묘 | coinbase | | DONE/BLOCK/NS | | | | | | | | | |
| Coinbase-02 | 청검 | coinbase | | DONE/BLOCK/NS | | | | | | | | | |
| Coinbase-03 | 청섬 | coinbase | | DONE/BLOCK/NS | | | | | | | | | |
| PaySponge-01 | 청령 | paysponge | | DONE/BLOCK/NS | | | | | | | | | |
| PaySponge-02 | 청성 | paysponge | | DONE/BLOCK/NS | | | | | | | | | |
| PaySponge-03 | 청기 | paysponge | | DONE/BLOCK/NS | | | | | | | | | |
| MetaMask | 인간-EOA-MM | metamask | | DONE/BLOCK/NS | | | | | | | | | |
| Rabby | 인간-EOA-RB | rabby | | DONE/BLOCK/NS | | | | | | | | | |
| 운영감시 | 청정 | n/a | - | - | - | - | - | - | - | - | - | 상태 이상 감시/롤백 검증 전용 |

요약:
- DONE: {count}
- BLOCK: {count}
- NEEDS_SUPPORT: {count}
- proof_dir 누락: {count}
- input_digest 누락: {count}
- sha256 누락: {count}
- logs 누락: {count}
- 실패 코드 Top3: {codes}
- 평균 제출 소요: {sec}
- 다음 액션:
  - BLOCK 항목 재요청 (1회)
  - 실패 반복 항목은 그룹별 리프트오프 여부 판단
  - 통과 기준 충족 시 v0.2 운영형 전환
```
