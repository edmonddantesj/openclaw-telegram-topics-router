# TASK_PARKING_LOT.md (SSOT)

이 문서는 "지금은 보류"된 작업들을 한 곳에 모으는 Parking Lot SSOT다.
- 원칙: 재개 시점에 필요한 **정확한 트리거/체크리스트/첫 커맨드**를 함께 적는다.
- 외부 게시/업로드/커밋은 별도 승인 게이트.

---

## deferred-bundle-2026-02-16

### BNB GoodVibes DEX Agent  (tag: bnb-goodvibes-video)
- Status: ✅ SUBMITTED (DONE)
- Progress:
  - BNB hackathon 제출 완료 (영상/링크 확정)
- Evidence:
  - YouTube demo: https://youtu.be/pRaU3KDAxxM
  - Local final video: `bnb-goodvibes-demo-final-60s.mp4`
- Needs from Edmond:
  - 기본: 영상 제출/업로드/링크 확정
  - (조건부) 키 재입력은 "tx proof 재런"이 필요할 때만
- Resume trigger:
  - 제출 폼 최종 입력/제출 필요 or 영상 링크/메타데이터 수정 필요
- Resume first command:
  - (필요 시) `cd bnb-goodvibes-dex-agent && cat manifest.json`

### Midl VibeHack  (tag: midl-vibehack-home)
- Status: PARKED
- Progress:
  - 빌드/증빙/데모 단계가 "집에서만 가능한 액션" 때문에 중단(대화 기록 기반)
- Needs from Edmond:
  - 집/안전환경에서 Xverse extension 연결 가능
  - 1 on-chain action 실행
- Resume trigger:
  - "집 도착" / "촬영 ㄱㄱ" / "키 접근 가능" 신호
- Resume first command:
  - (TBD) 관련 repo/폴더 경로 확인 후 첫 커맨드 확정
- Evidence:
  - (TBD) tx hash + explorer proof + 데모 영상

### AOI Workflow Builder Demo 촬영 (A/B/C + Full sequence)  (tag: aoi-workflow-demo-home)
- Status: PARKED
- Progress:
  - 촬영 조건(집에서만) 때문에 보류
- Needs from Edmond:
  - 촬영 가능한 환경(집)
- Resume trigger:
  - "집 도착" / "촬영 ㄱㄱ"
- Resume first command:
  - (TBD) 데모 스크립트/시나리오 파일 위치 확인

---

## deferred-bundle-2026-02-17

### Team Council 스킬 (Lite/Pro)  (tag: team-council-pause)
- Status: PARKED
- Progress:
  - Lite/Pro 네이밍 규칙/Notion DB/저장 스크립트/워커(autofill)까지 구축
- Needs from Edmond:
  - BNB 해커톤 피드백 상세 논의 후 우선순위 재확정
- Resume trigger:
  - "BNB 피드백 정리 끝" / "Team Council 다시" 신호
- Resume first command:
  - `ls skills/aoineco-team-council && python3 skills/aoineco-team-council/scripts/peek_queue.py`
- Evidence:
  - Notion Decision Log DB: https://www.notion.so/22efd166397c4804af859c38ddfd1f44

### $7 Survival / Bridge 운영 고도화  (tag: survival-bridge-gate)
- Status: PARKED
- Progress:
  - V6 pipeline에 survival gate(v1/v2) 경로/manifest/proof-first 설계 반영됨
  - Canary protocol(소액 테스트 전송) 및 DLMM/bridge 후보가 survival_input_v2 예시로 존재
- Needs from Edmond:
  - Shadow→Live 승격 게이트 기준 확정 후 실제 live 자동화 범위 승인
- Resume trigger:
  - "survival live gate 진행" 신호
- Resume first command:
  - `python3 the-alpha-oracle/engine/v6_pipeline.py` (최근 결과 확인)
  - `python3 scripts/shadow_kpi_digest.py`
  - (선택) `cat the-alpha-oracle/engine/survival_input_v2.example.json`

### x402 서명 엔진 / Claw.fm 업로드 준비  (tag: x402-clawfm)
- Status: PARKED
- Progress:
  - x402 signer 엔진 구현 흔적: `the-alpha-oracle/engine/x402_signer.js`
- Needs from Edmond:
  - claw.fm 업로드/발행 승인 + 계정/결제 플로우 확인
- Resume trigger:
  - "claw.fm 업로드 가자" 신호
- Resume first command:
  - `node the-alpha-oracle/engine/x402_signer.js`

### 로열티/문의 아웃리치 패키지 준비 (Nexus Bazaar 베타 전)  (tag: royalty-outreach-pack)
- Status: PARKED
- Progress:
  - 정책/템플릿 SSOT 존재: `context/ROYALTY_AND_ATTRIBUTION_POLICY.md`, `context/ROYALTY_OUTREACH_CONTACT_LOG_TEMPLATE_V0_1.md`
