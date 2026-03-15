# Peter Steinberger 툴셋 도입 검토 (v0.1)

## 결론
- 즉시 도입: 이미 보유/필수 기반 + 즉시 생산성 개선 가능군
- 단기 도입: 1~2주 내 점진 내재화 권장
- 조건부/보류: 보안/비공개/의존성 체크 후 승인

## 분류 A (즉시 활용 / 이미 보유 또는 연동 쉬움)
- `bird` (X 빠른 CLI)
- `oracle` (문맥 질의용)
- `claude-code` (에이전트 강화)
- `tmux` (터미널 멀티태스킹)
- `x-research` (X/트윗 모니터링)
- `usage` (사용량 추적)
- `swarm-kanban` (실행/우선순위)
- `agent-chat` (대화 연동)

## 분류 B (내재화 우선도 높음)
- `CodexBar` : 토큰·비용 거버넌스 가시성
- `peekaboo` : 스크린샷/증빙 자동화, GUI 제어
- `summarize` : 장문 요약 속도
- `VibeTunnel` : 브라우저 제어 루프 고도화
- `remindctl` : 루틴/알림 자동화
- `imsg` : 메시지 아웃바운드 정교화
- `camSnap` : CCTV 스냅샷/감시 루프
- `macOS Automator MCP` : macOS 제어 자동화
- `Claude Code MCP` : MCP 기반 에이전트 상호작용
- `AXorcist` : 접근성 자동화

## 분류 C (조건부 / 보류)
- `SweetCookie` / `SweetCookieKit` : 쿠키 추출(보안 리스크 큼)
- `bird` (비공개 특성으로 배포·의존성 관리 위험)
- `Twitt* 계열 연동` : 접근성/규제 변경 가능성 검토 필요
- `ElevenLabs 관련 음성툴` : 개인 음성 사용 정책/비용 구조 확인 후
- `sonoscli/spogo`(오디오 제어) : 사용빈도 낮으면 후순위
- `homebrew-tap`, `ordercli`, `mcporter`, `go-cli`, `goplaces` : PoC 후 우선도 재평가

## 내재화 체크리스트 (모든 신규 툴 공통)
1) Secret/권한은 로컬 격리
2) 최소 권한 실행
3) 실패·재시작 전략(자동복구) 정의
4) 월 1회 보안 감사
5) Notion/Local SSOT에 사용 로그 남기기

## 다음 단계 제안
- 1주차: B군 1차 도입(P0 5개) + 리포트
- 2주차: 운영 지표(시간절약/실패율/장애건수) 비교 후 C군 Go/No-Go
- AOI Ops 카드 2개 추가: `SteiPete Toolset POC` / `Toolset Security Review`
