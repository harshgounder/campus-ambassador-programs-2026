# AI organization census audit: rows 2801–2850

Audit prepared 2026-11-10. Requested opportunity-status cutoff: 2026-11-09.

## Source alignment

The CSV contains the 50 source rows in source order and carries the 13-column audit schema used by neighboring curated slices. `census_row`, `name`, `tier`, and `category` were copied directly from `outputs/census-search-ledger-2026-11-09.csv`; the source ledger was not edited. Output: `ai-orgs-audit-curated-2801-2850-2026-11-10.csv`.

## Findings

- **Niantic / Wayfarer:** Official Wayfarer Community pages list the Wayfarer Ambassador Program 2026 and a Cohort 5 announcement dated 2026-05-01. This is an official, current/recent community ambassador route at the cutoff, but it is specific to Wayfarer community participation and is not an AI/ML or campus-student program. The evidence does not establish that applications were open on 2026-11-09, or the compensation, geographic eligibility, or current accepting status.
- **Kubernetes SIGs:** Official Kubernetes Contributors pages describe open SIGs, working groups, meetings, and leadership; this is a genuine open-source community participation route. It is not a student ambassador intake operated by the `kubernetes-sigs` handle. Some subprojects touch AI/ML infrastructure, but that does not create a campus ambassador route.
- **basicmachines-co / MemMachine:** The official-looking MemMachine Student Ambassador page describes a six-month student community program, campus events, mentorship, swag, early access and possible referrals. The linkage between the census handle `basicmachines-co` and MemMachine/MemVerge was not authenticated in this pass. Treat it as an **uncertain lead**, not a confirmed named-entity program. No dated intake, India eligibility or cash compensation was verified.
- **Other rows:** No other exact named-entity formal student/ambassador intake was confirmed in this bounded pass. A few project contribution surfaces (for example Ceres Solver and OpenUTAU) are adjacent open-source participation, not ambassador programs. The source search results contain many unrelated generic campus-program pages; those were excluded as evidence.

## Search scope and limits

I reviewed the unreviewed URLs already present in the census source rows, searched exact names in multiple grouped web-search calls, and prioritized official project, GitHub, and organization pages when identifiable. The search provider warned that it accepts at most five queries per call; an initial ten-query request silently used only its first five. Follow-up calls covered the remaining groups, but this means discovery was bounded and uneven, not exhaustive. Exact-name searches for short handles often returned unrelated campus programs. Chinese/local-channel coverage was limited: no WeChat, Douyin, or Bilibili community/account access was used, and no account was created. No X MCP was used.

Nov 10 search observations are recorded separately from evidence dated by Nov 9. A live page observed Nov 10, without a pre-cutoff date or archived capture, is not proof that applications were open by the cutoff. No-hit means no matching route was confirmed in the scoped search, never that a program cannot exist.

## Eligibility and activity

For the named entity, country/school eligibility, deadlines, workload, compensation, and current application state were left unconfirmed unless an official source explicitly established them. The discovered Wayfarer community role has no confirmed student requirement. The MemMachine student-program lead needs identity and current-intake verification. No organization-specific MUJ/India fit should be inferred from general global language.

No forms were submitted, accounts created, personal details entered, or organizations contacted. No source files were changed.
