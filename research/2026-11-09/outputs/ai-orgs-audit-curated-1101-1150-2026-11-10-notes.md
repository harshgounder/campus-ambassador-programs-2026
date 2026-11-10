# AI/ML exact-name audit — source rows 1101–1150

Date prepared: 2026-11-10. Status cutoff: 2026-11-09. Candidate profile supplied for relevance: 18+, second-year B.Tech ECE, Manipal University Jaipur, India, graduating 2029.

## Method

Ran 50 separate Exa web searches, one for each exact census name, targeted at official student/campus ambassador, developer/community advocate, representative, and student-leader pathways. Search phrase: exact name plus official student/campus ambassador, developer advocate, and community representative. Prioritized official organization sources and treated search results, catalogs, jobs, internships, research, discounts, and ordinary open-source participation as non-equivalent to an ambassador role. Where an official route was surfaced, the CSV gives its direct URL and only the claims supported by the retrieved official page evidence.

## Limits and interpretation

This is a bounded exact-name screening pass, not exhaustive proof of nonexistence. Search engines may miss unindexed, private, local, renamed, or social-only calls; low-confidence no-hit rows must be read as “not confirmed in this pass.” Official source pages can change after the cutoff; undated live pages do not prove an intake was open on Nov 9. Identity can be ambiguous for individual handles, project names, archives, and similarly named entities. Geography, India eligibility, age, enrollment/year, hours, cash/noncash benefits, and application route are left unresolved unless supported by primary evidence. Roles are kept distinct from employment, internships, research, discounts, and ordinary OSS contributions. No forms were opened for submission, no accounts were created, and no outreach was sent. X MCP was not used.

## Row validation

Source rows were selected by 1-based data-row position with the header excluded. CSV source fields `name`, `tier`, and `category` were copied verbatim. Expected output schema: 13 columns: `census_row`, `name`, `tier`, `category`, `identity_check`, `official_student_route_status`, `programs_or_leads`, `cutoff_status`, `india_eligibility`, `official_urls`, `existing_ledger_duplicate`, `confidence`, `unresolved_gaps`. Independent validation below checks source alignment, uniqueness, row count, schema, and row widths.
