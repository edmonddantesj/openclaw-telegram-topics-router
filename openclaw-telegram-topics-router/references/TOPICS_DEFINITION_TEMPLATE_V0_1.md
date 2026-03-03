# Telegram Forum Topics — Definition v0.1 (Template)

Goal: Topic별 대화/저장/자동화 룰을 가볍게 고정해서, 멘션 없이(always-on) 대화해도 자동 분류 + 올바른 행동을 하게 한다.

## Global rules (applies to all topics)
- Session routing key: `chat_id + message_thread_id`
- Storage: SSOT는 그대로 유지. 모든 레코드에 `topic=<topic_slug>` 태그 추가.
- Proof-first: 작업 결과는 가능한 한 파일 경로/로그/링크로 증빙.

---

## announcements
- 목적: 공지/결정/고정 링크.

## ops
- 목적: 서버/크론/게이트웨이/장애 대응.

## maintenance
- 목적: 리그레션/정리/의존성 업데이트/잡다한 수리.

## random
- 목적: 애매한 대화/임시 메모/잡담.

---

## Calibration procedure (one-time)
- 각 토픽에서 1회: `@<bot_username> ping`
- 그 메시지의 `message_thread_id`를 확인해 `thread_id → topic_slug` 매핑에 등록.
