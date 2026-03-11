# MAC_MINI_STABILITY_CHECKLIST_V0_1.md

## 목적
맥미니 호스트가 갑자기 끊기거나 재부팅되거나, OpenClaw/노드/외장 SSD 관련 이상징후가 있을 때 빠르게 상태를 확인하기 위한 운영 체크리스트.

핵심 원칙:
- 먼저 **호스트 자체 문제인지** 확인한다.
- 그 다음 **OpenClaw/gateway/node** 문제를 확인한다.
- 마지막에 **외장 SSD / live media 경로 / 다운로드 경로**를 확인한다.

---

## 1. 호스트 생존 확인
아래를 먼저 본다.

```bash
uptime
last reboot | head -n 5
```

판단:
- 최근 `reboot`가 여러 번 있으면 OpenClaw 단독 장애가 아니라 **호스트 재부팅 문제**로 본다.
- uptime이 짧으면 방금 재기동된 것일 수 있다.

---

## 2. OpenClaw 서비스 확인
```bash
openclaw status
```

필수 확인:
- Gateway service = running
- Node service = running
- Telegram channel = reachable / WARN 여부

로그 빠른 확인:
```bash
tail -n 80 ~/.openclaw/logs/gateway.log
tail -n 80 ~/.openclaw/logs/gateway.err.log
tail -n 80 ~/.openclaw/logs/node.err.log
```

중점 키워드:
- `signal SIGTERM received`
- `shutdown timed out`
- `sendMessage failed`
- `Polling stall detected`
- `ECONNREFUSED 127.0.0.1:18789`

---

## 3. 디스크 / 메모리 압박 확인
```bash
df -h /
vm_stat | head -n 20
ps -axo pid,%cpu,%mem,rss,comm | sort -k3 -nr | head -n 15
```

판단:
- `/` 사용률이 매우 높으면 저장공간 압박 의심
- 특정 프로세스가 CPU를 과도하게 오래 잡으면 시스템 불안정 원인 후보로 기록

---

## 4. 재부팅/절전 흔적 확인
```bash
pmset -g assertions
pmset -g log | tail -n 200
```

중점 확인:
- `ExternalMedia`
- 절전 방지 assertion 과다
- sleep/wake 직후 문제 반복 여부
- 외장 저장장치(owner / device)가 계속 assertion을 잡는지

---

## 5. 외장 SSD 연관성 확인
현재 운영 원칙:
- **live OpenClaw media는 내부 SSD 유지**
- 외장 SSD는 **다운로드/아카이브 전용**

확인:
```bash
ls -ld ~/.openclaw/media ~/workspace/media
readlink ~/.openclaw/media || true
readlink ~/workspace/media || true
```

판단:
- symlink가 외장 SSD를 가리키면 live media가 다시 외장으로 간 상태일 수 있음
- 내부 디렉터리면 현재 운영 원칙 준수 상태

---

## 6. 즉시 대응 분기
### A. 호스트가 최근 재부팅됨
- OpenClaw만의 문제가 아니므로 호스트 문제로 분류
- 외장 SSD / 전원 / 절전 / sleep-wake부터 의심

### B. 재부팅은 없고 gateway만 흔들림
- Telegram polling/network 문제 우선 확인
- gateway.log / gateway.err.log 중심으로 본다

### C. Bitcoin node까지 같이 흔들림
- 공통 저장장치/공통 I/O 경로 문제 가능성 우선
- 외장 SSD 의존 경로를 먼저 의심

---

## 7. 운영 원칙
- 외장 SSD는 **실시간 런타임 저장소**가 아니라 **다운로드/보관소**로 취급한다.
- 안정성 이슈가 있을 때는 새 기능보다 **롤백과 A/B 확인**을 먼저 한다.
- “원인 미확정 상태의 자동화/스킬화”보다 **런북과 점검 절차**를 먼저 다듬는다.
