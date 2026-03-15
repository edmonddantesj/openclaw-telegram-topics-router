# Skill Scouting Autopilot Policy v0.1 (Aoineco)

Last updated: 2026-02-20 (KST)
Status: ACTIVE

> 목적: 정찰로 획득한 스킬 후보를 **팀 내부 검토→결론→자동 착수**로 연결한다.
> 주의: L3(돈/지갑/외부게시/온체인/비가역)는 자동 실행 금지. 승인 게이트 필수.

---

## 1) Trigger (발동)
- 정찰 결과가 들어오면 (cron/채팅/링크), 후보 스킬을 `context/skill_scouting/inbox/`에 1건으로 등록한다.

## 2) Default workflow (자동 재개 순서)
### Step A — Intake Pack 생성 (자동)
- 각 후보마다 `도입해줘(V0.2)`의 **증빙팩 포맷**으로 최소한의 "검토팩"을 만든다.
- 경로: `context/adoption/<YYYY-MM-DD>_<slug>_ADOPTION_PACK_V0_1/`
- 필수 파일:
  - `00_intake.json`
  - `10_license_and_security.md` (라이선스/보안 1차 스캔)
  - `20_creator_contact.md` (가능하면)
  - `30_rebuild_plan.md` (벤치마크→우리만의 새 스킬로 만들 때의 계획 포함)
  - `40_install_proof.md` (단, 설치/적용은 결론 후)

### Step B — Team Review (자동 준비 + 내부 논의)
- 팀원들이 같은 포맷으로 검토할 수 있게 **리뷰 카드 템플릿**을 자동 생성한다.
- 각 후보에 대해 아래를 채우고, 최종 결론을 1줄로 고정:
  - Adopt(도입해줘 진행) / Rebuild(벤치마크→우리 스킬로 재개발) / Reject
  - 근거(3 bullets) + 리스크(3 bullets)

### Step C — Decision Lock (결론 고정)
- 결론은 SSOT로 남긴다:
  - 로컬: `context/skill_scouting/decisions/<YYYY-MM-DD>_<slug>_DECISION.md`
  - **Notion Decision Log DB에도 미러링(SSOT 이중화)**: `context/NOTION_DECISION_LOG_TARGET_SSOT_V0_1.md`

### Step D — Auto Start (결론에 따라 자동 착수)
- **Rebuild**면: 새 스킬 스켈레톤 생성 + PRD/스펙/테스트 플랜부터 착수.
- **Adopt**면: `도입해줘(V0.2)` 프로토콜대로 진행(리빌딩→설치 증빙 포함).
- **Reject**면: 기록만 남기고 종료.

---

## 3) Boundaries (자동 금지)
- 외부 게시/홍보/업로드 (Moltbook/봇마당 등) → 항상 Yes/No 승인.
- 지갑/송금/브릿지/베팅 실행 → 항상 L3 승인.
- 비공개/Restricted 스킬을 ClawHub에 퍼블리시 → 승인 + Security Gate PASS.

---

## 4) SSOT References
- 도입해줘 프로토콜(정본): `context/COMMAND_DOIP_HAEJWO_PROTOCOL_V0_2.md`
- 정찰 거버넌스: `context/SKILL_SCOUTING_GOVERNANCE.md`
- 로열티: `context/ROYALTY_AND_ATTRIBUTION_POLICY.md`
- 게시 승인 SOP: `context/CONTENT_INGEST_TO_POST_APPROVAL_SOP_V0_1.md`
- ClawHub 퍼블리시 정책: `context/CLAWUB_PUBLISHING_POLICY_V0_1.md`
