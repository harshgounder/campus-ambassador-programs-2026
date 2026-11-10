# AI organizations census audit: rows 451–500

## Scope and alignment

Audited exactly census data rows 451–500, excluding the header, from `outputs/census-search-ledger-2026-11-09.csv`. The source has 5,745 data rows; row 451 is Crusoe Cloud and row 500 is Arya.ai. All 50 records retain the source `name`, `tier`, and `category`. The adjacent existing curated audit files use the requested 13-column schema. No central ledger was changed.

## Method

- Rechecked official organization and program pages where available; used web searches as discovery, not as proof by themselves. Search batches covered GPU/cloud communities, AI safety/research organizations, university AI institutes, and India AI companies.
- Favored organizer-owned pages and official application/eligibility descriptions. False-positive campus ambassador search results and third-party listings were excluded unless independently confirmed by the organizer.
- For each organization, recorded identity confidence, student vs. non-student route, published cutoff status as of 2026-11-09, India/global eligibility, deadline, and cash/noncash evidence where available. “No verified route” means only that none was confirmed in this bounded pass.
- Cross-checked existing output CSVs for previously surfaced organization/program mentions. A mention in the baseline census/search ledger is not treated as proof of an actionable duplicate. Known exact overlaps are called out for DigitalOcean Navigators, Nebius Fellows, Runpod Creator, Anthropic Claude Campus, and OpenAI Student Collective.

## High-value verified routes and scope limits

- Nebius Fellows is an official, curated AI builder/community leader program; its separate research grants page is postgraduate-only. Neither page states a student-specific route or India eligibility.
- Vultr Community currently offers open online participation with an earned Ambassador level; it is a points/contributions ladder, not a student selection program or cash stipend.
- DigitalOcean Navigators has an official application path and global framing, but no dated open/closed notice or published country list; experience expectations are substantial.
- Runpod Creator is an open, non-student-specific AI content community with in-kind credits/merch; later ambassador/campus tracks are described as possible future expansion.
- Stanford HAI and Mila have official student roles, but the reviewed requirements make them institution-bound and not applicable to a Manipal University Jaipur student.
- Anthropic’s 2026–27 Claude campus application window (Sep 1–12, 2026) was closed at the Nov 9 cutoff; its official page states a USD 3,600 stipend and worldwide applicants subject to work authorization in their study country.
- OpenAI’s Student Collective explicitly includes India and cash semester stipends, but India Fall 2026 applications were closed at cutoff; only future-interest registration remained.
- NIST NICE is an adjacent cybersecurity volunteer network, not an AI-specific student ambassador program. It is not treated as a fit-positive lead.

## Research tools and evidence URLs

Official program pages cited directly in the CSV include DigitalOcean Navigators (`https://www.digitalocean.com/community/pages/digitalocean-navigators`), Vultr Community and guidelines (`https://community.vultr.com/`, `https://community.vultr.com/guidelines`), Nebius Fellows (`https://nebius.com/fellows`), Runpod Creator (`https://www.runpod.io/creator-program`), Stanford HAI student groups (`https://hai.stanford.edu/research/student-affinity-groups`), Mila lab representatives (`https://mila.quebec/en/prospective-students/student-life-and-resources/lab-representatives`), Anthropic Claude Campus (`https://claude.com/programs/campus`), OpenAI Student Collective (`https://openai.com/student-collective/`), and NIST NICE (`https://www.nist.gov/nice/ambassador-finder`).

## Gaps

This was a bounded review of 50 rows, not an exhaustive audit of every organization’s social channels, regional hiring, invitation-only cohorts, or private communities. Some names are ambiguous or may have changed status (ARC, MIRI, Conjecture, Mad Street Den, Intello Labs); those receive lower confidence and explicit identity gaps. No forms were submitted and no messages were sent. Recheck pages before acting because several pages are undated and opportunity status can change.
