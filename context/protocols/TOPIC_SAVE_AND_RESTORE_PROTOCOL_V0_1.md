# Topic Save & Restore Protocol v0.1

상태: SSOT (local)

## 목표
전역 `현재를 저장` / `복구해줘`와 별개로, **토픽 단위 체크포인트**를 빠르게 남기고 복구할 수 있게 한다.

## 명령 체계
### 전역
- `현재를 저장`
  - 워크스페이스 전체 기준 저장.
  - `scripts/save_now.sh` 실행 계열 + 필요한 SSOT 업데이트.
- `복구해줘`
  - 반드시 **1회 분기 질문**:
    1) 전체 상태 복구
    2) 현재 토픽 복구
    3) 파일/폴더 복구

### 토픽별
- `이 토픽 저장`
- `이 토픽 복구`
- `토픽 저장: <slug>`
- `토픽 복구: <slug>`

권장 slug 예시:
- `x-post`
- `random`
- `maintenance`
- `inbox-dev`
- `acp`
- `ralph-loop`

## 저장 위치
- 인덱스: `context/topic-state/INDEX.md`
- 개별 상태 파일: `context/topic-state/<slug>.md`

## 토픽 상태 파일 최소 스키마
각 토픽 상태 파일은 최소 아래를 유지한다.

1. Topic identity
2. Current objective
3. Latest checkpoint
4. Decisions locked
5. Next actions
6. Key files / links
7. Restore instructions

## 저장 시 동작 (`이 토픽 저장`)
현재 토픽 기준으로 아래를 갱신한다.
- `context/topic-state/<slug>.md`
- 필요 시 대응 Playbook / HF 문서
- 당일 `memory/YYYY-MM-DD.md`에 저장 사실 기록

### 저장 내용 원칙
- 장황한 로그보다 **재개 가능한 요약** 중심
- 다음 턴에서 바로 이어갈 수 있게 쓴다
- 비밀값/시크릿은 절대 본문에 넣지 않는다
- 외부 링크보다 **로컬 SSOT 경로** 우선

## 복구 시 동작 (`이 토픽 복구`)
1. `context/topic-state/<slug>.md`를 먼저 읽는다.
2. 거기서 가리키는 Playbook / HF / 관련 파일만 최소한으로 읽는다.
3. 아래 3가지를 짧게 재구성한다.
   - 지금 뭐 하는 토픽인지
   - 마지막으로 어디까지 됐는지
   - 지금 당장 다음 액션이 뭔지

## Playbook vs HF vs Topic-state 역할 분리
- `context/topics/*_PLAYBOOK*.md`
  - 반복 규칙 / 운영 원칙 / 고정값
- `context/handoff/HF_*.md`
  - 진행중 큰 작업 / 열린 이슈 / 장애 / 결정 히스토리
- `context/topic-state/<slug>.md`
  - **지금 당장 복구용 압축 상태**

즉:
- Playbook = 헌법
- HF = 사건 파일
- Topic-state = 마지막 세이브 포인트

## 추천 운용 규칙
- 큰 전환점마다 `이 토픽 저장`
  - 목표 변경
  - 결론 확정
  - 다음 액션 바뀜
  - 파일 구조/경로 정리 완료
- 하루 종료 전 중요한 토픽 1~3개는 topic-state 갱신
- HF가 길어지면 topic-state는 더 짧고 날카롭게 유지

## 예시 호출
- `이 토픽 저장`
- `이 토픽 복구`
- `토픽 저장: x-post`
- `토픽 복구: random`

## 가드레일
- 복구 완료를 주장하기 전에 실제 참조 파일을 확인한다.
- topic-state가 낡았으면, 복구 응답에서 그 사실을 명시한다.
- 모호하면 slug를 1회만 확인 질문한다.