- Needs from Edmond:
  - 베타 오픈 날짜 확정 + 메시지팩 초안 승인
- Resume trigger:
  - "베타 오픈일 확정" / "로열티 메시지팩 만들자" 신호
- Resume first command:
  - `sed -n '1,200p' context/ROYALTY_AND_ATTRIBUTION_POLICY.md`
  - `sed -n '1,200p' context/ROYALTY_OUTREACH_CONTACT_LOG_TEMPLATE_V0_1.md`

### Alpha Oracle 제출 문서(USDC hackathon) 정리  (tag: alpha-oracle-submission-clean)
- Status: ❌ CLOSED — USDC hackathon ended, submission not made
- Outcome:
  - 제출 못함 (해커톤 종료)
- Post-mortem (optional):
  - 다음 USDC 계열 해커톤 대비해 제출용 `submission.json` 템플릿을 V6-only로 미리 준비
- First command (if revisiting docs):
  - `cat the-alpha-oracle/submission.json | head`

### 크론 큐레이터(blue-sound-insight-curator-dual) 외부 게시 금지 전환  (tag: curator-internal-only)
- Status: PARKED
- Progress:
  - 외부 게시 금지 + Idea Vault 저장 고정으로 payload 업데이트 완료
- Needs from Edmond:
  - Idea Vault 저장 포맷(필수 필드) 최종 확정
- Resume trigger:
  - "큐레이터 포맷 확정" 신호
- Resume first command:
  - `openclaw cron list`로 job 확인 + 다음 실행 결과 검토

### EigenCloud Open Innovation Challenge  (tag: eigencloud-open-innovation)
- Status: ✅ SUBMITTED (DONE)
- Deadline: Feb 20 11:59pm PT
- Requirements:
  - Must use EigenCompute/EigenCloud
  - No tokenized agents
  - Include demo link + repo link + announcement tweet (tag @eigencloud)
  - Form fields: Name, X handle, Email, Project name, One-line, How used EigenCloud, Demo link, Tweet link

- Strategy (A→B):
  - **A 먼저 제출 가능 수준으로 구축**: Verifiable Proof Bundle Runner (proof-first manifest+sha256)
  - **B는 확장 로드맵**으로만 포함(시간/완성도 봐서 구현 추가): Verifiable Agent Identity Wrapper

- Proposed fit for Aoineco:
  - Proof-first + fail-closed 운영 철학을 EigenCompute 실행 증빙으로 포장

- Current blocker:
  - Local access unavailable right now
  - Docker daemon not running (Docker Desktop OFF) → `docker run` fails
- Resume trigger:
  - "오늘/내일 아이겐레이어 해커톤 하자" + Docker Desktop 켜짐 신호
- Resume first command:
  - `docker run --rm hello-world`
  - then: proceed to EigenCompute toolchain install + A(MVP) scaffold
- Evidence:
  - Ideas: https://ideas.eigencloud.xyz/
  - Dev: https://developers.eigencloud.xyz/
  - Form: https://docs.google.com/forms/d/e/1FAIpQLSdjCpocv1HibJOEMLtxBxbxleMOZoUIXSmUOT-B1QSv-7HLPg/viewform

## deferred-bundle-2026-02-20

### Nexus Bazaar 용어 정책 + 다음 빌드 백로그  (tag: bazaar-terminology-backlog)
- Status: PARKED
- Decision (locked): **Top-level term = “Nexus Bazaar”**. “AI DEX”는 외부 top-level 금지(내부/배경 용어로만).
- Current internal build:
  - Private repo: https://github.com/edmonddantesj/nexus-bazaar-private
  - Core-Temp v0.2: audit FAIL → 🧊Frozen(0.0°C), proof bundle에서 sdna_verify 자동감지
  - UI v0.2: price range + badge filters + temp min
- Parked next actions (resume backlog):
  1) Trust 이벤트/히스토리 기반 고도화
     - FAIL→freeze→thaw 조건(새 PASS 번들 시 해제 등) 설계
     - 산출물: `trust_timeline.json` (merchant별 이벤트 로그) + core-temp 계산이 이를 참조
  2) Search index v0.2 스키마/계약 고정 + CI
     - index schema v0.2 명시 + UI/CLI 필수 필드 고정
     - CI에 index 생성 + (간이) UI 로드 테스트 추가
  3) UI polish (reviewer workflow)
     - preset filters(Verified/Frozen/Guardian-only)
     - merchant 상세 drawer(최신 proof/audit/sdna 요약)
     - 36.5°C baseline 시각화
- Resume trigger:
  - "바자르 다시" / "Trust timeline 하자" / "UI polish" 신호
- Resume first command:
  - `cd projects/nexus-bazaar-private && python3 scripts/test_audit_stall_demo.py && python3 scripts/test_bazaar_fx_skill_demo.py`

## Notes
- 이 파일은 cron job `AOI — 보류(실전/해커톤) 번들 요약 브리핑 (내일)`이 요약 대상으로 사용한다.
