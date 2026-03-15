# TOPIC PARALLEL SUMMON POLICY V0.1

## Goal
Ensure that topic-bound owner agents can directly summon other team agents in parallel when discussion, review, or cross-functional consensus is needed.

## Effective date
2026-03-15

## Scope
All Telegram topic-bound owner agents configured in `~/.openclaw/openclaw.json`.

## Runtime rule
Each topic owner agent should be allowed to spawn/summon other agents directly.
Configured rule:

```json
"subagents": {
  "allowAgents": ["*"]
}
```

## Why this was needed
Observed failure mode:
- `main` could summon multiple agents
- `analyzer@topic55` could not
- practical symptom: owner fell back to single-agent/manual roundtable instead of true parallel summon

Root cause:
- `main` explicitly had `subagents.allowAgents: ["*"]`
- topic-bound agents such as `analyzer` did not
- therefore agent summon visibility/capability differed by requester session

## Policy decision
- All topic owner agents should have the same summon capability baseline as `main`.
- "Do not split into clone-shards" means do not fake multi-agent discussion by spawning many copies of the same agent.
- It does **not** forbid summoning distinct real agents for bounded parallel review.

## Operational interpretation
When a user asks in-topic:
- `토론해줘`
- `같이 논의해줘`
- `병렬로 봐줘`
- `팀원 불러서 봐줘`
- or explicitly names 2+ agents

The topic owner should be allowed to:
1. summon relevant real agents
2. run bounded parallel review
3. return a consensus summary

## Recommended output shape
1. Participants
2. Key issues
3. Consensus / conclusion
4. Next action

## Guardrails
- No clone-shard discussions using multiple copies of the same agent
- No uncontrolled broad fan-out
- Prefer small bounded sets (2~4 agents)
- L3/human-gate actions remain unchanged
