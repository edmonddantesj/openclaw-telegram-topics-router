# DM_BACKUP_CHEONGMYO_1TO1_20260310

- label: DM_BACKUP_CHEONGMYO_1TO1_20260310
- source: B / upstream-context
- topic_key: RANDOM
- treatment: proposal_only for topic-directly-relevant items
- mode: COLLECT_NORMALIZE_PROPOSE

## Decisions (upstream-context, not direct apply)
1. 전체 토픽 운영에서 Random(81)을 포함한 포럼 토픽 맵과 일괄 compact 대상에 random=81이 포함되어야 한다.
   - source_ref: B2/messages.html excerpt matched by search: "random = 81"
2. 토픽 협업 체계에서 Random도 다른 토픽처럼 handoff/SSOT/Playbook 체계의 대상이다.
   - source_ref: B2/messages.html excerpts around "각 토픽의 작업은 HF로 '토픽별로' 관리" and playbook references

## Tasks (upstream-context, not direct apply)
1. 각 토픽 백업 수신 시 Playbook 업데이트, 필요시 HF 생성/업데이트, 반복업무 자동화 후보 추출.
   - topic relevance to Random: direct, because Random is part of whole-topic policy.
   - source_ref: B2/messages.html excerpts around "이 백업을 기준으로... Playbook... HF... 자동화"
2. 전 토픽 공지/협업 규칙/announcements canonical을 기준으로 운영하고, 토픽별 START HERE 또는 로컬 SSOT로 복구 가능하게 유지.
   - topic relevance to Random: direct as operating context.
   - source_ref: B2/messages.html excerpts around announcements canonical and START HERE

## Deliverables (upstream-context, not direct apply)
1. context/topics/<slug>_PLAYBOOK_V0_1.md 체계
   - source_ref: B2/messages.html excerpt around "context/topics/<slug>_PLAYBOOK_V0_1.md"
2. context/handoff/HF_<slug>.md 체계
   - source_ref: B2/messages.html excerpt around "context/handoff/HF_<slug>.md"
3. context/telegram_topics/ANNOUNCEMENTS_CANONICAL_V0_1.md canonical reference
   - source_ref: B2/messages.html excerpt around canonical announcements path

## Status
- upstream_context_present: yes
- directly_random_relevant_items_found: yes
- promoted_to_truth: no
- proposal_only: yes

## Uncertain
- DM export is HTML pages only; exact timestamps/message IDs for every extracted policy snippet were not normalized in this pass.
- 일부 excerpt는 전토픽 공통 정책이라 Random 직접 적용 여부는 별도 검토 필요.
