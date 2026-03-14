# 청묘 ↔ 흑묘 지원 프로토콜 One-Page V0.1

## 목적
청묘팀이 특정 토픽에서 흑묘팀 지원이 필요할 때,
요청 범위를 구조화해서 넘기고 흑묘팀이 재사용 가능한 산출물로 회신하도록 만드는 내부 요약본.

## 기본 구조
- 청묘팀: 범위 정의 / 목표 / 마감 / 승인 경계 명시
- 흑묘팀: 범위 내 지원 실행 / 문서화 / 초안화 / 재사용 자산화
- Human gate: 외부 반영 / 최종 승인 / 고위험 실행

## 공용 요청 포맷
- Topic:
- Priority: P0 / P1 / P2
- Current state:
- Goal:
- Deadline:
- Needed support:
- Expected output type:
- Constraints / human gate:
- Reference paths:

## 공용 회신 포맷
- Owner:
- State: done / partial / blocked / needs-human-review
- What was done:
- Output:
- Next:
- Blocker / human gate:
- Updated paths:
- Promote candidate: no / local playbook / SSOT candidate

## 기술 토픽 확장 필드
기술성 높은 토픽(inbox-dev / ops / 일부 ADP / incident / recovery)에서는 아래 optional field를 추가 권장.

- Affected scope: repo / folder / script / state / db / service
- Failure mode: what is broken / missing / risky

## 언제 쓰나
- 범위가 큰 일을 분해해서 외부 지원 초안/체크리스트/리서치가 필요할 때
- 복구/재구축 요청을 구조화해서 넘길 때
- 리뷰/정리/SSOT 승격 후보 선별이 필요할 때
- 제출/배포 전 준비 산출물을 분담할 때

## Human gate 기본값
아래는 기본적으로 human gate로 남긴다.
- 외부 제출
- 외부 공개
- 최종 게시
- 배포 / 프로덕션 반영
- 조직 구조 변경
- 정책 변경
- 승인 범위 밖 파일 수정
- 고위험 실행

## 한 줄 원칙
청묘팀은 구조화해서 요청하고,
흑묘팀은 bounded 산출물로 회신하며,
외부 반영과 최종 승인은 human gate로 남긴다.
