# AI-priority organization census audit: rows 601–650

Audit date: 10 November 2026. Requested status cutoff: 9 November 2026.

## Source alignment

Read the census CSV header and confirmed exactly 50 data rows, CSV data rows 601–650 inclusive (header excluded): first Sardine, last pyannote. Names and category fields were copied directly from those rows. The census file's source URLs are search leads and are not treated as evidence by themselves.

## Findings and limits

The row-level CSV preserves the requested schema and separates closed, periodic, rolling, undated, and unconfirmed states. Official-source checks confirmed OpenAI Codex Ambassadors is closed and excludes student applicants; the separate Codex student credit offer is limited to US/Canada. The Google Student Ambassador official 2026 listing gives an Oct 5 close, so it is closed by the cutoff and duplicated across three Google model aliases. Mistral's official ambassador page is rolling, asks for prior advocacy and a six-month commitment, and publishes non-cash benefits. Akash's student route opens periodically and is framed around US campuses, so India eligibility is unresolved. Aethir's official materials describe global ambassador routes, but they are older and do not establish a current intake.

For remaining organizations, the organization-specific bounded check did not establish a current official student ambassador intake. This is explicitly recorded as a non-hit, never as proof that no program exists. This pass has not verified every official URL for every organization, pay, workload, or duplicate against every central ledger; confidence is low where the direct official route was not established. No central ledgers were changed, and no applications, forms, or messages were submitted.



## Independent metadata alignment correction

Alignment correction on 2026-11-10: source row IDs and names were checked and matched, but the original batch used investigator-assigned priority labels in `tier`. The `tier` values have been replaced with exact source-ledger values for all 50 rows; audit findings are otherwise unchanged.
