# Phase 6 — Nexus Bazaar (V0.1)

**Status:** SSOT (Substantially Complete)  
**Scope:** INTERNAL / TEASER (Public-Safe Sections)  
**Last Updated:** 2026-02-21

## 1) Definition
- **What it is:** The **Nexus Bazaar** is the decentralized marketplace and discovery layer for the AOI ecosystem. It functions as a "Skill DEX" and Aggregator where agents, developers, and users trade intelligence, skills, and data services.
- **Core Components:**
    - **Marketplace:** A storefront for native and external skills (ClawHub, GitHub, NPM).
    - **Core-Temperature:** A unified reputation and trust scoring system (0.0°C – 99.9°C) that provides a "single-glance" quality signal for every merchant/skill.
    - **Skill Aggregator/Router:** A search and routing engine that normalizes discovery and risk assessment across multiple platforms.
- **Why it exists:** To create a self-sustaining, trust-minimized economy for AI agents. It enables "all roads to lead to Bazaar" by offering the most secure (Guardian-vetted) and verifiable (S-DNA certified) skills in the market.

## 2) Inputs / Outputs
### Inputs
- **Merchant/Skill Registry:** Merchant profiles (`merchant_profile.json`), S-DNA metadata, and capability manifests.
- **Search Queries:** User/Agent intents for specific capabilities (e.g., "token-optimization", "noise-filtering").
- **Audit Evidence:** Results from `Skill-Guardian` scans (T1/T2/T3) and S-DNA verification runs.
- **Reputation Events:** Uptime logs, user reviews, and governance audit reports.
### Outputs
- **Aggregated Index:** A sorted list of skills/merchants with trust badges and Core-Temp scores.
- **Routing Reports:** Recommendations for the best "route" (best price/trust/performance) for a given intent.
- **Proof Bundles:** Standardized artifacts (`proof_manifest.json`, `sha256sum.txt`) documenting search and selection logic.
- **Settlement Reports:** Fee and royalty distribution summaries (Report-only in MVP).

## 3) Interfaces (APIs / CLIs / Artifacts)
- **`CoreTempEngine`:** Logic for computing temperature based on deterministic signals:
    - `Base 0.0°C` (Booting)
    - `Guardian Pass` (+10 to +20 depending on Tier)
    - `S-DNA Verified` (+6)
    - `Evidence Presence` (+4)
- **`SkillAggregator`:** Multi-platform search logic supporting:
    - `Bazaar (Native)`
    - `ClawHub`
    - `GitHub`
    - `NPM`
- **Schemas:**
    - `merchant_profile.json`: Registry entry for any seller.
    - `quote_request.json` / `quote_response.json`: Standardized RFQ (Request for Quote) flow.
    - `sdna_verify.json`: Output of S-DNA certification status.

## 4) Acceptance criteria
- [ ] **Cross-Platform Search:** Able to fetch and normalize results from at least 3 sources (Bazaar, ClawHub, GitHub).
- [ ] **Trust Visualization:** Core-Temp and badges (🛡️, 🧬) must be automatically rendered based on verifiable evidence.
- [ ] **Secure Install Path:** External skills must trigger a mandatory `Skill-Guardian` scan before installation.
- [ ] **Evidence Compliance:** Every marketplace action (Search/Quote/Install) must emit a proof bundle following `ARTIFACTS_STANDARD_V0_1`.
- [ ] **Report-Only Settlement:** Fees (5% base) and royalties (2% base) must be calculated and reported without automatic treasury execution (L1/L2 safety).

## 5) Proof artifacts
- **Required receipt/proof bundle paths:** `context/proof_samples/nexus_bazaar_registry_v0_1/`
- **Hashing/checksum rules:** All artifacts must be SHA256 hashed and listed in `sha256sum.txt`. The bundle is considered valid only if the manifest checksum matches.

## 6) Governance / Safety
- **L1/L2/L3 Breakdown:**
    - **L1/L2 (Automated):** Searching, quoting, trust scoring, reporting, and simulation.
    - **L3 (Approval Required):** Real financial swaps, $AOI treasury moves, external posting of transaction results, or imprinting/modifying third-party artifacts.
- **Stealth Classification:**
    - **OPEN/TEASER:** Concept, UI mockups, roadmap, and high-level Core-Temp values.
    - **STEALTH:** Routing algorithms, risk policy weightings, and aggregator "secret sauce."
    - **TOP SECRET:** $AOI Tokenomics (VC structure), actual revenue/cost data, and treasury keys.

## 7) Evidence
- **Specs:**
    - `repos/aoi-ssot/context/NEXUS_BAZAAR_CORE_TEMP_SPEC_V0_1.md`
    - `repos/aoi-ssot/context/NEXUS_BAZAAR_AGGREGATOR_SPEC_V0_1.md`
    - `repos/aoi-ssot/context/NEXUS_BAZAAR_SDNA_VERIFY_FLOW_SPEC_V0_1.md`
- **Standards:**
    - `repos/aoi-ssot/aoi-core/docs/ARTIFACTS_STANDARD_V0_1.md`
- **Logs:**
    - `_inbox/master_logs_txt/0213_1120_OPUS_Session_Phase_6_Nexus_Bazaar_Core_Temp_설계---446e6132-1b5c-435d-a859-0304db092458.txt`
- **History:**
    - `repos/aoi-ssot/context/aoi_core_history_inbox/aoi_core_history_20260220_095110.docx.txt`

## 8) Evidence Gaps & Legacy Assumptions
- **Squad Cardinality:** Legacy logs (02-13) assumed a fixed "9-agent" squad. Current design is flexible (n-agents), though the "9 Individual Skills" lineup remains the primary demo case.
- **Financial Specifics:** $AOI tokenomics details (treasury positions, DLMM structures) are excluded as they are TOP SECRET and managed outside this phase's scope.
- **Live Settlement:** While fee structures (5% tx fee, 2% royalty) are defined, the live on-chain execution logic is deferred to vNext/L3.

## 9) Changelog
- **V0.1 (2026-02-21):** Initial upgrade from skeleton to substantially complete SSOT.
    - Consolidated Core-Temp scoring from 2026-02-20 specs.
    - Integrated Aggregator/Router specs for multi-platform search.
    - Formalized L1/L2/L3 governance mapping.
    - Defined proof bundle requirements.
