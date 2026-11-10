# AI organization census audit: rows 951–1000

Audit prepared: 2026-11-10. Requested status cutoff: 2026-11-09.

## Source alignment

Confirmed exactly 50 source data rows (header excluded) from `outputs/census-search-ledger-2026-11-09.csv`. Exact first/middle/last: 951 `xbgoose` (`org`, `classification`); 975 `jonathandinu` (`org`, `image`); 1000 `neroued` (`org`, `multimodal`). Programmatic assertions matched every census row ID, name, tier, and category.

## Bounded findings and limits

The exact-name pass used one Exa search per row, prioritizing official identity/program pages and excluding unrelated aggregators. These searches are discovery checks, not exhaustive crawl or proof of nonexistence. For 48/50 rows no named-entity official student/campus leadership route was confirmed. A bounded non-hit is not evidence that no route exists.

One parent-organization route surfaced: Mistral Experimental is described on its official Hugging Face profile as under Mistral AI, and Mistral AI’s official docs currently describe rolling AI Ambassador applications, requiring AI/ML expertise, prior advocacy, active community participation, and six-month commitment. The route lists API credits, early feature access, recognition, and event access, with community support, educational content, feedback, and events as responsibilities. No cash stipend, student requirement, India rule, or time-hours estimate was stated on the fetched page. Because the page is undated and no Nov 9 archive was checked, its rolling status is marked open-appearing, not timestamp-verified. The connection is to the parent Mistral AI program, not a separately confirmed subteam cohort.

Hugging Face’s official Student Ambassador call is a historical 2022 program (deadline June 13, cohort ended Dec 31, 2022), not a current opportunity. It is relevant only as historical context for HuggingFaceM4. LeRobot’s separate Seeed Physical AI workshop partnership page is not treated as a LeRobot ambassador program.

For applicants without an exact-entity route, CSV rows carry the same clearly unaffiliated cross-organization leads: OpenAI Student Collective; Claude Campus; local Google Developer Groups on Campus; Microsoft Copilot Student Ambassador; Red Hat Academy Student Ambassador; HackerRank Campus Crew. Broad-AI relevance, age/student/campus criteria, country restrictions, deadlines, time, cash and noncash benefits are qualified per the official pages and earlier same-series source review. Notable limitations: OpenAI India Fall 2026 intake was closed; Microsoft requires an affiliated four-year university and MUJ affiliation was not confirmed; Red Hat requires Academy participation/instructor nomination; HackerRank is coding/community rather than AI-specific and unpaid; local Google availability varies; Claude’s prior-audit Sep 12, 2026 deadline was past at cutoff.

## Sources checked

Exact-name identity/program discovery searches were run via Exa for all 50 names. Official pages fetched for Mistral Ambassador program; Hugging Face 2022 Student Ambassador call; OpenAI Student Collective; Claude Campus; Google Developer Groups; Microsoft Copilot Student Ambassador; Red Hat Academy Student Ambassador; HackerRank Campus Crew. See per-row URLs in the CSV. Census search-result URLs were not treated as official proof merely because they were present in the source.

## Applicant profile and boundaries

Fit is assessed against the user-supplied profile: age 18+, second-year BTech ECE at Manipal University Jaipur. Those facts are not established by census rows. The audit checked applicant profile fit, India/MUJ/geography only where evidence was available, deadline/workload and cash versus benefits; unknowns remain explicit. No forms were submitted and nobody was contacted. Central ledgers were not modified.
