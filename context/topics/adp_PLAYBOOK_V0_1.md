# adp PLAYBOOK V0.1

- **Purpose:** Aoineco Dataplane(ADP) — 운영/업무/픽셀오피스/라벨링/보드(Jira/Ralph) 가시화 포털을 SSOT로 고정
- **Last updated:** 2026-03-08

## Imported from DM export (Shadow Ingest)

### Recurring tasks (Top N)
1) **ADP 정식 명칭은 Aoineco Dataplane(ADP)로 고정(ACC 혼동 금지)**
- Proof: DM export `messages16.html` msgId=11118

2) **ADP 서버 헬스: 응답 먹통이면 restart로 정상화 + tailnet URL/로컬 URL 구분**
- Proof: DM export `messages16.html` msgId=11190

3) **Pixel Office/보드(Jira/Ralph) 뷰를 ‘업무 분배/라벨’ 루프와 연결**
- Proof: DM export `messages17.html` msgId=11389, 11393 (auto dispatch / collab splitter)

4) **ADP에 Ralph Loop 분류/집계 뷰 유지(필터/분류 규칙은 label 포함으로 넓게)**
- Proof: DM export `messages17.html` msgId=11547, 11549

### Automation candidates (adp)
- ADP 서버 헬스체크/재시작은 launchd로 고정 주기 감시 후보.
- 보드 분류 규칙/라벨 누락 정리는 Ralph Loop로 backlog 처리 후보.

## Where to record
- 진행중 작업: `context/handoff/INDEX.md` + 관련 HF
- 정책/체크리스트: 이 Playbook + `context/adp/*` SSOT

## Heukmyo support routing
- AC/Judge 구조 정리, work card schema 분해, room workflow 정리, installable package/productization 메모 정리처럼 구조화 지원이 필요할 때는 `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md` 기준으로 요청을 구조화한다.
- 기술성 높은 요청(상태 스키마/구현 경계/복구성 검토)은 optional extension field(`Affected scope`, `Failure mode`)를 함께 붙인다.
- 외부 반영, 정책 변경, 고위험 운영 전환은 human gate 유지.
