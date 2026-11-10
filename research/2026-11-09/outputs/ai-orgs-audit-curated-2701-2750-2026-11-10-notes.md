# AI organization census audit: rows 2701–2750

Audit prepared: 2026-11-10. Requested opportunity-status cutoff: 2026-11-09.

## Source alignment

The output CSV contains 50 data rows, in original order, copied from rows 2701–2750 (header excluded) of `outputs/census-search-ledger-2026-11-09.csv`. Validation checked each census row number, organization name, tier, and category against the source. Output has the same 13-column schema used by neighboring audit slices. Source CSV was not edited.

## Findings

- **MegEngine is the strongest named-entity route found:** its official `MegEngine Contributor Program` (MECP) is aimed at university students and supports open-source contributions and community growth. Its contributor / Awesome MegEngineer recognition criteria are described in the official resource repository; this is a contribution and recognition route, not a campus ambassador cohort. The page includes a registration route and mentions a badge / commemorative gift. No cash stipend, geography, deadline, or current intake status was verified. The repository content includes older material and was inspected on Nov 10, so it does not establish that intake was open or terms unchanged at the Nov 9 cutoff.
- **Nixtla** has official student/researcher access and a contributor-swag community route. These are academic product access and open-source rewards, not ambassador roles. The official researcher page and docs page describe different access durations (up to six months versus 30 days with potential extension); this inconsistency is retained as a verification gap. No country exclusion is stated, but MUJ email acceptance is unknown.
- **ROS Navigation / Nav2** welcomes students to contribute code, docs, tutorials, and community support; maintainership may follow sustained contribution, but there is no clear formal process. A 2026 Nav2 documentation sprint was an adjacent volunteer contribution call, not ambassador recruitment.
- **Solace** offers user-facing conversations with experienced developer advocates, described as seasoned IT professionals. That is an employee-expert/customer engagement path, not a volunteer or student representative role.
- **Thunderbird** is identity-ambiguous as a census handle, but likely Mozilla Thunderbird. Search found a real 2026 campus ambassador program for Thunderbird School of Global Management (ASU); this is a different organization and was explicitly excluded as a false positive.
- **OpenMLSys** (Chinese/English ML-systems book) and **Agenta-AI** have public open-source contribution/community paths but no formal ambassador programs confirmed. The official OpenMLSys repo references a WeChat group; the group itself was not accessed, so local-channel recruitment may have been missed.
- For `transcranial`, search results surfaced Neuromatch and Society for Neuroscience ambassador programs, but the handle does not identify either organization. They are recorded as unaffiliated adjacent leads only, not named-entity opportunities.
- The remaining entries are bounded no-hits. Generic ambassador aggregators and third-party lists returned unrelated names often; these were not counted as organizational evidence. No-hit means no formal route was confirmed in the bounded search, not that no route exists.

## Search and evidence coverage

All 50 exact names were present in the census search ledger and were individually represented in its exact-name search-results records. I used Exa broad web discovery with official organizer pages, repositories, docs, and company pages prioritized, then checked the strongest candidate routes against their official pages. Search output was productive; no API rate-limit or access-limit error was returned. Quality varied substantially for short GitHub handles and common names, which is why the official-source preference and no-hit caveat matter.

Where practical, Chinese/local-channel context was considered through MegEngine's Chinese-language official community/resource pages and OpenMLSys's Chinese repository/book pages. I did not access closed or login-gated group channels (including WeChat), and did not use X MCP. Third-party pages, social snippets, and search-engine matches alone were not treated as proof. No accounts were created, applications submitted, forms entered, personal information supplied, or organizations contacted.

Current pages and search observations were made on Nov 10, after the requested cutoff. Each row distinguishes dated pre-cutoff context from Nov 10 observations; absent dated evidence is not presented as a cutoff-status claim. The audit does not establish completeness.

## Applicant fit and unresolved details

Fit is framed against the supplied applicant profile (18+, second-year B.Tech ECE student at Manipal University Jaipur, India, expected graduation 2029). No organization-specific MUJ eligibility was confirmed. MegEngine says the contributor program is for university students but does not state international scope; Nixtla's academic route does not state country restrictions but its university-email acceptance is unverified. Compensation, workload, deadlines, and status remain unknown except where an official page explicitly described a non-cash gift or travel support.

## Primary source URLs

- MegEngine Contributor Program and community: https://github.com/MegEngine/Resource/blob/master/Contributor_Program.md ; https://www.megengine.org.cn/community-joinus ; https://www.megengine.org.cn/community-AMGE
- Nixtla student/researcher access, docs, and contributor swag: https://www.nixtla.io/researchers-and-students ; https://www.nixtla.io/docs/introduction/ways_to_get_access ; https://swag.nixtla.io/
- Nav2 getting involved and Open Navigation: https://docs.nav2.org/rolling/community/getting_involved/ ; https://opennav.org/about/ ; https://docs.nav2.org/rolling/community/
- Solace developer advocate engagement: https://solace.com/engage-developer-advocate/
- Thunderbird identity and unrelated school program: https://www.thunderbird.net/ ; https://thunderbird.asu.edu/about/people/campus-ambassadors
- OpenMLSys: https://github.com/openmlsys/ ; https://openmlsys.github.io/v1/cn/
- Agenta-AI: https://github.com/Agenta-AI/agenta/ ; https://agenta.ai/docs/contributing/first-pr
- Adjacent, unaffiliated Neuromatch / SFN routes: https://neuromatch.io/ambassadors/ ; https://www.sfn.org/Advocacy/US-Advocacy-Programs/Early-Career-Policy-Ambassadors
