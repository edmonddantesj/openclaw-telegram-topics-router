# MAC_MINI_INCIDENT_RUNBOOK_V0_1.md

## 목적
맥미니에서 OpenClaw, Bitcoin node, 외장 SSD, sleep/wake 관련 문제가 섞여 보일 때 우선순위를 잃지 않고 대응하기 위한 incident runbook.

---

## 0. 상황 정의
다음 증상이 보이면 이 런북을 사용한다.
- Telegram 응답이 끊김
- OpenClaw가 갑자기 응답 안 함
- Gateway/Node가 재시작됨
- 맥미니 자체가 다운되거나 재부팅됨
- Bitcoin node 오류가 동시에 증가함

---

## 1. 1차 분류
질문은 하나다.

### Q1. 맥미니 자체가 재부팅/다운/잠김 되었나?
확인:
```bash
uptime
last reboot | head -n 5
```

- **Yes** → OpenClaw 문제보다 **호스트 incident** 로 본다.
- **No** → OpenClaw/gateway/channel incident로 본다.

---

## 2. 호스트 incident 대응
### Step A. 공통 원인부터 의심
우선순위:
1. 외장 SSD / USB / 마운트 / I/O stall
2. sleep/wake / power management
3. 디스크/메모리 압박
4. 특정 프로세스 폭주

### Step B. 빠른 상태 수집
```bash
df -h /
pmset -g assertions
pmset -g log | tail -n 200
openclaw status
```

### Step C. 운영 판단
- OpenClaw와 Bitcoin node가 **같이** 흔들리면 공통 저장경로/외장 SSD를 우선 의심
- 외장 SSD를 live storage로 쓰고 있다면 내부 SSD로 롤백 우선

---

## 3. OpenClaw incident 대응
확인:
```bash
openclaw status
tail -n 120 ~/.openclaw/logs/gateway.log
tail -n 120 ~/.openclaw/logs/gateway.err.log
tail -n 120 ~/.openclaw/logs/node.err.log
```

중점 패턴:
- `sendMessage failed`
- `Polling stall detected`
- `signal SIGTERM received`
- `shutdown timed out`

해석:
- Telegram 전송 실패만 있으면 channel/network 쪽 우선
- SIGTERM + restart가 보이면 supervisor/서비스 재기동 포함해서 본다

### alive but unhealthy 판정
다음을 만족하면 프로세스는 살아 있어도 서비스는 비정상으로 본다.
- `openclaw status` 상 gateway/node는 running인데 실제 메시지 응답이 없음
- Telegram 쪽 polling/send 실패가 반복됨
- node가 gateway reconnect만 반복하거나 `ECONNREFUSED 127.0.0.1:18789`가 보임
- stale lock/session 찌꺼기 흔적이 보임

### doctor 실행 기준
다음 조건이면 `openclaw doctor --fix`를 빠른 복구 수단으로 고려한다.
- 호스트는 살아 있고 `openclaw status`도 응답하지만 실제 대화 응답이 멈춤
- 최근 로그에 polling stall / sendMessage failed / shutdown timed out / reconnect loop가 섞여 있음
- 마지막 큰 변경(예: 저장경로 변경)은 이미 롤백했는데도 OpenClaw 내부 상태만 꼬여 보임

주의:
- `doctor --fix`는 근본 원인 분석을 대체하지 않는다.
- 호스트 kernel panic / 재부팅 원인이 있으면 먼저 상위 원인을 따로 추적한다.

---

## 4. 롤백 우선 원칙
문제가 새 변경 이후 시작됐으면:
- 분석보다 먼저 **마지막 큰 변경점**을 의심한다
- 특히 저장경로 / symlink / 외장스토리지 / 자동화 추가는 우선 롤백 후보

현재 known-good 운영 원칙:
- `~/.openclaw/media` = 내부 SSD
- `~/workspace/media` = 내부 SSD
- 외장 SSD = 다운로드 / 아카이브 전용

---

## 5. 재발 방지 원칙
- live runtime storage는 내부 SSD 우선
- 외장은 archive/download 용도만
- 새 구조를 넣을 때는 한 번에 크게 바꾸지 말고 A/B로 확인
- 안정성 문제는 먼저 런북으로 고정하고, 반복 패턴이 생기면 그때 스크립트/스킬화

---

## 6. 사건 종료 조건
다음을 만족하면 incident 종료로 본다.
- 최근 재부팅 없음
- OpenClaw 응답 정상
- Telegram 응답 정상
- Bitcoin node 오류 감소 또는 정상화
- 외장 SSD 연관 live path 제거/격리 완료
