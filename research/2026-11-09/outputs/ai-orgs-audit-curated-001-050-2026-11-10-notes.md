# Curated AI organization audit — rows 1–50

**Cutoff:** 2026-11-09. **Audit file:** `ai-orgs-audit-curated-001-050-2026-11-10.csv`.

## Scope and result

Audited census data rows 1–50 (header excluded), one record per input name. The sweep issued 50 name-specific search queries for official student/campus, ambassador, developer community, chapter, student volunteer, and adjacent technical routes, then made five focused follow-up queries for BAAI, NVIDIA, IBM SkillsBuild, Hugging Face, and Black Forest Labs. The search service returned a rate-limit error on a separate parallel Exa retry; results from that retry were not treated as evidence. All positives below rely on organizer/official pages or are explicitly labeled adjacent/uncertain.

Official pages support several routes, with important differences: Qwen developer/event ambassador (global wording; country eligibility unstated); OpenAI Student Collective (India cohort closed for Fall 2026, future interest remains); EleutherAI contributor community (informal/undated); Qdrant Stars (contributor-led, intake link but no published status/eligibility); Mistral AI Ambassadors (rolling, six-month commitment, no country or student rules); OpenBMB MiniCPM Ambassadors (ongoing recruitment stated; country eligibility unstated); Haystack Ambassadors (quarterly review, geography explicitly not a barrier, six months of contribution required); and AI4Bharat’s remote student internship (adjacent, undated apply path). Hugging Face’s student ambassador page is a 2022 closed call. Upstage’s 2nd ambassador cohort is historical/closed or uncertain, with no current intake verified. NVIDIA’s DLI University Ambassador route is educator-only under published qualifications, so it is an adjacent screen-out for this student. IBM SkillsBuild appeared only via secondary/university career-center material; it is retained as an unverified lead, not a confirmed route.

The census tranche does not imply all these routes are currently actionable. “Global” wording is kept separate from explicit India eligibility. Unmatched names use `NO VERIFIED ROUTE FOUND IN THIS PASS`; this means no route was verified during this bounded search, not that no route exists.

## Dedupe

Checked `ai-ml-priority-verification-delta-2026-11-09.csv`, the first-wave ambassador ledger and focused AI outputs, including AI education, AI labs/models, open-source, developer ecosystem, and the OpenAI/ambassador correction files. Confirmed duplicates: OpenAI Student Collective, Qwen Ambassador, Mistral Ambassador, OpenBMB MiniCPM Ambassador, Haystack Ambassador, Qdrant Stars, and NVIDIA DLI University Ambassador. Their prior records are cited in each row. Qwen is specifically flagged for a source-renderer conflict: a prior local recheck found its page unreadable, while the current fetch exposed program content; do not silently treat eligibility or intake as fully reconciled. The separate Upstage and IBM leads are marked as prior discovery/unverified mentions where applicable, not validated duplicates.

## Sources and counts

- **50** individualized organization-name searches in one batched search request.
- **5** additional focused name-specific queries.
- **12** first-party pages directly fetched for route verification: Qwen, OpenAI Student Collective, Codex Ambassadors, Qdrant Stars, Mistral Ambassadors, Haystack Ambassadors, OpenBMB MiniCPM, AI4Bharat home/positions, AI4Bharat IndicNLP project page, Upstage Ambassador cohort, Hugging Face’s historical student-ambassador call, and EleutherAI Get Involved.
- Additional official search excerpts reviewed for NVIDIA DLI University Ambassadors and current NVIDIA student programs; the IBM SkillsBuild item came from a university career-center flyer and is not organizer proof.
- Existing output files were searched with targeted terms and `rg`; no central ledger was edited.

## Limits

This is a name-by-name tranche audit, not an exhaustive search of every language, local forum, social platform, repository issue board, or national student chapter. Many of the 50 names are model families or repositories rather than independent organizations, so a product-level ambassador program may not exist under the model’s own name. Search snippets and surfaced links were discovery leads only. No forms were opened or submitted, and no person or organization was contacted. No X MCP was used.
