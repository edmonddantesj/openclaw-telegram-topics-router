# ACP 바운티 운영 스킬 — 실행 패키지 (순서형)

## 0) 전제 확인
- 현재 `openclaw-acp` 경로 3개 오퍼링은 스키마/핸들러 동작 준비 완료.
- 외부 푸시/권한은 사용자 승인 또는 별도 브랜치/포크 기준으로 수행 필요.
- `WORKFLOW_AUTO.md` 경로가 현재 워크스페이스 루트에 존재하지 않음(요청 파일 자체 미존재).

---

## 1) 가격/포지셔닝 잠금 (빠른 결판)
- `bounty_scope_plan`: **0.03 USDC**
- `bounty_match_maker`: **0.05 USDC**
- `bounty_qc_packager`: **0.08 USDC**
- 패키지 제안(권장): `scope + match + qc = 0.16 USDC`

---

## 2) 한글/영문 오퍼링 소개문 (복붙용)

### A) 한글(판매용)
**서비스명:** `Bounty Scope Planner`
- 바운티 의뢰를 1페이지 실행 플랜으로 바꿔줍니다.
- 요구사항을 명확화하고, 작업 분해, 체크리스트, 리스크/완화안을 함께 제공합니다.
- 결과: 승인 가능한 구조화 문서 + 증빙 해시.

**서비스명:** `Bounty Match Maker`
- 요구 스킬/조건을 넣으면 가장 적합한 오퍼링을 점수 기반으로 추천합니다.
- Top 후보 + 매칭 근거 + 예산 감안 순위 + 리스크를 제공합니다.
- 결과: 즉시 실행 가능한 바운티 분배 사다리.

**서비스명:** `Bounty QC Packager`
- 제출물/텍스트를 기준 항목별로 점검해 통과율, 누락 항목, 리스크 수준을 산출합니다.
- 실무형 증빙 JSON을 남겨 분쟁/재작업 비용을 줄입니다.

### B) English (marketing)
**Bounty Scope Planner**
- Converts vague bounties into an auditable execution plan.
- Returns task breakdown, acceptance checks, risks/mitigations, and proof-ready handoff metadata.

**Bounty Match Maker**
- Ranks candidate offerings by required skill overlap and delivery constraints.
- Returns top recommendations, rationale, budget framing, and risk tags.

**Bounty QC Packager**
- Scores submission quality against explicit criteria, surfaces misses, and outputs an evidence-grade QC report.
- Helps reduce rejection/rework cycles with clear correction guidance.

---

## 3) ACP 등록/테스트 실행 순서

### 3-1. 사전 준비
```bash
cd /Users/silkroadcat/.openclaw/workspace/skills/openclaw-acp
acp setup
acp whoami
acp sell list
```

### 3-2. 오퍼링 등록(개별)
```bash
acp sell create bounty_scope_plan
acp sell create bounty_match_maker
acp sell create bounty_qc_packager
acp sell list
acp sell inspect bounty_scope_plan
acp sell inspect bounty_match_maker
acp sell inspect bounty_qc_packager
```

### 3-3. 샘플 시나리오 dry-run (요약)
```bash
# scope
npx tsx -e "import { executeJob } from './src/seller/offerings/bounty_scope_plan/handlers.ts';
const r = await executeJob({ goal:'Create launch narrative', constraints:'max 900 words', deliverableType:'launch brief', requiredChecks:['clarity','evidence'] });
console.log(r.deliverable);"

# match
npx tsx -e "import { executeJob } from './src/seller/offerings/bounty_match_maker/handlers.ts';
const r = await executeJob({ goal:'Need ops recovery guidance', requiredSkills:['ops','recovery','plan']});
console.log(r.deliverable);"

# qc
npx tsx -e "import { executeJob } from './src/seller/offerings/bounty_qc_packager/handlers.ts';
const r = await executeJob({ expectedCriteria:['scope clearly described','proof bundle'], submissionText:'scope clearly described and proof bundle included', strictMode:true});
console.log(r.deliverable);"
```

### 3-4. 정합성 체크포인트
- `status: ok|failed` 존재
- `input_digest` 존재
- `evidence` 블록 존재
- 실패 시 `failure_code`와 `suggested_fix` 존재
- strict 실패면 `score.strictModeFail`이 true인지 확인

---

## 4) 운영용 템플릿(바운티 수주 문구)

**클라이언트 최초 응답 템플릿:**
- "요건이 정리되기 전에 바로 착수하면 실패율이 2배 올라갑니다. 먼저 Scope Plan으로 의뢰를 정리하고, Match로 적임자 1차 배정, QC로 합격 기준 고정한 뒤 진행하면 승인 확률이 즉시 올라갑니다."

**배달 완료 템플릿:**
- "Plan/Match/QC 체인으로 산출물 정합성 점검이 끝났습니다. 핵심 지표: scope_status=ok, match_top=..., qc_coverage=...%. 누락 항목은 ... 입니다. 다음 조치 제안: ..."

---

## 5) 다음 실행(순서)
1. 위 템플릿 승인 후 pricing lock-in
2. 각 `sell create` 실행 및 결과 캡처
3. 실패면 `offering.json` 미리보기와 요구 필드 보정
4. 2~3건 바운티 샘플을 실제 `acp job create`로 시뮬레이션
5. `/memory/2026-02-19.md`에 접수ID/응답스니펫 기록
