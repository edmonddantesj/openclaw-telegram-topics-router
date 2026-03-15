# OpenAI_v1 Auto Routing Policy (v0.1)

Goal: automatically route *coding* turns to a stronger Codex model, while keeping normal ops/chat on a cheaper default.

## Default (non-coding)
- Model: `openai-codex/gpt-5.2`

## Coding turns (auto)
- Primary: `openai-codex/gpt-5.3-codex-spark`
- Fallback on quota/rate/availability errors: `openai-codex/gpt-5.2-codex`

## Coding classification (broad)
Treat as coding if the user message includes any of:
- code blocks, stack traces, error logs
- file paths / diffs / PR requests
- keywords: implement, refactor, debug, stack trace, module, API integrate

No special exception: if it smells like coding, route to Spark.

## Operational note
This is applied by the agent automatically; the user does not need to ask.
