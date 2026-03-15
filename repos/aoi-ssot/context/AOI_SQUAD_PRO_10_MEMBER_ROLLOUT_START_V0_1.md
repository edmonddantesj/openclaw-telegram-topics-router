# AOI Squad Pro 10인 롤아웃 실행 시작안 (v0.1)

일시: 2026-02-19 19:21 KST (User-initiated)
상태: **실행 중**

## 0) 목표
- AOI Squad Pro를 10인 체계로 전원 확장한다.
- Notion 대시보드 실 데이터(역할/감정/태스크 기반)를 내부 표기와 정합한다.
- 승인/실행/증빙 흐름을 즉시 일관된 포맷으로 고정한다.

---
## 1) 10인 핵심 슬롯(현재 Notion 기준)
1) 🧿 청령 (Oracle) — Chief of Staff / VCP 검증 및 링크 Assert / Project Oracle / Logic, Reasoning
2) 📢 청음 (Blue_Sound) — Community/Artist / 봇마당/X 복구 포스팅 / Diplomatiq Sound
3) 🛡️ 청검 (Blue-Blade) — Security Guard / 지갑 보호 및 카나리 감시 / prompt-guard
4) 🗂️ 청비 (Blue-Record) — Knowledge Master / 장애 기록 및 칸반 업데이트 / Knowledge Record
5) ⚡ 청섬 (Blue-Flash) — Builder / 해커톤 최종 제출물 검수 / Action Flash
6) 👁️ 청안 (Blue-Eye) — Scout / 신규 스킬 정찰 및 시장 분석 / Market Eye
7) 🧠 청뇌 (Blue-Brain) — Strategist / V7 수익 모델 및 지갑 설계 / OMNIA Ω
8) ⚙️ 청기 (Blue-Gear) — DevOps/Sentry / API 엔드포인트 감시 및 인프라 / Infra Gear
9) 📈 청성 (Blue-Growth) — Marketer / X 전략 및 유저 획득 / Growth Matrix
10) 🧰 청정 (Blue-Maintainer) — Maintenance Engineer / Daily smoke tests + 회귀 triage / Stability Wrench

---
## 2) 역할 라우팅 (Pro pipeline mapping)
**기본 Preset A:** `Planner -> Researcher -> Builder -> Reviewer -> Operator`

- 청령: Planner
- 청안/청성: Researcher(보조)
- 청섬: Builder
- 청비/청검/청뇌: Reviewer (+ 청검은 Security 라우팅 우선)
- 청기/청정: Operator

**Preset B (콘텐츠/보안 혼합):** `Researcher -> Writer -> Builder -> Security -> Operator`

---
## 3) 즉시 시행(First 2 hours)
### 3.1 Notion 데이터 정합 마무리
- [ ] `skills/aoi-squad-pro` 소유 문서에 위 10명 슬롯/맵핑 반영
- [ ] 승인/런타임/증빙 필수 필드( input_digest, version, runtime, generated_at, evidence ) 정책 고정
- [ ] `Notion Dashboard` 변경 시 API fallback 경로 점검(페이지/블록 읽기 쿼리)

### 3.2 ACP 운영 리스크 차단
- [ ] `acp job create` 500 원인 캡처
- [ ] `Unsupported action: probe` 대응 룰시트 작성
- [ ] 외부 job 유입시 runId/proof_dir/sha256 자동 캡처 템플릿 적용

### 3.3 커뮤니티/포스팅 안정성 체크
- [ ] Botmadang/Moltbook 포스팅 payload 필수 필드(제목·검증 흐름) 고정
- [ ] 최근 실패 케이스 대비 재시도 정책 적용

---
## 4) 실행 체크포인트 (3개 트랙)
1. **팀 롤아웃 트랙(10인 확장)**: 2~3명 파일럿 → 10명 확대
2. **ACP 실매출 트랙(안정성)**: 내부 500/Unsupported 재현→패치 또는 우회
3. **Grant/해커톤 트랙**: Base/KALE outcome 수신 캡처 + 즉시 증빙 업데이트

---
## 5) 10분 스타트 가이드 (채팅 복붙용)
1) 오늘 대상 슬롯 10개 확인
2) `approve -> run -> proof` 템플릿 열기
3) 첫 태스크 1개씩 배정(각 5분)
4) 증빙 경로를 동일하게 남김
   - `/tmp/aoi_squad_pro_run_<ts>/input.json`
   - `/tmp/aoi_squad_pro_run_<ts>/proof.json`
   - `/tmp/aoi_squad_pro_run_<ts>/proof.sha256`
5) 실패시 즉시 `failure_code` + `suggested_fix` 남김

---
## 6) 완료 기준
- 10인 슬롯 100% 승인 룰 반영 완료
- 오늘 생성한 작업 1건 이상이 `run/proof` 증빙 경로에 남음
- Notion 접근 이슈 발생시에도 API로 최소 역할/담당 상태 조회 가능
- ACP 자기 오퍼(job create) 500/unsupported 대응 문서화 완료

---
## 7) 즉시 실행할 다음 지시
- 다음 응답에서 바로: **전문담당 1차 배치표 + 1회차 실행 템플릿**을 각자에게 배포한다.
