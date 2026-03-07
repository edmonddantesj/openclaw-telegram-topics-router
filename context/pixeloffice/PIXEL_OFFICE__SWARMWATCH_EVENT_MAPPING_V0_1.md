# PixelOffice ↔ SwarmWatch Event Mapping V0.1 (Draft SSOT)

목적: PixelOffice(운영 UI)가 HF/Playbook/자동화(launchd/Ralph Loop) 상태를 **SwarmWatch식 “정규화 이벤트”**로 받아서 실시간 오버레이/승인게이트까지 제공할 수 있게 하는 매핑 SSOT.

참고: SwarmWatch normalized event: `agent_state` (Runner → Local control plane → UI)
- keying: `agentKey = agentFamily:agentInstanceId`
- transport: localhost HTTP + WebSocket

---

## 1) Core Entities (PixelOffice)
- **Work Item:** HF 문서 1장 (예: `context/handoff/HF_acp_ops_202603.md`)
- **Rule/Checklist:** Playbook (예: `context/topics/acp_PLAYBOOK_V0_2.md`)
- **Automation:** launchd job / Ralph Loop task
- **Proof:** URL / log path / file path / tx hash

---

## 2) Normalized Event Schema (PixelOffice v0)
SwarmWatch를 그대로 쓰지 않아도, 아래 필드 세트로 호환 레이어를 둔다.

```ts
// PixelOfficeNormalizedEvent (v0)
{
  type: 'agent_state',
  agentFamily: 'pixeloffice',
  agentInstanceId: string,     // e.g. 'hf:acp_ops_202603' | 'launchd:com.aoineco.acp.weekly_dispatch'
  agentName: string,           // e.g. 'HF ACP Ops' | 'launchd weekly_dispatch'
  state: 'idle'|'thinking'|'reading'|'editing'|'awaiting'|'running'|'error'|'done'|'inactive',
  detail?: string,             // human-readable summary
  hook?: string,               // e.g. 'hf_update' | 'launchd_tick' | 'approval_required'
  projectName?: string,        // optional: 'aoineco'
  ts: number                   // epoch seconds
  // + optional extensions:
  meta?: {
    hfPath?: string,
    playbookPath?: string,
    proof?: { kind: 'url'|'path'|'tx'|'log', value: string }[],
    approval?: { required: boolean, reason?: string, scope?: 'buy'|'onchain'|'publish'|'secret'|'other' }
  }
}
```

---

## 3) Mapping Table (SSOT)

### A) HF(진행중 작업) → agent_state
| PixelOffice source | agentInstanceId | state mapping | detail | hook | proof |
|---|---|---|---|---|---|
| HF header(Status/Last updated) | `hf:<slug>` | ACTIVE→running / HOLD→idle / DONE→done | HF Goal/Next 1줄 | `hf_update` | HF 내 Commands/paths/proofs |

권장 slug 규칙: 파일명 `HF_<slug>.md`에서 `<slug>` 사용.

### B) Playbook(규칙/반복업무) → agent_state
| source | agentInstanceId | state | detail | hook |
|---|---|---|---|---|
| Playbook 변경/버전업 | `playbook:<topic>` | editing | 변경 요약 | `playbook_update` |

### C) launchd(리마인더/잡) → agent_state
| source | agentInstanceId | state | detail | hook | proof |
|---|---|---|---|---|---|
| launchd tick | `launchd:<label>` | running→done | 실행 메시지 1줄 | `launchd_tick` | stdout/stderr log path |
| launchd error | `launchd:<label>` | error | exit code + stderr tail | `launchd_error` | stderr log path |

### D) Approval Gate(승인 필요 이벤트) → awaiting
| trigger | agentInstanceId | state | detail | hook | meta.approval |
|---|---|---|---|---|---|
| buy/onchain/publish/secret 등 | `gate:<scope>:<id>` | awaiting | “승인 필요: <scope>” | `approval_required` | `{required:true, scope, reason}` |

---

## 4) Approval UX (PixelOffice)
- UI는 `awaiting` 상태인 항목을 별도 큐로 보여주고 Approve/Decline 제공
- Fail-open/Timeout 정책은 운영 성격에 따라 다르게:
  - **secret/publish/onchain:** timeout 시 **deny(또는 hold)**
  - **read-only/status ping:** timeout 시 **allow(fail-open)**

---

## 5) MVP Implementation (권장)
1) 이벤트 발행기: (간단) Python/Node watcher가
   - HF 파일 변경 감지
   - launchd 로그 append 감지
   - 승인 게이트 이벤트 수동 생성
2) localhost control plane: `/event`(ingest) + `ws://...` broadcast
3) PixelOffice overlay: orbit/agent list + approvals queue + HF deep-link 버튼

---

## 6) Notes
- 본 문서는 **픽셀오피스가 SwarmWatch의 장점(정규화/오버레이/승인게이트)을 흡수**하기 위한 매핑 SSOT이다.
- 실제 SwarmWatch를 포크할지/유사 구조를 구현할지는 별도 결정.
