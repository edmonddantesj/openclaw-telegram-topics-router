# EigenCloud / EigenCompute — Open Innovation Challenge (Draft v0.1)

> Constraint: **No tokenized agents**
> Deadline: **Feb 20, 11:59pm PT**
> Required: demo link + repo link + announcement tweet (tag @eigencloud)

## Project
- **Project name:** EigenProof Runner (Aoineco)
- **One-line description:** A verifiable agent runner that produces a proof-first bundle (manifest + sha256) for every container execution on EigenCompute.

## How did you use EigenCompute/EigenCloud?
We packaged our “proof-first” pipeline into a Docker workload and ran it on EigenCompute.
Each run emits a verifiable bundle:
- `input.json` (work request)
- `output.json` (deterministic result for the demo)
- `manifest.json` that records:
  - SHA256 hashes of inputs/outputs
  - code version (git commit baked into container; stored as `runtime.git_commit`)
  - runtime metadata (timestamp, environment)

This makes agent execution auditable and reproducible: anyone can re-run the container and verify integrity by recomputing hashes.

## Demo link (placeholder)
- (TODO) YouTube demo: <ADD_LINK>

## Repo link
- GitHub repo: https://github.com/edmonddantesj/eigenproof-runner
- Submission form: https://docs.google.com/forms/d/e/1FAIpQLSdjCpocv1HibJOEMLtxBxbxleMOZoUIXSmUOT-B1QSv-7HLPg/viewform?pli=1

## Tweet announcement (draft)
Tweet draft (EN):

> Shipping our first EigenCompute build: **EigenProof Runner** — a proof-first agent runner that emits a verifiable bundle (manifest + sha256) for every container execution.
> 
> ✅ No tokenized agents. Just utility + verifiability.
> 
> Demo: <LINK>
> Repo: <LINK>
> 
> @eigencloud

## Optional Roadmap (B)
If time allows, extend A → B:
- **Verifiable Agent Identity Wrapper**: prove code + data + upgrade policy + state continuity (fail-closed) on top of the proof bundle runner.

## Form fields checklist
- Name: (Edmond)
- X handle: (Edmond)
- Email: (Edmond)
- Project name: EigenProof Runner (Aoineco)
- One-line description: (above)
- How used EigenCompute/EigenCloud: (above)
- Demo link: TODO
- Tweet link: https://x.com/edmond_dantes_j/status/2024363616930320385?s=20
