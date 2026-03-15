# AOI Squad Pro — Launch Plan (D-? Fast Beta) v0.2

Source baseline: Notion “AOI Squad Pro — Launch Plan (D-7) v0.1” page.

## 🎯 Non‑negotiables
- **Beta deadline:** 2026-02-21 (Sat) **12:00 KST 이전** — “설치→첫 실행→승인→증빙(proof)”까지 end-to-end 동작 데모.
- **2-week dev window**는 유지하되, 베타 이후는 안정화/포장/배포 확장.
- **Guardrails:**
  - No direct merges to `main`
  - No external posting
  - No ClawHub publish w/o Edmond approval
  - No secrets/tokens/vault 출력 금지
  - “No internal nicknames” in PR/output (외부용)

## 🧭 Product shape (what we ship in Beta)
### Beta = “Agent Ops Kit (Pro)”
1) **1-command install** (macOS): repo clone/install → skill placement → 권한 설정 → smoke test
2) **Updater (tag-based)**: pull → checkout tag → smoke test → rollback hint
3) **Access control v0 (manual allowlist)**: allowlisted customer ids only (fail-closed)
4) **Onboarding quickstart (5 min)**: run → approval_request → approve → proof link
5) **2 demo scripts**
   - docs task: README modify
   - ops task: launch checklist 생성
6) **QA safety suite (minimal but real)**
   - patch apply/reject
   - sha mismatch
   - deny_globs
   - absolute path blocked

## 🧑‍🤝‍🧑 Role split (스쿼드 운영)
- 🧿 Oracle: scope lock, acceptance criteria, ADR 기록
- 🧠 Analyzer: onboarding flow, demos, copy(내부/외부), info architecture
- ⚔️ Security: allowlist model, fail-closed, string-scan(닉네임/비밀), regression cases
- ⚡ Builder: installer/updater, smoke, packaging, CI-lite(로컬)
- 📢 Comms: landing/announcement draft(게시 금지; 내부 준비), FAQ, support intake 설계
- 🧼 Maintainer(Blue‑Maintainer): daily smoke + cron health + run-state/artifacts 탐지 안정화

## ✅ Acceptance criteria (Beta)
- 새 맥에서(또는 깨끗한 사용자 환경에서) 아래가 1시간 내 재현:
  - install 1회
  - quickstart 실행 1회
  - approval request/approve 1회
  - proof artifact 1개 생성(파일 경로 + sha 또는 URL)
- 실패 시: 왜 실패했는지 3줄 요약(log pointer 포함)

---

# 📅 Schedule

## Phase 0 — 오늘~내일(2/17~2/18): Foundations (P0)
- [P0] Installer skeleton + smoke test
- [P0] Updater skeleton
- [P0] Allowlist fail-closed gate
- [P0] Quickstart 문서 초안

## Phase 1 — 2/19(Thu): Demo-ready
- [P0] demo script 2개 구현
- [P0] QA 최소 6케이스 자동 실행 스크립트
- [P0] proof artifact 포맷 고정(1줄 summary + 경로)

## Phase 2 — 2/20(Fri): Polish + rehearsal
- [P0] Fresh install rehearsal(새 폴더/새 venv)
- [P0] Troubleshooting (권한/경로/py 버전)
- [P1] Landing copy/FAQ 내부 준비

## Phase 3 — 2/21(Sat) 12:00 이전: Beta handoff
- [P0] 베타 결과물 패키징(install/update + docs + demos + qa)
- [P0] “1-page beta report” 생성(무엇이 됐고/안됐고/다음)

## Phase 4 — 2/21~2/28: Hardening week
- [P0] run-state/artifacts 자동 탐지 복구
- [P0] cron digest 안정화(실패 원인 포함)
- [P1] Customer delivery path 확정(zip vs invite)
- [P1] Support policy v0.1

## Phase 5 — 3/1~3/3: Launch readiness
- [P1] Pricing packaging + licensing v1
- [P1] External announcement (승인 후)

---

# 🔥 Fast follow (우리가 AITMPL 대비 내세울 강점)
- **Proof-first**: 실행 결과가 증빙으로 남는다.
- **Governance by default**: 승인/가드레일/Fail-closed.
- **SSOT**: Notion+local로 리셋에도 복구.
- **Ops health**: “왜 안나왔어?”를 자동으로 설명.
