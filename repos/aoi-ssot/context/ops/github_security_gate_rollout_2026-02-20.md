# AOI Security Gate rollout (edmonddantesj) — 2026-02-20

목표: 10개 레포에 **AOI Security Gate** 적용 (Pre-push hook + GitHub Actions CI).

원칙:
- 기본 브랜치 직접 푸시 금지 → `chore/aoi-security-gate` 브랜치에서 PR.
- 적용 전 /tmp 클론 후 gate 스캔으로 예상 신호/주요 findings 기록.
- 템플릿 소스: `/Users/silkroadcat/dev/eigenproof-runner`.
- `aoi-core/state/{approvals,proofs,ci_artifacts}` 는 gitignore + git 미추적으로 유지.

---

## Rollout summary (table)

| Repo | Visibility | Default branch | Existing CI? | Pre-scan signal | Applied? | PR |
|---|---:|---|---:|---:|---:|---|
| eigenproof-runner | PUBLIC | main | yes | green | no-op | - |
| aoi-skills | PUBLIC | main | yes | yellow | yes | https://github.com/edmonddantesj/aoi-skills/pull/9 |
| bnb-goodvibes-dex-agent | PUBLIC | main | yes | red | yes | https://github.com/edmonddantesj/bnb-goodvibes-dex-agent/pull/16 |
| x402-stacks-mvp | PUBLIC | main | no | green | yes | https://github.com/edmonddantesj/x402-stacks-mvp/pull/1 |
| alpha-tracker-v2 | PRIVATE | master | yes | green | yes | https://github.com/edmonddantesj/alpha-tracker-v2/pull/4 |
| the-alpha-oracle | PRIVATE | master | yes | yellow | yes | https://github.com/edmonddantesj/the-alpha-oracle/pull/4 |
| 7-dollar-bootstrap-x402 | PUBLIC | main | yes | red | yes | https://github.com/edmonddantesj/7-dollar-bootstrap-x402/pull/4 |
| aoi-squad-orchestrator-pro | PRIVATE | main | yes | yellow | yes | https://github.com/edmonddantesj/aoi-squad-orchestrator-pro/pull/4 |
| tempo-budget-guardian-agent | PUBLIC | main | yes | red | yes | https://github.com/edmonddantesj/tempo-budget-guardian-agent/pull/4 |
| solana-sentinel | PUBLIC | main | yes | green | yes | https://github.com/edmonddantesj/solana-sentinel/pull/1 |

---

## Repo details

### edmonddantesj/eigenproof-runner
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=green score=100 max_severity=info
- Stack/lockfiles:

```
stack=python
lockfiles_present=uv.lock
```
- Applied: no-op
- PR: (none)

### edmonddantesj/aoi-skills
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=yellow score=75 max_severity=med
- Pre-scan findings (top):

```
- [med] repro.lockfile.missing: No common lockfile detected (reproducibility risk).
```
- Stack/lockfiles:

```
stack=python
lockfiles_present=none
```
- Applied: yes
- PR: https://github.com/edmonddantesj/aoi-skills/pull/9

### edmonddantesj/bnb-goodvibes-dex-agent
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=red score=0 max_severity=high
- Pre-scan findings (top):

```
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file README.md.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file manifest.json.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file AUTONOMOUS_LOG.md.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file reports/run_20260214_192247_baseline_live.json.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file docs/proofs/run_20260216_181521_aggro_rebalance_live.json.
```
- Stack/lockfiles:

```
stack=python,node
lockfiles_present=package-lock.json
```
- Applied: yes
- PR: https://github.com/edmonddantesj/bnb-goodvibes-dex-agent/pull/16

### edmonddantesj/x402-stacks-mvp
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: no
- Pre-scan: signal=green score=100 max_severity=info
- Stack/lockfiles:

```
stack=python,node
lockfiles_present=package-lock.json
```
- Applied: yes
- PR: https://github.com/edmonddantesj/x402-stacks-mvp/pull/1

### edmonddantesj/alpha-tracker-v2
- Visibility: PRIVATE
- Default branch: master
- Existing CI workflows: yes
- Pre-scan: signal=green score=100 max_severity=info
- Stack/lockfiles:

```
stack=python,node
lockfiles_present=package-lock.json
```
- Applied: yes
- PR: https://github.com/edmonddantesj/alpha-tracker-v2/pull/4

### edmonddantesj/the-alpha-oracle
- Visibility: PRIVATE
- Default branch: master
- Existing CI workflows: yes
- Pre-scan: signal=yellow score=75 max_severity=med
- Pre-scan findings (top):

```
- [med] repro.lockfile.missing: No common lockfile detected (reproducibility risk).
```
- Stack/lockfiles:

```
stack=python
lockfiles_present=none
```
- Applied: yes
- PR: https://github.com/edmonddantesj/the-alpha-oracle/pull/4

### edmonddantesj/7-dollar-bootstrap-x402
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=red score=0 max_severity=high
- Pre-scan findings (top):

```
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file README.md.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file manifest.json.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file proof/RELAI_X402_PROOF.md.
```
- Stack/lockfiles:

```
stack=python,node
lockfiles_present=package-lock.json
```
- Applied: yes
- PR: https://github.com/edmonddantesj/7-dollar-bootstrap-x402/pull/4

### edmonddantesj/aoi-squad-orchestrator-pro
- Visibility: PRIVATE
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=yellow score=75 max_severity=med
- Pre-scan findings (top):

```
- [med] repro.lockfile.missing: No common lockfile detected (reproducibility risk).
```
- Stack/lockfiles:

```
stack=python
lockfiles_present=none
```
- Applied: yes
- PR: https://github.com/edmonddantesj/aoi-squad-orchestrator-pro/pull/4

### edmonddantesj/tempo-budget-guardian-agent
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=red score=0 max_severity=high
- Pre-scan findings (top):

```
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file memory_track3_proofs_latest.md.
- [high] secrets.pattern.match: Potential secret detected (PRIVATE_KEY_HEX) in file README.md.
```
- Stack/lockfiles:

```
stack=python,node
lockfiles_present=package-lock.json
```
- Applied: yes
- PR: https://github.com/edmonddantesj/tempo-budget-guardian-agent/pull/4

### edmonddantesj/solana-sentinel
- Visibility: PUBLIC
- Default branch: main
- Existing CI workflows: yes
- Pre-scan: signal=green score=100 max_severity=info
- Stack/lockfiles:

```
stack=python,node,rust
lockfiles_present=package-lock.json,Cargo.lock
```
- Applied: yes
- PR: https://github.com/edmonddantesj/solana-sentinel/pull/1

