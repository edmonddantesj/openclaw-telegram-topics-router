# github PLAYBOOK V0.1

- **Purpose:** GitHub 링크 인입 → 분석/도입/적용(LOCAL APPLY) + 광역 영향(WIDE REVIEW) 분리 운영
- **Last updated:** 2026-03-08

## Imported from DM export (Shadow Ingest)

### Recurring tasks (Top N)
1) **GitHub 인입/벤치마크 아이디어를 Notion에 기록(Reference List/Benchmarking) + 누락 검증**
- Rule: GitHub 레퍼런스는 Notion DB에 ‘표(속성)’와 ‘열기(본문 리포트)’까지 채워져야 완료.
- Failure mode: 표만 채우고 본문이 비어있거나, 잘못된(유령) DB에 쓰는 문제.
- Proof: DM export `messages.html` msgId=122, 123988 (요청/실패패턴)

2) **DB ID/워크스페이스 정합성 먼저 확인(동명 페이지/복제본 주의)**
- Rule: 이름이 같아도 ID가 다르면 다른 DB다 → 주소창 ID/직링크 기반으로 대상 확정.
- Proof: DM export `messages.html` msgId=123893, 123849

3) **GitHub 분석 리포트 포맷 고정 (3줄 요약 + 기술 구조 + 적용 인사이트)**
- Rule: ‘열기’ 본문에 동일 포맷으로 축적해 재사용성 확보.
- Proof: DM export `messages.html` msgId=123984

4) **실행 컨텍스트 env(GITHUB_TOKEN 등)가 도구 인증을 덮어쓰는 이슈 주의**
- Rule: auth가 이상하면 환경변수 오염부터 의심(필요 시 `env -u GITHUB_TOKEN gh …`).
- Proof: 로컬 운영 기록(SSOT): `context/topics/inbox-dev_PLAYBOOK_V0_1.md` Common pitfalls

## Where to record
- 인입/진행: `context/handoff/INDEX.md` + 관련 HF
- 정책/체크리스트: 이 Playbook + `context/GITHUB_WIDE_REVIEW_AND_LOCAL_APPLY_POLICY_V0_1.md`
