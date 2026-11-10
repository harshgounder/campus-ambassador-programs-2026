# AI/ML exact-name audit — source rows 1151–1200

Date prepared: 2026-11-10. Status cutoff: 2026-11-09. Candidate profile supplied for relevance: 18+, second-year B.Tech ECE, Manipal University Jaipur, India, graduating 2029.

## Method

Ran one bounded exact-name Exa web search for each of the 50 source labels (50 queries total), targeting official student/campus ambassador, developer/community advocate, representative, and student-leader routes. A high-concurrency attempt initially returned provider HTTP 429 rate-limit errors for many requests. Searches were retried as spaced batches of five. Therefore, the retry results provide one query per row, but the initial failures are not negative evidence. A supplementary Parallel web search accepted only the first five of 50 submitted queries and was not treated as complete coverage.

Reviewed surfaced exact-name results for official-source routes and obvious adjacent results. No exact-entity official student route was confirmed in the bounded results. Some results concern research recruitment, research participation, competitions, ordinary project contribution, workshops, or professional/community leadership; these are recorded as adjacent leads where appropriate and are not represented as ambassador programs. Generic search noise (including a result for HackerRank Campus Crew attached to the ambiguous word “clips”) is not an exact-entity match. No X MCP used.

## Findings and interpretation

Every row is a bounded no-confirmation result, confidence low. Low confidence reflects the lack of a verified route and, for many labels, entity ambiguity; it does not establish that a route does not exist. No route-specific primary-source evidence supported claims about India/foreign-student eligibility, age, degree/year, time/tasks, compensation/perks, application process, or whether a call was open on the cutoff date. For candidate relevance, the user profile was considered, but no eligibility inference was made without published program terms. Pages with undated live content do not by themselves prove the program was active on Nov 9, 2026.

No forms were opened for submission, no applications/accounts/outreach were made, and no contact was sent.

## Row validation

Source rows are 1-based data-row positions excluding the header. Source fields `name`, `tier`, and `category` were copied verbatim. Output schema is 13 columns: `census_row`, `name`, `tier`, `category`, `identity_check`, `official_student_route_status`, `programs_or_leads`, `cutoff_status`, `india_eligibility`, `official_urls`, `existing_ledger_duplicate`, `confidence`, `unresolved_gaps`. The independent validation checks source alignment, uniqueness, count, schema, and row widths.
