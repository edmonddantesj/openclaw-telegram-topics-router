# Delegation Policy (Telegram Topics) — v0.1

## Mode

- **MODE: B (auto-delegate by default)**
  - Default behavior: when a meaningful request arrives in a topic thread, route to the thread’s Primary owner (and optionally collaborators) automatically.

## Noise filters (anti-spam)

Auto-delegation triggers only when the message contains at least one of:

- A question / request for action
- A task instruction / decision request
- A log excerpt / error report
- A link + instruction to review

Otherwise: ignore or wait for explicit `#call/#council/#all-hands`.

## Cooldown (batching)

- **Thread cooldown: 180 seconds**
  - During cooldown, new messages are buffered and handled in a single batch.

## L3 guardrails (fail-closed)

Auto-delegation must **not** execute or approve anything that is L3-sensitive. If a message implies any of:

- Money movement / transfers / payouts
- Signing / private keys / seeds
- On-chain LIVE actions
- External publishing (posts/comments) without explicit approval
- Secrets / API keys / credentials

Then:

- **Do not auto-execute.**
- Escalate to **청묘** (and request explicit confirmation).

## Response style

- **Style: human** (사람 말투 유지)
- Optional short header line is allowed when helpful (e.g., 담당 표시), but avoid rigid bot templates.
- Structured artifacts (decisions/next actions) should be written to the **handoff** topic when needed.
- Do not acknowledge and stall: if a task is executable within L1/L2 boundaries, execute it promptly and report after.
- If execution cannot start immediately, convert it into an explicit tracked artifact instead of leaving it implicit.

## Attendance commands

- Attendance commands remain manual human triggers:
  - `#call ...`
  - `#council core|market`
  - `#all-hands` (only for full-team opinion requests)

## Expansion / extra attendance (assignment)

- Trigger: user command (attendance commands above).
- When triggered, **청령** acts as dispatcher: decides who to add and assigns roles per topic context.

## Notes

- This is a policy SSOT. The runtime router/execution layer must implement it.
- Roster SSOT: Notion Squad Dashboard (page id `3049c616-de86-81a3-8420-e9a6188d96f6`).
- Topic/thread SSOTs:
  - `context/telegram_topics/thread_topic_map.json`
  - `context/telegram_topics/thread_agent_map.json`
