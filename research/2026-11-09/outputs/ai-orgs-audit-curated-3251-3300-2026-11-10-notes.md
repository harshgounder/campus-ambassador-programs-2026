# AI organization census audit — source rows 3251–3300

Prepared 2026-11-10. Requested evidence cutoff: 2026-11-09. Candidate profile: adult second-year B.Tech ECE student at Manipal University Jaipur (India), expected graduation 2029.

## Coverage and method

- Audited 50 consecutive source rows from `census-search-ledger-2026-11-09.csv`; copied `name`, `tier`, and `category` verbatim and in order. Companion CSV follows the neighboring 13-column schema.
- Used grouped exact-name public-web queries covering student/campus ambassador, community leader, champion, advocate, fellow, chapter, representative, creator, developer community, and relevant specialty terms. Followed search leads for the Girls-In-AI exact GitHub identity, Catalyst RL, pgmpy, TanStack and MuJoCo-related robotics project. Search results were reviewed for exact-entity fit; broad generic campus-ambassador schemes and unrelated same-name programs were not attributed to these census entities.
- The local Agent Reach CLI was unavailable (`command -v agent-reach` returned no path). Searches used the available public-web search tools. No X MCP or login-gated social tooling was used. No forms, accounts, personal data, or organizational contact were involved.
- Excluded code contribution, GitHub activity, ordinary community membership, contests, jobs/recruiting, research opportunities, sponsorship, and generic directories as evidence of an ambassador or appointed student-leader role.
- Exact-handle names generally resolve to user profiles, project repositories, labs or products; those labels alone do not establish a formal program owner. No exact-name duplicate qualifying student-leader opportunity was identified in reviewed curated outputs. Prior census/search-wave matches are discovery records, not proof of a program.

## Organization-specific findings

- **Girls-In-AI (row 3252):** exact GitHub organization profile describes a Shenzhen-based Chinese women-in-programming learning project, with beginner programming, data analysis, machine learning and deep-learning content. It should not be conflated with unrelated “Girls in AI” organizations or programs returned by generic searches. Its repository/contributor and educational content routes do not document a campus/student ambassador intake. Source: [Girls-In-AI GitHub profile](https://github.com/girls-in-ai).
- **Catalyst team (row 3263; reinforcement learning):** exact Catalyst RL repository describes open-source machine-learning and reinforcement-learning software. The project is a toolkit; ordinary software contributions or use are not a formal student-leader intake. Source: [catalyst-team/catalyst-rl](https://github.com/catalyst-team/catalyst-rl).
- **pgmpy (row 3276; probabilistic graphical models):** official documentation identifies a Python toolkit for probabilistic graphical models. Search surfaced historical GSoC 2014 student participation pages; those are software project/contest participation, not an ambassador appointment and do not establish a current intake. Sources: [pgmpy documentation](https://pgmpy.readthedocs.io/en/latest/), [pgmpy GSoC 2014 page](https://github.com/pgmpy/pgmpy/wiki/GSoC-2014).
- **TanStack (row 3290):** official site identifies an open-source web application library ecosystem and describes maintainers, partners/sponsors, and developer contribution/community routes. These do not constitute a student ambassador or campus leader program. Pages were observed Nov 10, 2026, after the cutoff, and do not prove cutoff availability/status. Sources: [TanStack](https://tanstack.com/), [TanStack repository and contribution information](https://github.com/TanStack/tanstack.com).
- **mujocolab (row 3294; robotics/reinforcement learning):** official `mjlab` repository describes an Isaac Lab-style API powered by MuJoCo-Warp for reinforcement-learning and robotics research. GitHub topic results showed repository activity through Nov 8, 2026, but activity is not evidence of an ambassador intake. Source: [mujocolab/mjlab](https://github.com/mujocolab/mjlab).
- **Other exact project/profile names:** targeted searches included the listed AI/ML-related handles and projects. Results either supported a project/profile identity or returned unrelated third-party ambassador schemes and generic community references. No qualifying exact-entity student/campus ambassador, champion, advocate, fellow, chapter, representative or creator intake was confirmed. For example, an individual profile, software project, GitHub organization membership page or lab roster alone does not establish an intake. Selected identity locators are recorded in the CSV.

## Cutoff, geography, candidate fit, benefits

Searches were made Nov 10 after the requested Nov 9 cutoff. Only dated pre-cutoff material is used for cutoff facts. Undated and post-cutoff pages are treated as current observations, not retroactive proof of whether an intake was open or closed on Nov 9. The historical pgmpy GSoC evidence is from 2014 and concerns project participation; the Nov 8 mjlab repository activity concerns code updates only. Neither establishes an ambassador role.

No India eligibility, age, enrollment, year, major, or graduation criteria could be assessed for a qualifying student-leader route because none was confirmed. No deadlines, compensation, stipend, workload, term, perks, application procedure or selection criteria were proven for a qualifying route. Candidate fit is therefore unassessable across the 50 entities. No country exclusion is inferred from lack of published eligibility.

## Coverage and access limitations

The sweep was bounded and grouped, not 50 exhaustive manual audits across every regional university channel, private community, platform or language. Chinese identity context was checked for Girls-In-AI; broad local-language coverage was not performed across all names. Search indexes can surface unrelated programs with the same generic terms. Agent Reach CLI was absent. No X MCP, forms, account creation, contact or personal-data entry occurred. “No route found” means no qualifying exact-entity intake was confirmed in this bounded search, not proof that none exists.

## Validation

CSV has exactly 13 columns and 50 data rows. IDs are 3251–3300 in ascending order with no gaps; each `name`, `tier`, and `category` exactly matches the corresponding source-ledger row.
