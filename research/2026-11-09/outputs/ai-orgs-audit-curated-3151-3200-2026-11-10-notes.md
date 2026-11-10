# AI organization census audit — source rows 3151–3200

Prepared 2026-11-10. Requested evidence cutoff: 2026-11-09. Candidate profile: adult second-year B.Tech ECE student at Manipal University Jaipur (India), expected graduation 2029.

## Coverage and method

- Audited 50 consecutive data rows from `census-search-ledger-2026-11-09.csv`; copied `name`, `tier`, and `category` verbatim and in order. The companion CSV uses the neighboring 13-column schema.
- Reviewed the four machine search-result URLs per source row as discovery leads, screening for exact-entity student ambassador, campus ambassador, champion, advocate, fellow, chapter, community representative, and creator routes. Follow-up web searches targeted `sdv-dev`, Eclipse SDV acronym collision, `ml-tooling`/marimo, `ai-winter`, `girafe-ai`, and adjacent exact names including Ploomber, Deta and Chaskiq. Official/project sources were preferred when available.
- Checked the required Agent Reach route: `/usr/bin/bash: agent-reach: command not found`; the health-check could not run. The available public web-search tool was used for bounded follow-up queries. No X MCP was used. Social-platform search backends, private communities, exhaustive per-handle searches and systematic Chinese/local-language coverage were not available in this pass.
- Search errors: Agent Reach missing; no other tool-level errors observed. Results are bounded, not exhaustive.
- Excluded generic campus-ambassador directories and unrelated-provider programs (including Claude, Zed, GUVI, Trinka, SwytchCode, 2077AI, DevIn and others), generic jobs, education courses, standard open-source contribution routes, and generic community pages as evidence of an exact entity-owned student leader intake.

## Findings and status distinctions

- **Potentially material acronym collision:** exact census `sdv-dev` is the Synthetic Data Vault GitHub project family, an ML/synthetic-data tool. Search results surfaced Eclipse SDV’s official Global Advocates page, but Eclipse SDV is a distinct software-defined-vehicle initiative. Its volunteer ambassador program requires established participation in its own working group and says three ambassadors have been selected; this was excluded from the `sdv-dev` row. No `sdv-dev` student/ambassador route was confirmed. Official/project sources: https://github.com/sdv-dev ; https://github.com/sdv-dev/SDV ; unrelated lookalike: https://eclipsesdv.org/ambassador-program/ .
- `ml-tooling` census results included marimo’s official ambassador page. That is a cross-entity hit: marimo has Campus, Professional and Alumni tracks, but no relationship proving it is the census entity `ml-tooling` was found. The ml-tooling/ml-workspace contributor guidance is ordinary open-source contribution, not a student representative intake. Sources: https://github.com/ml-tooling/ml-workspace ; https://marimo.io/ambassadors .
- `ai-winter` points to a China-based robotics motion-planning/navigation and deep reinforcement learning developer/project, not the unrelated AI Winter School. No student ambassador call was found. Source locator: https://github.com/ai-winter/ .
- `girafe-ai` search results included an MSAI course/cohort; the source describes education/capstone, not an ambassador application. This is an adjacent education lead and was excluded as a role.
- No dated exact-entity open, rolling, closed, restricted or future student ambassador intake was established for this slice by the requested Nov 9 cutoff. No confirmed current open or closed roles were found. Where current/undated pages were observed Nov 10, they were not backdated. A no-hit means no evidence located in this bounded public search, not proof of absence.
- Most remaining census names appear to be user handles, individual developers, repositories or small project names. Identity uncertainty is preserved per row; exact-name search hits to unrelated organizations do not prove ownership. No qualifying exact-name duplicate of a verified student/community-leader role was identified in the checked AI ledger context; generic cross-entity hits were excluded.

## Cutoff, access, and coverage limitations

- The requested cutoff is Nov 9, but this pass was prepared Nov 10. Only evidence explicitly dated before cutoff was treated as cutoff evidence. Current crawls or undated page states are labeled observations or unresolved, never backdated.
- The ledger's four returned URLs often point to unrelated programs. They provide candidate leads only. This audit did not individually open/search all 50 handles across all social networks, country sites, university channels or private communities, and non-English coverage is incomplete. It therefore does not establish that no program exists.
- No forms were opened/submitted; no account or personal data was entered; no organizations were contacted. Compensation, time commitment, deadline and student eligibility are left unknown unless proved by an exact-entity source.

## Validation

- Output CSV: exactly 13 columns and 50 data rows.
- `census_row` values are exactly 3151–3200 in ascending order, without gaps or duplicates.
- Each row's `name`, `tier`, and `category` exactly matches the corresponding source ledger data row.

- **Non-LLM AI/ML and Chinese-channel follow-up:** `datamllab` is Rice University’s Data Analytics Lab; its GitHub organization includes reinforcement-learning projects such as HarborRL and RLCard. This is a research lab/repository presence, not a student ambassador call. `YunYang1994` public Chinese-language search results point to a Guangzhou developer whose projects include computer vision/Yolo and reinforcement learning; no representative intake surfaced. Robotics research/education is present around Peter Corke and the *Introduction to Autonomous Robots* textbook, but neither produced a matching person/project-owned ambassador role. QUT's historical robotics school outreach used QUT student ambassadors; it is an institutional program and not an exact-entity current intake. Sources: https://github.com/datamllab ; https://github.com/YunYang1994 ; https://www.qut.edu.au/about/our-people/academic-profiles/peter-corke ; https://www.qut.edu.au/news?id=106741 ; https://introduction-to-autonomous-robots.github.io/ .
