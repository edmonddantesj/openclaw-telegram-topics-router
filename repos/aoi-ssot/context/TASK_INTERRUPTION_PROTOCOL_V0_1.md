# TASK_INTERRUPTION_PROTOCOL_V0_1.md

## 목적
대화/작업 중 태스크가 다른 태스크로 **중단(interrupt)** 될 때,
- 진행상태/다음 할 일/필요 입력을 **Parking Lot(SSOT)** 에 저장하고
- 사용자가 "끝/완료" 신호를 주면 즉시 **트리거 기반 리마인드**로 재개를 돕는다.

## SSOT 파일
- Parking Lot: `context/TASK_PARKING_LOT.md`
- 상태 포인터: `CURRENT_STATE.md`

## 운영 규칙 (고정)
1) **중단 순간에 즉시 파킹**
- 아래 3가지를 반드시 기록:
  - (a) 지금 어디까지 했는지(Progress)
  - (b) 다음 할 일(Next)
  - (c) 에드몽에게 필요한 입력/승인/자료(Needs)

2) **태그 기반 트리거**
- Parking Lot 항목은 `tag:` 를 반드시 가진다.
- 사용자가 `끝/완료/다 했어/OK` 또는 `재개 <tag>` 신호를 주면:
  - 해당 tag와 연관된 PARKED/BLOCKED 항목을 찾아
  - 3줄 요약 + 재개 첫 커맨드(또는 다음 행동 1개)까지 제시한다.

3) **Done 보고 금지 (VCP 연계)**
- 파킹/재개 모두: 링크/파일 경로 등 증빙이 가능한 형태로 기록한다.

## 추천 사용자 커맨드(대화용)
- `파킹 <tag>: <한줄>` → 지금 하던 거 중단 저장
- `재개 <tag>` → 저장된 거 바로 이어서 시작
- `태스크 목록` → 파킹된 것들 요약 출력

## Parking Lot 카드 템플릿
```md
### <Title>  (tag: <tag>)
- Status: PARKED | BLOCKED
- Progress:
- Next:
- Needs from Edmond:
- Resume trigger:
- Resume first command:
- Evidence:
```
