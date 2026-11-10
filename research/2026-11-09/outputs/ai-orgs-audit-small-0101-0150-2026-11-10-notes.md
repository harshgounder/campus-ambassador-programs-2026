# AI small-tier exact-name audit, ranks 101–150

**Cutoff requested:** 2026-11-09. **Research date:** 2026-11-10.

## Scope and row integrity

This audit preserves the exact `census_row`, `small_rank`, `name`, `tier`, and `category` values from the source queue for all 50 ranks 101–150. The output has 50 data rows and 14 columns. These are small-tier HF-associated entries; several are personal accounts, labs, or research publishers rather than independent program organizers. Identity uncertainty was kept explicit.

## Findings

No organizer-owned, currently open student ambassador, campus advocate, champion, creator, or community-lead application was verified in this slice. This is a bounded indexed-search result, not evidence that no such opportunity exists. `ncbi` is a name collision: the surfaced Campus Affiliates page belongs to the National Coalition Building Institute, not an AI organization. The Vamsi search returned a third-party Google Gemini Student Ambassador page but no evidence tying this account to that program; it was excluded. TheBloke's model material references a general Discord community; `org2ai` has a closed GitHub issue inviting Discord/WeChat participation. These are separated as non-ambassador leads, not counted as current student opportunities. Flax sentence embeddings mentions a community event; Westlake Representation Learning Lab advertises research/recruitment opportunities; neither establishes an ambassador route. China/local entities SCUT-DLVCLab, Westlake-repl, and IndexTeam were included within this row range and screened, but no student/ambassador intake was verified.

For every row, Nov 9 cutoff state is `unknown` unless an explicit dated, closed artifact is noted. An undated profile/page read on Nov 10 does not establish status on Nov 9. India eligibility remains unconfirmed in all cases; no eligibility was inferred from global availability, account location, or broad community access.

## Method, duplicates, and limits

Used exact census handles/names with student ambassador, campus, community-lead and program terms, then checked identity against indexed entity/profile pages when results surfaced. Official or organizer-owned URLs are recorded in the row. Exact-name duplicate screening was run against local CSV outputs in `outputs/`; `IndexTeam` and `superb` matched prior census/search artifacts, recorded as mentions/candidates rather than evidence of open programs. This scan can miss aliases, translations, private communities, and routes in local-language channels. Search-provider rate limiting interrupted a portion of the parallel search batch; those entries remain low-confidence bounded negatives and are marked with gaps. No forms were submitted and no organizers contacted.

The 14-column CSV is the row-level record; it includes cited URLs and keeps separate-route leads, cutoff status, India eligibility, duplicate screen, confidence, and gaps distinct. No claim of exhaustive absence is made.
