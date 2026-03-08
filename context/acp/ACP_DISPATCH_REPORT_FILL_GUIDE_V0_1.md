# ACP Dispatch Report Fill Guide V0.1 (0–8 machine-readable)

목적: ACP Dispatch #002(이후 포함)에서 12명 팀원이 **자율로 구매/분석**한 내용을, 합본/편집이 쉬운 “머신-리더블” 포맷으로 빠르게 채우도록 가이드한다.

- **Canonical spec repo:** `repos/aoineco-acp-dispatch-spec/dispatch/`
- **Issue #002 folder:** `repos/aoineco-acp-dispatch-spec/dispatch/ACP_DISPATCH_002_2026-03-07/`
- **Channel:** Moltbook (publish is L3 승인)

---

## 하드 룰 (반드시)
1) **구매/결제/온체인 실행은 L3**: 최종 실행/게시 전에는 메르세데스 승인(Yes/No) 없이는 진행하지 않음.
2) **Author name: Aoineco only** (assistant persona/개인명 표기 금지)
3) **시크릿 금지:** seed/private key/Privy auth key/acp-*** API key 등은 문서/Notion/채팅/Repo에 절대 포함 금지
4) **증빙 우선:** 주장/결론에는 최소 1개 이상의 evidence pointer를 붙인다(링크/tx hash/job id/log path)

---

## 0–8 섹션 템플릿(고정)
> 아래 섹션 헤딩을 그대로 사용(0~8 번호 유지). 이걸 지켜야 합본/자동 파싱이 가능.

### 0) Identity
- Role: (예: BLUE_BLADE)
- Report file: (본인 파일명)
- Date: YYYY-MM-DD

### 1) What we bought (or tested)
- Skill/Offering name:
- URL:
- Price / unit:
- Why chosen (1–2 lines):

### 2) Setup / How to run (repro)
- Prereqs:
- Steps:
- Expected output:

### 3) Result summary (fast)
- Worked? (yes/no/partial)
- Output quality (1–5):
- Time-to-value:
- 1-line takeaway:

### 4) Evidence pointers (proof-first)
- tx hash (if any):
- job/deliverable id (if any):
- logs / screenshots:
- notes:

### 5) Failure modes / gotchas
- What broke:
- Edge cases:
- Mitigations:

### 6) Ops / Security / Guardrails
- Data exposure risk:
- Permission surface:
- Rate-limit / cost risk:
- Suggested gates (L1/L2/L3):

### 7) Verdict
- Adopt / Watch / Skip:
- Who should use it:
- When to avoid:

### 8) Next
- Next experiment (1):
- Next experiment (2):

---

## Evidence 규격(최소)
- 링크/tx hash/job id 중 1개 이상 필수
- tx hash는 축약(앞 6 + 뒤 4) 가능하나, 가능하면 full도 첨부
- 로그 파일은 경로만(내용 전문 붙여넣기 금지; 필요 시 요약만)

## 4/4/4 배치 운영 팁
- Batch마다 스킬 탐색 범위를 다르게(겹침 최소화)
- “결과 없는 리서치”보다 **작게라도 실행/증빙**을 우선

## 편집자(청묘) 합본 체크
- 섹션 0~8 누락 여부
- Evidence 존재 여부
- 금칙어/시크릿 문자열 포함 여부
- L3(구매/게시) 승인 기록 여부
