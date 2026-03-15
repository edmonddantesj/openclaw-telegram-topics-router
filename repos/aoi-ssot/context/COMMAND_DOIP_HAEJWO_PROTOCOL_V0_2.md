# Command Protocol — “도입해줘” (V0.2)

> V0.1의 의미/순서는 유지하되, **단계별 산출물(증빙) 포맷**을 고정한다.

## 0) 정의 (SSOT)
사용자가 스킬/레퍼런스 도입 논의 중 **“도입해줘”**라고 말하면, 에이전트는 아래를 기본 의미로 이해하고 실행한다.

## 1) 실행 순서 (반드시 이 순서)
1. 라이선스/보안 검증 (필수)
2. 창작자 연락처 탐색/기록
3. 리빌딩/디벨롭 + S‑DNA 재구성 (보안 업그레이드 포함)
4. 설치/내부 적용 (기본: 리빌딩 결과물 설치)

## 2) 산출물(Proof) — 파일/포맷 고정
### 2.1 로컬 SSOT 폴더
- 경로: `context/adoption/<YYYY-MM-DD>_<slug>_ADOPTION_PACK_V0_1/`
- 이 폴더 안에 아래 파일을 **반드시 생성**한다.

### 2.2 파일 리스트 (필수)
1) `00_intake.json`
- 목적: 무엇을 도입하려는지 “입력”을 고정
- 스키마:
```json
{
  "slug": "swarm-kanban",
  "source_url": "https://clawhub.com/skills/swarm-kanban",
  "requested_by": "Edmond",
  "trigger": "도입해줘",
  "date_kst": "2026-02-19",
  "notes": "why now / intended use"
}
```

2) `10_license_and_security.md`
- 목적: 라이선스/보안 검증 결과를 **캡처/인용 기반으로** 고정
- 템플릿:
```md
# License & Security Check

## License
- Declared license: <MIT/Apache/Unknown>
- Commercial restriction text (verbatim quote):
  - "..." (없으면: 미명기)
- Redistribution restriction text (verbatim quote):
  - "..." (없으면: 미명기)

## Security scan (manual + heuristics)
- Network egress: <None / External API domains: ...>
- Secrets handling: <None / Reads env / writes token file ...>
- Exec/eval/subprocess: <None / Details>
- Auto-run hooks/cron: <None / Details>

## Risk tier
- L1 / L2 / L3:
- Rationale (1-3 bullets):
```

3) `20_creator_contact.md`
- 목적: 창작자 연락처 탐색/기록 + TBD를 표준화
- 템플릿:
```md
# Creator Contact

- Owner/Author: <handle/name>
- Contact methods found:
  - email: <...|TBD>
  - x/twitter: <...|TBD>
  - github: <...|TBD>
  - website/form: <...|TBD>

## Contact attempt log (if attempted)
- YYYY-MM-DD | channel | target | message_pack_version | result | proof
```

4) `30_rebuild_plan.md`
- 목적: 리빌딩 계획(우리 방식) + S‑DNA 포인트 정의
- 템플릿:
```md
# Rebuild Plan (S-DNA)

## What we keep
- ...

## What we change (security upgrades)
- allowlist/timeout/retry
- masking
- approve gate

## Outputs
- rebuilt skill path:
- tests:
```

5) `40_install_proof.md`
- 목적: 설치/내부 적용 증빙(VCP) 고정
- 템플릿:
```md
# Install Proof

- Installed artifact: <rebuilt|original>
- Install method: clawhub install / local copy / git submodule ...
- Installed path: skills/<slug>
- Smoke test: PASS/FAIL
- Evidence:
  - command(s):
  - log path(s):
```

### 2.3 선택 파일 (권장)
- `11_security_scan_raw.txt`: rg/grep 결과(긴 출력은 여기로)
- `41_smoke_test_log.txt`

## 3) Notion 기록 (필수)
- Notion Reference Inbox에 1페이지로 기록
- 페이지 본문에 위 파일들의 요약을 붙이고,
- 로컬 SSOT 경로를 맨 위에 1줄로 박는다:
  - `SSOT(local): context/adoption/<...>/`

## 4) 승인 라우팅 (L1/L2/L3)
- 거버넌스 정본: `context/SKILL_SCOUTING_GOVERNANCE.md`
- 로열티 정본: `context/ROYALTY_AND_ATTRIBUTION_POLICY.md`

## 5) 금지/주의
- 시크릿/토큰/vault 출력 금지
- Nexus Bazaar 베타 오픈 전 외부 공개/배포/판매/게시 금지
