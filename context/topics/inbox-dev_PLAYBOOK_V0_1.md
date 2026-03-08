# inbox-dev PLAYBOOK V0.1 (Topic 585)

- **Purpose:** 긴급개발/핫픽스/데드라인 대응 (실행 우선)
- **Last updated:** 2026-03-08

## Recurring rules (must not forget)
1) “긴급”이 나오면 **식별자 먼저**
   - HF 파일명/링크 또는 토픽+키워드 2~3개 확보
   - 없으면 추측 실행 금지 → HF부터 생성
2) 모든 P0는 Proof-first
   - 배포 URL / PR / 커밋 / 로그 / 재현 스텝 중 최소 1개를 남긴다.
3) 멈추기 전 Next 3
   - 중단 직전에 다음 액션 3개를 HF에 남긴다.

## Imported from DM export (Shadow Ingest)
- 반복 패턴: 외부 서비스/SDK 상호작용(예: 시장/계정 상태가 시간에 따라 만료)에서 오류가 날 경우, **재스캔/재조회(현 시점 기준)**가 1차 대응.
  - Proof: DM export `messages2.html` msgId=1059 (시장 재스캔 제안)

## Canonical Handoff
- ACTIVE 인덱스: `context/handoff/INDEX.md`
- 관련 HF(현재): `context/handoff/HF_inbox_dev_urgent_202603.md`

## Common pitfalls
- GitHub auth 환경변수(`GITHUB_TOKEN`)가 `gh` 인증을 덮어쓰는 케이스 주의(필요 시 `env -u GITHUB_TOKEN gh ...`).
