# AI organization census audit — source rows 3401–3450

Prepared 2026-11-10. Requested evidence cutoff: 2026-11-09. Candidate profile: adult second-year B.Tech ECE student at Manipal University Jaipur (India), expected graduation 2029.

## Coverage and method

- Audited 50 consecutive rows from `census-search-ledger-2026-11-09.csv`; copied row number, name, tier and category verbatim and in order into the companion 13-column CSV.
- Used five grouped Exa web searches (up to 10 results each; 50 result slots including overlap) across exact entity names and student/campus ambassador, developer advocate, champion, community, and AI/ML terms. Queries included AI/ML beyond LLMs, software, robotics, reinforcement learning, computer vision, and data infrastructure. One query included Chinese terms for student, campus, developer and community ambassadors. Search output was treated as discovery only, not proof of program ownership or absence.
- Read three organizer/identity pages directly via Exa fetch: MemMachine's Student Ambassador page, its Community Ambassador page and its GitHub organization page. These confirm the one exact-entity route found in this slice.
- Checked nearby curated outputs for exact-entity duplication. A prior audit had mentioned MemMachine as an unrelated namesake result against another census handle; that is not a duplicate record for this exact MemMachine row.
- Excluded generic directories, unrelated programs, jobs/recruiting, research or contests, ordinary open-source contributions, and cross-entity lookalikes. Examples include Replit results returned for the unrelated `luspr` handle, Akash results returned for `aksnzhy`, and DeepStation/2077AI ambassador pages returned for `DeepGraphLearning`. These do not establish a role with those exact census entities.
- The Agent Reach command-line utility was unavailable in this environment; public-web research used the connected Exa search/fetch tools. No X MCP or browser was used. No forms were submitted, accounts created, organizations contacted, or personal information entered.

## Organization-specific finding

- **MemMachine (row 3446):** The official student program says it empowers students “around the world” as campus representatives for MemMachine, described as an open-source memory/context layer for AI agents. It asks ambassadors to host 1–2 events per semester, build API projects, create content and give feedback. To apply/onboard, it directs candidates to join the MemMachine Discord, introduce themselves in `#ambassadors`, describe their role/interests and an outreach idea, and share profile/project links; the team says it will follow up. The page describes a six-month active phase, mentorship, certificate, swag, early access, visibility, and possible referrals/internships for top ambassadors. These benefits and possible referrals are not guaranteed. The separate Community Ambassador page covers developers, researchers, creators and professionals around the world.

  The organizer page was observed on Nov 10, 2026, but has no publication/update date and no explicit application open/closed state or deadline. Therefore the exact Nov 9 cutoff availability cannot be confirmed. “Students around the world” supports an inference that an India-based student may apply, but the page gives no country list or India-specific rule. It states no age floor, year/major restriction or graduation rule; an adult second-year ECE student graduating in 2029 is not expressly assessed by the selection criteria. The program is AI-agent/LLM-adjacent; it is included because the census scope includes AI, while the rest of the slice was searched across broader AI/ML disciplines too.

  Sources: [MemMachine Student Ambassador Program](https://memmachine.ai/community-student-ambassador-program/), [MemMachine Community Ambassador Program](https://memmachine.ai/community-ambassador-program/), [MemMachine GitHub organization](https://github.com/MemMachine).

## Other names and limits

- For the other 49 census labels, no exact-entity official student/campus/developer/community ambassador, champion, advocate, fellow, chapter, representative or creator intake was confirmed in these bounded grouped searches. Many labels are GitHub-style handles/project names; a handle or repository alone does not establish a distinct legal organization or a program owner. Negative findings do not prove that no local, private, unindexed, invitation-only or future intake exists.
- Some listed source URLs point to plausible but different programs or generic aggregators; the row-level CSV distinguishes those from exact-entity evidence. A route for an organization mentioned only in search results is not carried across to another row with a similar handle.
- Search was run on Nov 10 after the requested Nov 9 cutoff. Current page presence, especially undated pages, is not treated as proof of availability at cutoff. No qualifying route for this slice has dated evidence establishing open/closed status on Nov 9.
- Regional language coverage was limited to grouped English/Chinese web-search discovery; this was not a comprehensive Chinese/local-platform pass for every name. Search indexing and language coverage constrain negative conclusions.

## Candidate fit and unresolved information

Only MemMachine produced an exact-entity route. Worldwide student wording suggests possible India fit, but does not give country-specific eligibility; age, academic year, major, graduation timing, selection criteria and actual intake status on Nov 9 remain unconfirmed. It states event expectations but not total weekly hours or compensation. No exact route in this slice was confirmed to be open at cutoff. The CSV carries these uncertainties row by row.

## Validation

The output CSV has the neighboring 13-column schema and exactly 50 data rows. Row IDs are 3401–3450 in ascending order with no gaps. Every `name`, `tier` and `category` value exactly matches the corresponding source-ledger row.
