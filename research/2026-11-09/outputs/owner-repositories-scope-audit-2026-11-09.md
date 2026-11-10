# Owner's map repositories: research-scope audit — 9 November 2026

Purpose: use the user's own maps to define the eventual breadth of program discovery. These repositories are scope guides, not ambassador-program directories; a mapped field or technology does not establish that any organization has an open role.

## Repositories reviewed

### `harshgounder/ai-map` (private, default branch `main`, last updated 2026-10-03)

Reviewed `README.md`, `PLAN.md`, `REVIEW-layer1-2026-10-02.md`, the authority registry, and the five harvested source files for ACM CCS, MSC2020, ANZSRC 2020, arXiv and OpenAlex.

The scope is intentionally **AI layer 1 only**. The PLAN calls for one-authority-at-a-time harvesting, then a revision-gap wave, then a source-by-source matrix; the owner had not yet chosen the final inclusion rule for the map. Five of 35 authority entries were harvested in the registry snapshot; other entries are only landed/found or marked gaps. The map records that sources disagree on boundaries: for example, ACM places ML beside AI, arXiv has sibling categories for ML/CV/robotics/NLP, while the owner explicitly chose to include ML and the AI-using parts of CV and adjacent fields. The review identifies dropped or conflated areas including pattern recognition, fuzzy/soft computing, document AI/OCR, active inference, distillation/adaptation, neuro-symbolic AI, robotics/embodied AI, signal processing, and the two directions of quantum-for-AI versus AI-for-quantum.

Use this as a taxonomy warning: the AI phase needs separate lanes for methods, capabilities, systems, engineering, trust/society and application domains, and it must include technical societies and niche communities rather than only AI product companies.

### `harshgounder/cs-universe` (private, default branch `main`, last updated 2026-08-15)

Reviewed `README.md`, the full `ROADMAP.md`, `CHECKPOINT.md`, `HACKATHON-TRACK.md`, the full section/file tree, and the CS Ontology list header and size. The roadmap has 20 top-level layers (00 math/history through hardware, architecture, assembly, OS, compilers, languages, algorithms, networks, databases, distributed systems, concurrency, software engineering, web, virtualization, storage, security, frontier, end-to-end, and applied computing), plus appendices and external cross-checks. The README describes the stack from silicon through operating systems, languages, distributed systems, software and web, with frontier topics such as AI infrastructure/inference, eBPF, quantum and formal methods. The appendix contains 14,736 CS Ontology 3.5 topics, used as a completeness cross-check.

The 2026-08-14 checkpoint reports 177 roadmap entries: 88 written and 89 not yet written. That is a content-writing checklist, not a count of the field or opportunities. The `HACKATHON-TRACK.md` priority override was specific to an August event and must not be treated as the present search priority. Current file dates are August 2026, so later technologies and open-program status need live verification.

For the future non-AI tech phase, use the full layer structure as a field checklist. In particular, retain hardware/semiconductors/embedded/FPGA; architecture and accelerators; operating systems and compilers; programming languages and algorithms; networking/telecom; databases and distributed systems; cloud and virtualization; security; web and developer tools; storage; formal methods/quantum; and the applied-computing topics. A few high-visibility developer tools or cloud platforms would not represent this map.

### `harshgounder/startup-universe` (private, default branch `main`, last updated 2026-08-21)

Reviewed `README.md`, `ROADMAP.md`, `CHECKPOINT.md`, and the pre-seed pack index. The business map runs from founder and problem discovery through markets, customers, validation, product, business model, money/legal, team, marketing, sales, metrics, research, ecosystem, series A+, and end-to-end journeys. Its `14-ecosystem` layer explicitly includes incubators/accelerators, investors, startup communities and India-specific rails. The pre-seed pack has a separate technical diligence, product, data-room, fundraising and GTM index.

The August checkpoint described the main book as a skeleton, while the pre-seed pack contains a substantial independent checklist. Treat startup programs (incubators, accelerators, venture fellowships, founder communities and student-founder networks) as a separate eventual cross-sector lane; do not mix them into AI ambassadors unless the role itself is AI-specific.

### `harshgounder/opportunity-max` (private; taxonomy v3.1 dated 2026-08-12)

Reviewed the repository README, `OPPORTUNITY-TAXONOMY.md`, and the `master-intakes.csv` metadata and candidate records. The taxonomy defines **292 leaf opportunity types across 13 families (A–M)**, organized around the mechanism, sponsor intake, and discovery platform. It separates structured programs, research/academic routes, communities, startup paths, outcomes, government overlays, content, relationship-based opportunities, and platforms. This is a useful role-mechanism framework alongside the field taxonomies; it helps prevent a search from equating every use of “ambassador” or “fellow” with the same opportunity.

The intake snapshot lists **13,592 records** and is dated August 2026. It is a historical discovery pool, not a live-status source. A keyword cross-check surfaced 126 ambassador/chapter-like rows (112 unique program-provider pairs) and 433 AI-keyword rows (422 unique pairs) not exact-matched to the current outputs at the time of comparison. These are **lexical candidate pools, not verified gaps**: many are stale, closed, unrelated, courses, competitions or false positives. Candidate names must be identity-checked, deduplicated by mechanism and organizer, and reverified from current organizer pages before integration.

## Current AI taxonomy mismatch to preserve

`/home/liebert511/campus-ambassador-hunt/scope/SCOPE-AI.md` now has the original 24 AI product/ecosystem categories plus 10 later-added closed-source/application/research/compute/funding categories. `REPORT-AI-SCOPE.md` still describes the earlier 24-category, 486-organization snapshot, while the data inventory has since expanded. Do not use the old report's category or organization count as the current full denominator without a separate current recount. The broader 24+10 category list still does not replace the technical research-field map above.

## Search design implications

1. Keep a field × region/language × role-type matrix so program discovery does not collapse to company ambassador pages.
2. For every field, search both formal ambassadors and adjacent roles (student chapters, developer champions, student representatives, community volunteers, hackathon organizers, fellowships and research pathways), recording the role type separately.
3. Keep status, eligibility, geography, deadline, workload, and cash/non-cash evidence independent; `Apply` buttons and search snippets do not establish acceptance from India or a current cohort.
4. The AI search remains in progress. The non-AI CS and startup-universe program lanes start only after the AI field gaps have had dedicated discovery passes; reading these repositories is preparatory scope work, not evidence that the AI phase is finished.
5. Use `opportunity-max` to test role-mechanism coverage and generate bounded leads; do not treat its August 2026 intake snapshot as current, and do not inflate the project ledger with its lexical candidate counts.
