# AI organizations census audit: rows 51–100

Scope: CSV data rows 51–100 (50 organizations), `outputs/census-search-ledger-2026-11-09.csv`, checked for the 2026-11-09 research cutoff. The audit output is `ai-orgs-audit-curated-051-100-2026-11-10.csv`; central ledgers were not changed.

## Search and source review

- Cross-checked all `outputs/*.csv` records for exact organization-name matches before classifying a candidate; search-result index appearances were separated from confirmed program ledger entries.
- Used 22 grouped Parallel/Exa search calls (66 concise query phrases across this and follow-up pass) covering the 50 names with targeted terms such as “student ambassador program,” “official student ambassador community,” and company-specific community/campus terms. Search results were discovery evidence only.
- Attempted direct fetch of 11 official pages for the strongest possible leads: Suno Growth Ambassador form, SenseTime talent page and scholarship/news page, Replit Campus Leaders, Qodo Super Qodoer, MLflow Ambassadors, Lightning AI Ambassadors, Vector Institute students, OpenHands, and Weaviate community. Official organizer pages were prioritized over third-party listings.
- Treated the audit output as per-name lead triage, not exhaustive proof of absence. An official homepage or contribution guide alone does not establish a student program.

## Positive or adjacent leads in this slice

Suno has a current creator-growth application form requiring applicants to be 18+, create English short-form content, and produce 15–30 videos monthly; it requires country support through PayPal or Bill.com. Its separate Sunoversity page is dated 2024 and closed in 2024, so it is not current. SenseTime has a CUHK Shenzhen notice dated July 30, 2026 for 2027 campus ambassador recruitment; the accessible notice does not establish an India/global intake or remaining application window. Qodo, Replit, Langfuse, Lightning AI, MLflow, Weaviate, AWS, and Vector Institute all have prior ledger leads or adjacent program records; the audit labels role types and geography separately. Elastic has historical official community-ambassador material, but current application status is unresolved. Yandex U-Team and Civitai Champion pages surfaced as leads whose current cross-border intake is unverified. KServe has an open-source contribution route, not a student-specific program.

Adept Scientific was kept distinct from Adept AI; Society of Women Engineers was kept distinct from the SWE-agent repository; Replit was not confused with Replicate. Search noise from generic campus-ambassador vendors and unrelated programs was excluded.

## Limitations

Search indexing and page content can be incomplete or stale. A “NO VERIFIED ROUTE FOUND IN THIS PASS” cell means this pass did not substantiate one, not that no route exists. Most “India eligibility” fields remain unknown where official materials were silent. No forms were submitted, accounts accessed, people contacted, or user data entered.
