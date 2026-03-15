# $7 Project (Limitless + Meteora DLMM) — Key Points v0.1

## Source
- Raw dump: `context/7DOLLAR_LIMITLESS_METEORA_DISCUSSION_DUMP_2026-02-16_17_V0_1.txt`

## 1) What was missing initially
- ‘$7 프로젝트 수익률(%)’은 **온체인 증빙/스냅샷/자동 집계가 없어서** 정확 계산이 불가한 상태로 시작.
- Supabase의 “매시간 기록”도 실제로는 **2/11(UTC)에서 멈춰있었음**.

## 2) Supabase predictions 기록(매시간) — 복구 결정
- 테이블: `public.predictions`
- 운영 규칙(당시 합의):
  - 매시간 **:50** V6 판단
  - 매시간 **:52** V6 결과를 predictions에 insert
  - 매시간 **:00** shadow settle(10분 후)로 is_win/pnl 업데이트
- 중단 원인: `vault/supabase.env` 부재로 env 로드 실패.
- 해결: `vault/supabase.env` 채우고 1건 insert 성공 확인(총 row 증가).

## 3) Limitless 자동 투자 운영 룰
- 목표: Limitless hourly market에서 BTC 종목 LONG/SHORT/HOLD를 V6로 판단.
- 합의된 단계:
  - 48시간 **Shadow 모드(시뮬/복기)**
  - 이후 성과 보고 후 자동 LIVE 진입
- 베팅 하드캡: **$1 per bet**
- Kill-switch 필요(자동 기본이라도 최소한의 안전 플래그/연속 손실 중단 등).

## 4) Wallet/keys (sensitive)
- Base(EVM) 지갑을 실험 지갑으로 사용.
- private key / api key는 채팅에 재노출 금지. vault 파일에 존재 여부만 확인.
- (채팅 요약에서는 주소/해시 마스킹; SSOT/Notion에만 원문 보관)

## 5) Gas management: USDC→ETH 자동 탑업(자동화)
- 트리거: ETH < MIN_ETH (예: 0.001)
- 목표: TARGET_ETH (예: 0.003)
- 하드캡: MAX_SWAP_USDC=1, MAX_SWAPS_PER_DAY=1
- DEX 선택: **Aerodrome(Base)**
- 안전 설계:
  - fail-closed (애매하면 스왑 안 함)
  - 자동 approve 금지 → **USDC approve는 사전 1회 수동**
- 구현 스크립트(뼈대):
  - `scripts/auto_gas_topup_aerodrome.mjs`
  - `scripts/approve_usdc_aerodrome_router.mjs`

## 6) Diversified yield loop: Base↔Solana(deBridge) + Meteora DLMM
- 전략 구조(합의):
  - Base(Limitless) = 공격(알파)
  - Solana(Meteora DLMM) = 수비(수수료/현금흐름)
- 핵심 리스크: 브릿지 실수/비용/복잡도 증가.
- 팀 합의안(초소액 최적):
  - 초기 배분: **DLMM 80% / Base 20%**
  - Base 상한: 50% (당분간)
  - 브릿지: 덩어리로 가끔(2~3일 1회 or 주 1회), Canary 필수
  - default OFF + fail-closed + allowlist + staging + 지갑 분리
- 미결정(필수 결정 2개):
  - 브릿지 목적 자산: Solana USDC 착지 vs SOL 착지
  - 브릿지 트리거: (A) 주기 고정 (B) USDC 임계치 초과분 비율 (C) Shadow 성과 게이트

## 7) Remaining gaps for true ROI(%)
- ‘$7 수익률’은 predictions(예측 로그)만으로는 계산 불가.
- Meteora DLMM 포지션/수수료/클레임을 **스냅샷/아티팩트**로 누적해 PnL 계산 루프가 필요.
