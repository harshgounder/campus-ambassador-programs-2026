# AI/ML exact-name organization audit — source rows 1651–1700

Date prepared: 2026-11-10. Status cutoff requested: 2026-11-09. Candidate profile: age 18+, second-year B.Tech ECE, Manipal University Jaipur (India), graduating 2029.

## Scope and method

This is a bounded 50-row screening pass against data-row positions (header excluded) in `/home/liebert511/campus-ambassador-hunt/data/ai-orgs-census.csv`. Exact census names were searched in three ways: (1) organization/product-specific queries paired with campus/student/ambassador terms; (2) role-family queries for champion, advocate, fellow, chapter, representative, and community leadership; and (3) targeted official-domain or exact-platform searches for the strongest leads. Search-result similarity alone was not treated as proof of entity match. Official pages/forms were preferred; third-party snippets were used only to locate official sources or date context. The census labels are GitHub accounts (including some individual-looking handles), so for most labels account identity remains only weakly established.

No X MCP was used. No account was created, form was filled/submitted, or organizer contacted. The Kling AI Google Form appeared in search excerpts only; it was not submitted.

## Findings

- **KlingAIResearch (row 1685):** Exact Kling AI student ambassador application located. The organizer's April 17, 2026 X announcement links the form. The form describes a first student cohort, campus/community event organizing, free product credits/subscriptions and possible event funding; expected graduation 2029+ is an option. The form contains no explicit geography, age, or deadline terms. Search indexing on Nov 10 does not prove it was accepting on Nov 9. It is a strong route lead, but not a confirmed-open Nov 9 opportunity or confirmed India-eligible program. This is an exact duplicate of the Kling AI Student Ambassador record already present in `recheck-source-slice-1001-1534-wave2.csv` row 1029; do not create a second ledger record.
- **RasaHQ (row 1658):** Rasa Heroes is an official adjacent builder/feedback cohort with a community application/interest route and rolling cohorts. Its own page says it is not an ambassador scheme. Country and student eligibility are not stated; it should not be promoted as a campus ambassador opportunity.
- **NVIDIA-NeMo (row 1699):** An NVIDIA-wide student ambassador program is evidenced through affiliated university sources and 2026 activity, with Japan school selection and established members. The sources do not provide a current India-facing public application. Event registration is not an ambassador application. Prior research already recorded this related NVIDIA route, so no new distinct opportunity is proposed.
- **Other 47 labels:** No exact-entity official student/campus/community ambassador, advocate, champion, chapter, fellowship, or representative application was confirmed in the bounded searches. This is not evidence that none exists. Some pages/results were generic homonyms, unrelated projects, ordinary open-source participation, competitions, or professional-only roles; those were not counted as exact student routes.

## Candidate fit and cutoff handling

For Kling AI, the requested 2029 graduation year fits a listed form option, but there is no age or India rule, no assurance that ECE is selected, and no dated Nov 9 application-status evidence. For Rasa Heroes, student status is not a stated requirement and the route is a build/feedback cohort, not ambassador work. For NVIDIA, existing appointed cohorts and region-specific affiliated-campus activity do not show a path for an MUJ student. The other rows have no verified route to assess against the profile.

Nov 10 observations are not silently treated as Nov 9 facts. A live-looking/accessible form without a dated acceptance statement is recorded as an undated lead, not as confirmed open.

## Validation

The accompanying CSV uses the required 13-column schema exactly. Source `name`, `tier`, and `category` were copied verbatim for rows 1651–1700. The final check verifies all 50 unique IDs, exact positional alignment, exact metadata fields, column order, and row widths. This slice supports the larger AI-first search but does not complete the 5,745-row census or the worldwide opportunity universe.
