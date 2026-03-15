# AOI Core — Brand/Whitepaper/Pillars Alignment Map v0.1 (SSOT)

Last updated: 2026-02-20 (KST)
Owner: Edmond (PO)
Status: DRAFT (consolidated)

> Purpose: 제품명 확정 전에, AOI 철학/브랜드(Chungho/청교), 백서/라이트페이퍼 주장, 플랫폼 현실(SSOT+코드), 7대 메인 테마를 **한 장의 정합성 지도**로 맞춘다.

## Inputs (TFT drafts)
- Brand system: `context/strategy_tft/aoi_core_brand_alignment/BRAND_SYSTEM_SSOT_V0_2_DRAFT.md`
- 7 pillars audit: `context/strategy_tft/aoi_core_brand_alignment/SEVEN_PILLARS_AUDIT_V0_1_DRAFT.md`
- Gap matrix: `context/strategy_tft/aoi_core_brand_alignment/WHITEPAPER_PLATFORM_GAP_MATRIX_V0_1_DRAFT.md`

## SSOT anchors
- `context/AOI_CORE_PRODUCT_VISION_V0_1.md`
- `context/AOI_CORE_MVP_SCOPE_V0_1.md`
- `context/BRAND_AOI_CHUNGHO_SSOT_V0_1.md`
- `context/SSOT_INDEX.md`

---

# 1) Brand Architecture (Locked)
## 1.1 Relationship stack (canonical)
- Aoineco (회사/운영자) → AOI(표준/철학) → AOI Core(운영 OS) → CHUNGHO(우산 심볼/고유명사 모티프) → Blue Bridge/청교(2차 모티프)

## 1.2 Hard rules (ship gate)
- CHUNGHO 표기: **CHUNGHO(ALL CAPS)**
- 최초 1회만: **CHUNGHO (Blue Tiger)**, 이후 CHUNGHO만
- 청교(靑橋) 단어 남발 금지 → 이미지/카피 1줄 악센트만
- 과장/수익 보장/알파 보장 문구 금지

## 1.3 Exposure tier mapping (OPEN/TEASER/STEALTH/TOP SECRET)
- OPEN: AOI 정의 + AOI Core 운영 언어(Policy→Gate→Approval→Proof) + proof demos
- TEASER: Bazaar/Guardian T1-2/ Core-Temp/ Squad Pro modules
- STEALTH: S‑DNA handshake 상세, Omega Fusion 파라미터, Skill Aggregator 로직, Survival 수익모델 상세
- TOP SECRET: $AOI tokenomics/treasury/wallets

---

# 2) Whitepaper ↔ Platform Gap Top10 (Fix list)
> 기준: 사용자 신뢰/보안/브랜딩 리스크가 큰 것부터.

1) **Stealth $AOI vs Litepaper 공개 토큰 문구** (TOP SECRET)
- Gap: conflict
- Fix: Litepaper를 internal-only로 내리거나, Stealth rule을 재정의(권장: internal-only 유지)

2) **“✅ Complete” 로드맵 주장 vs MVP(vNext) 문서 충돌**
- Gap: conflict
- Fix: “코드는 internal skill로 존재하되, productized shipping은 vNext”로 문구 정렬

3) **S‑DNA Layer3 ‘proprietary’ vs 코드 존재** (STEALTH)
- Gap: conflict
- Fix: public-safe wrapper만 공개 + secrets/handshake params는 vault/STEALTH로 분리

4) **Monte Carlo / Self-Reflection 엔진 운영 언어 강함 vs 증빙/데모 부족**
- Gap: missing-code 또는 missing-doc
- Fix: 데모 proof bundle + 재현 커맨드가 없으면 WP를 methodology로 다운그레이드

5) **Naming drift: AOI Core vs Nexus Protocol vs AI DEX vs Bazaar**
- Gap: missing-doc
- Fix: 용어 매핑표 1페이지(동의어/하위모듈/비전)를 SSOT로 고정

6) **Brand-Genesis / Smart-Manager는 가격/오퍼가 있는데 SSOT 산출물 정의가 없음**
- Gap: missing-doc
- Fix: 1페이지 SSOT 2개 생성(스코프/출력스키마/거버넌스/증빙)

7) **Guardian/Sentry를 publish gate로 강제하는 실행 증빙 부족**
- Gap: missing-doc
- Fix: Guardian report artifact + Security Gate checklist를 release gate에 연결

8) **Core-Temp(평판) ‘운영’ 주장 vs 구현 근거 부족**
- Gap: missing-code
- Fix: 개념 유지(TEASER) 또는 계산 로직+증빙을 먼저 구현

9) **Settlement/x402/royalty 레이어의 스키마 표준화 부족**
- Gap: missing-doc
- Fix: ledger schema + statement generator + proof bundle 연결(현재 B-min 일부 존재)

10) **Public claims registry 부재**
- Gap: missing-doc
- Fix: OPEN/TEASER claim → evidence path → demo command registry를 SSOT로 추가

---

# 3) 7 Pillars Audit — “증빙 산출물” 표준화 (Cross-pillar fix)
## 3.1 공통 갭
- 정의/히스토리는 강함.
- 하지만 플랫폼 수준에서 pillar별로 **proof bundle에 붙는 표준 산출물(JSON/MD/Report)**이 통일되지 않음.

## 3.2 공통 해결책 (단일 스키마)
- 각 pillar는 최소 1개 artifact를 의무 생성:
  - `<pillar>_report.json`
  - `<pillar>_notes.md`
  - `sha256sum.txt`

## 3.3 Pillar별 “다음 액션” 1줄
- S‑DNA: public-safe spec + restricted spec 분리 + verify CLI
- Guardian: tier spec + guardian_report.json 표준화
- Context‑Sentry: spec + compression decision artifact
- Ω Oracle: oracle_verdict.json + calibration proof
- Bazaar: mechanics spec + core-temp rules + settlement schema
- Survival: ratio calc spec + revenue/cost proof
- Stealth: exposure tier matrix + publish enforcement

---

# 4) Immediate Work Queue (48h)
1) Write `context/EXPOSURE_TIER_MATRIX_V0_1.md` ✅ (draft created)
2) Write `context/NAMING_MAPPING_TABLE_V0_1.md` (AOI Core / Nexus / Bazaar / AI DEX) ✅ (draft created)
3) Create Brand-Genesis SSOT + Smart-Manager SSOT (1-page each) ✅
   - `context/BRAND_GENESIS_PRODUCT_SSOT_V0_1.md`
   - `context/SMART_MANAGER_PRODUCT_SSOT_V0_1.md`
4) Define Proof Artifact schema per pillar (v0.1) ✅
   - `aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`

---

## Evidence
- TFT folder: `context/strategy_tft/aoi_core_brand_alignment/`
