# 청묘 ↔ 흑묘 지원 프로토콜 참조 연결안 V0.1

## 목적
토픽 playbook에서 언제 이 프로토콜을 참조해야 하는지 빠르게 연결하기 위한 메모.

## Canonical vs Local Reference

- Canonical policy source:
  - `context/heukmyo-squad/playbook/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_V0_2.md`
  - `context/heukmyo-squad/playbook/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_TECH_EXTENSION_V0_1.md`
- Workspace-local operating references:
  - `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md`
  - `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_EXAMPLES_V0_1.md`

Rule:
- Policy interpretation should follow canonical playbook docs.
- Day-to-day topic routing and request drafting inside this workspace may use the local one-page/examples set.

## 권장 참조 추가 위치

### 1) inbox-dev PLAYBOOK
파일: `context/topics/inbox-dev_PLAYBOOK_V0_1.md`

권장 추가 문구:
- 범위가 큰 복구/재구축/설계 분해 요청은 `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md` 기준으로 흑묘팀 지원 요청을 구조화한다.
- 기술성 높은 요청은 optional extension field(`Affected scope`, `Failure mode`)를 함께 붙인다.

### 2) ops PLAYBOOK
파일: `context/topics/ops_PLAYBOOK_V0_1.md`

권장 추가 문구:
- 운영 체크리스트 초안, 장애 triage 정리, 복구/점검 문서화가 필요할 때는 청묘 ↔ 흑묘 지원 프로토콜을 사용한다.
- 재시작/모델 전환/서비스 변경은 human gate로 남긴다.

### 3) hackathons PLAYBOOK
파일: `context/topics/hackathons_PLAYBOOK_V0_1.md`

권장 추가 문구:
- 제출 패키지 준비 중 리서치/체크리스트/초안/비교표 지원이 필요할 때는 청묘 ↔ 흑묘 지원 프로토콜로 요청 범위를 구조화한다.
- 최종 제출/외부 공개는 human gate 유지.

### 4) ADP / bazaar / github-adoption technical PoC
현재 또는 차기 playbook/hand off에 아래 수준으로 연결 가능:
- 구조화된 지원 요청 필요 시 본 프로토콜 참조
- 기술성 높은 요청은 optional extension field 추가

## 연결 방식
Playbook 본문에 길게 설명하지 말고, 아래 정도의 짧은 문구를 추천.

> 흑묘팀 지원이 필요할 때는 `context/heukmyo-squad/CHEONGMYO_HEUKMYO_SUPPORT_PROTOCOL_ONEPAGE_V0_1.md` 기준으로 요청을 구조화한다. 기술 복구/구현 지원은 `Affected scope`, `Failure mode`를 추가한다.

## 메모
canonical 본체/기술 확장 문서는 외부 canonical repo 기준으로 잠겨 있을 수 있으므로,
workspace에서는 one-page 요약본과 예문을 운영용 참조로 유지한다.
