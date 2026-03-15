# NEXUS Bazaar / The Archive — Resource Hub Expansion SSOT V0.1

Status: draft SSOT for durable product direction
Date: 2026-03-15

## Purpose

Capture the current agreed product direction so the ideas do not get lost between sessions.

This document is about the **resource hub / curation layer** around NEXUS Bazaar and The Archive, not the already-known runtime blocker on `public.listings`.

## Core direction

NEXUS Bazaar / The Archive should evolve into a **merchant + resource hub** that can:
- aggregate a creator/seller's external storefronts and public resources
- support user-submitted links and internal curated links
- surface trust/proof/review context
- gradually add community response layers such as likes and comments
- keep click-out / attribution / proof-first principles where appropriate

## Naming and section decisions

### 1) `Library` instead of `Longform`
- Do **not** define the writings section as `Longform`.
- Define it as **`Library`**.
- `Library` should cover curated books, essays, research posts, technical writings, documentation, and other high-quality readings.
- The intended feel is a **library / librarian / bookshelves / reading room** aesthetic rather than a generic blog list.

### 2) GitHub section publishing rule
- The Archive GitHub section should publish only the **GitHub-confirmed subset**.
- Minimum inclusion rule:
  - explicit URL exists
  - URL is clearly `github.com/...`
- Exclude:
  - missing URL
  - non-GitHub links
  - ambiguous references
- Current exporter artifact for this subset:
  - `artifacts/bazaar/github_reference_cards_github_only.json`

### 3) Public copy quality rule
- Do not bulk-publish Notion `Key Point` text directly when it includes internal evaluation tone.
- Internal phrasing such as GO/HOLD/adoption judgments/caution language must not leak into public cards.
- Preferred publishing rule:
  - triage into `public-ready / ambiguous / exclude`
  - refine public-safe summaries gradually
  - quality over speed

## Resource model direction

The Archive / Bazaar should support multiple resource families under one broader hub.

Planned families include:
- GitHub
- Bazaar-native listings
- ACP
- ClawHub
- Hackathon demos
- Library (curated writings / books / documents)

Recommended shared model:
- common `resource` layer
- source-specific metadata
- review / visibility / public-safe summary separation

Suggested high-level fields:
- `source` (`github|bazaar|acp|clawhub|hackathon|library|website`)
- `title`
- `summary_public`
- `summary_internal`
- `source_url`
- `status`
- `visibility`
- `tags`
- `category`
- `metadata jsonb`

## Library section direction

### What Library is
Library is the curated reading section of The Archive.

It should:
- introduce high-quality texts like a curated shelf
- send readers to original sources where possible
- allow curator framing / intro copy
- later support likes and comments

### Source-link recovery rule
For existing curated writing records where the original URL was not stored:
1. read title / summary / metadata from the current DB
2. search public web / X as needed to recover the original source URL
3. save recovered source URL into the DB
4. only expose verified entries publicly

## Community response layer

### Likes / hearts
A lightweight response layer is desired across all major resource types.

Target types:
- GitHub
- Bazaar listings
- ACP
- ClawHub
- Hackathon demos
- Library entries

Recommended v1:
- one heart/like reaction type
- count visible on cards/detail pages
- sorting/ranking can later use reaction counts

Suggested data shape:
- `resource_reactions`
  - `resource_id`
  - `user_id`
  - `reaction_type`
  - `created_at`

### Comments / recommendations
Comments are desirable, but should launch more conservatively than likes.

Recommended rollout:
- v1: comment submission + moderation queue
- v2: approved comments visible publicly
- v3: richer recommendation/discussion features

Suggested constraints:
- short recommendation-style comments first
- moderation required before public display
- anti-spam / anti-abuse rules from the start

Suggested data shape:
- `resource_comments`
  - `resource_id`
  - `user_id`
  - `body`
  - `status` (`pending|approved|hidden`)
  - `created_at`

## Merchant/storefront alignment

This expansion is compatible with the older merchant-hub direction from prior Bazaar work:
- creators/sellers can have multiple external storefronts
- Bazaar can act as the discovery / curation / trust / attribution layer
- click-out remains the default safe mode for external platforms

This means GitHub / ClawHub / ACP / Library do not need to be treated as disconnected features.
They can be part of one broader hub architecture.

## Implementation order (agreed preference)

Do this sequentially, not all at once.

Recommended order:
1. design/confirm the shared DB model in Supabase
2. keep GitHub confirmed subset flow as the first working intake path
3. add `Library` as the curated reading section
4. add likes/hearts
5. add moderated comments
6. later improve ranking/discovery with reaction data

## Hackathon curation direction

Hackathons should become a first-class curation lane.

### Collection policy
- The default curation focus is **hackathon winners / awarded projects**.
- Over time, The Archive may also include selected non-winning but high-quality entries when:
  - planning was unusually strong
  - implementation quality was strong
  - proof/demo quality was notable
  - the build is worth preserving as a reference despite not winning

### Research workflow
- Heukmyo team should be used as an ongoing research/support source for hackathon discovery.
- Expected loop:
  1. Heukmyo team researches hackathon projects continuously
  2. findings are stored in Supabase as internal records
  3. records are reviewed/curated
  4. qualified entries are published to The Archive

### Publish rule
- Store broadly in DB.
- Publish narrowly on the public surface.
- Public labels for non-winning but curated entries can later include ideas such as:
  - `Editor's Pick`
  - `Notable Build`
  - `Worth Watching`

## Promotion timing rule

Official promotion from Mercedes's own public account should **not** happen yet.

Promotion should start only once The Archive reaches roughly an **alpha-to-beta** shape where the core world and major sections are visibly real.

### Practical launch gate
Before official public promotion, aim to have most of the following present:
- GitHub section working with confirmed subset
- ACP section visible
- ClawHub section visible
- Hackathon section started
- Library section started
- public-safe summaries/copy in place
- basic review/curation flow working
- overall presentation coherent enough to feel like one world rather than scattered experiments

## Current product philosophy

- Reuse the real body of work already created with Mercedes and AOI systems.
- Prefer durable internal systems over one-off manual curation.
- Preserve public-safe separation from internal evaluation language.
- Build gradually; do not rush bulk publishing.
- Favor beautiful worldbuilding where it helps product coherence (Archive + Library + merchant/resource hub).
- Delay official promotion until the Archive feels sufficiently whole.
