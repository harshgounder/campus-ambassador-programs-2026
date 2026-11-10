# AI/ML exact-name audit — source rows 1201–1250

Date prepared: 2026-11-10. Status cutoff: 2026-11-09. Candidate profile supplied for relevance: 18+, second-year B.Tech ECE at Manipal University Jaipur, India, graduating 2029.

## Method and search coverage

Ran exactly one Parallel web-search query per exact census label, 50 queries total. All 50 calls completed without tool errors and returned 10 results apiece (500 returned result records). The result sets were inspected for exact-entity official student/campus ambassador, developer/community advocate, representative, or student-leader routes. The search engine returned substantial cross-query noise: unrelated school ambassador pages and unrelated AI companies' programs recurred against multiple names. Those were excluded as false matches. Search success means a result set was returned; it does not mean the web was exhaustively searched or that every result was relevant.

The only exact-entity official route confirmed was Arize Phoenix's general Phoenix Ambassador Program (census row 1243, `arize-ai`). Its two official pages were fetched to review the route and terms. The official join page says students, professionals, and independent builders may apply, and describes meetup/workshop organizing, event materials, and an event stipend of up to US$500 for a locally hosted meetup. The main program page was live-fetched on 2026-11-08 and showed an Apply link. This supports a live-appearing application route by cutoff, but no deadline, seat limit, explicit rolling policy, hours, or term was stated. It is a general community ambassador role rather than a student-only campus role. India is represented by a listed Bengaluru ambassador, which does not establish applicant eligibility from India. No form was opened or submitted.

For `mozilla-ai`, results included legacy Mozilla Firefox Student Ambassador wiki pages. The official legacy page says new Firefox Student Ambassadors would no longer be accepted as Campus Clubs replaced that program. This is historical Mozilla-wide material, not a current Mozilla AI route, and was excluded from positive matches.

Jobs, internships, research recruitment, research participation, discounts, ordinary OSS contribution, competitions, workshops, and events were excluded as ambassador routes unless the exact organization published an actual representative/advocate role. A no-hit is bounded non-confirmation and must not be read as proof no program exists.

## Findings and fit

There is one confirmed route among these 50 exact labels: Arize Phoenix Ambassador Program. The official page states general eligibility for students but does not give age, degree/year, or a country-specific rule. An 18+ second-year MUJ ECE student could be a plausible applicant if building with Phoenix and able to organize local community events, but India eligibility, hours, term, selection criteria, and availability/capacity by the Nov 9 cutoff remain unverified. The event stipend is conditional and limited to up to US$500 for a local meetup; it is not a recurring personal stipend. Non-cash benefits listed include swag/event kits, promotion, and early access to product/research updates.

The remaining 49 rows are bounded no-confirmation results, confidence low. For each, the CSV links a primary project/profile page where an identity source was available; such a profile does not establish that a student route exists. No route-specific primary evidence established age, education/year, India/foreign-student eligibility, tasks/hours/term, compensation, application route, or cutoff intake status.

## Duplicate checks

Checked the central AI priority ledger (`ai-ml-priority-verification-delta-2026-11-09.csv`), the first-wave ambassador research ledger, and all earlier curated AI census audit slices present in outputs. No row in the central AI priority ledger matched this slice's labels or an Arize Phoenix program. The Arize Phoenix route is already present in `ambassador-research-first-wave-2026-11-09.csv` as “Phoenix Ambassador by Arize”; earlier curated census rows 401 (Arize) and 402 (Phoenix) also cross-link the same route. This slice records the duplicate and does not modify the central ledger. No exact-label duplicates were found in earlier curated AI census slices for the other 49 labels.

## Row validation

The output CSV contains the exact 13-column schema used by the prior slice: `census_row`, `name`, `tier`, `category`, `identity_check`, `official_student_route_status`, `programs_or_leads`, `cutoff_status`, `india_eligibility`, `official_urls`, `existing_ledger_duplicate`, `confidence`, `unresolved_gaps`. Source positions are 1-based data rows with the header excluded. Validation checks all 50 positions against the source census, verbatim `name`/`tier`/`category`, row uniqueness, schema, and row width. Only the two requested additive slice files were created.

No forms, accounts, outreach, or X MCP were used.
