# AI/ML exact-name audit — source rows 1401–1450

Date prepared: 2026-11-10. Status cutoff requested: 2026-11-09. Candidate profile supplied for relevance: 18+, second-year B.Tech ECE, Manipal University Jaipur, India, graduating 2029.

## Method and limits

Ran one exact-name web search per source label, pairing the quoted label with student ambassador, campus ambassador, ambassador program, developer ambassador, or community champion wording appropriate to the entity. Searches were throttled sequentially in groups of at most four; all 50 calls returned search payloads. Search results were discovery evidence, not exhaustive coverage. No search failure was treated as a no-hit. Exact-name searches can miss differently named or poorly indexed programs, non-English pages, and routes that do not use ambassador language. Common names/handles can yield noisy or mismatched results. No-hit means no route was confirmed in this bounded pass, not proof of absence.

Deep-checked primary pages for Streamlit Creator and Advocate, Kong Champions, Milvus community context, and Google Research student engagement. Current pages do not by themselves establish historical status at the Nov 9 cutoff. Google Research fellowships, student-research placements and research internships were excluded as research/internship opportunities, not student leadership roles. No forms were submitted, accounts created, outreach made, or X MCP used.

## Confirmed opportunity pages and adjacent lead

- **Streamlit, row 1402:** Official pages describe the Streamlit Creator and Advocate community programs. The Creator role involves publishing apps/components/content, helping community members, contributing feedback/PRs, testing features and quarterly meetups. Benefits include product-team access, amplification, credential, collaboration and swag. The current page says “Applications open in November,” but it is undated and does not establish that intake had opened by Nov 9. The Advocate page offers content/video training, one-on-one support, global promotion and swag, and describes earning potential from sponsored content, affiliate marketing and courses. It has a Get Started application route but no dated intake evidence. Neither page publishes age, student/year/major or India-specific terms; candidate fit and current acceptance remain unconfirmed. Official sources: https://streamlit.io/become-a-creator and https://streamlit.io/community/advocates.

- **Kong, row 1412:** Official Kong Champions is an advocacy/community-recognition route for Kong users, including open-source users, with champions around the world. Described activities include forums, blogs, videos, webinars, speaking/hosting events, feedback, reviews and customer stories. Perks include early product access, private group/events, recognition, team access and swag. The official page invites applications and says review is monthly. It does not publish an age, student/year/major, duration, workload or cash-pay requirement. Global wording suggests international participation but is not explicit about India; cutoff state is not dated. Source: https://konghq.com/community/kong-champions.

- **Milvus, row 1401:** A Milvus-branded Medium article describes community contributors called “Milvus Ambassadors” who organize events and answer forum questions. The official community page lists Slack, Discord, GitHub, office hours and social channels but no ambassador intake, selection route or role terms. This is an adjacent descriptive lead, not a verified open opportunity. No cutoff, India, age, academic, workload or benefit terms were established. Sources: https://milvusio.medium.com/our-journey-to-35k-github-stars-the-real-story-of-building-milvus-from-scratch-e1344a493a94 and https://milvus.io/community. Prior exact-name audit row 316 recorded no actionable Milvus route; this review likewise found no application route.

- **Google Research, row 1433:** Official student-engagement page lists fellowships, student research opportunities and research internships; these do not meet the requested representative/ambassador/student-leader scope and were excluded. Source: https://www.research.google/programs-and-events/student-engagement/.

Other exact-name results were mostly source identity/profile pages, unrelated generic ambassador directories, third-party programs, ordinary community or OSS participation, commercial pages, event/hackathon results, jobs, courses or noisy matches. They were not promoted to candidate opportunities without an exact-entity primary source for a qualifying role.

## Duplicate checks

Searched the existing AI audit slice CSVs, the prior source-row 1301–1350 notes, and `outputs/ai-ml-priority-verification-delta-2026-11-09.csv` for Milvus, Streamlit and Kong/Champions routes. Milvus appears in prior audit row 316, where no actionable student route was found. No exact actionable Streamlit Creator/Advocate or Kong Champions route duplicate was found in those reviewed files. The Google Research student/research links are not qualifying ambassador duplicates.

## Exact-name search roster

One quoted exact-name query was submitted for each source row: milvus-io; streamlit; coqui-ai; anthropics; AstrBotDevs; logseq; Wei-Shaw; chatanywhere; reactive-resume; NaiboWang; danielmiessler; Kong; ray-project; gradio-app; aymericdamien; ifixai-ai; deepspeedai; agno-agi; apachecn; tinyhumansai; chatboxai; wshobson; lyogavin; volcengine; codewhale-hq; patchy631; pingcap; ShareX; linshenkx; Yeachan-Heo; photoprism; drawdb-io; google-research; VectifyAI; mindsdb; The-Vibe-Company; floodsung; ashishpatel26; RSSNext; storytold; naptha; chatchat-space; TriliumNext; AlexsJones; JCodesMore; CopilotKit; sgl-project; Dokploy; PDFMathTranslate; fengdu78.

## Row validation

The slice file preserves `census_row`, `name`, `tier`, and `category` verbatim from 1-based source rows 1401–1450 (header excluded). Independent full-slice validation checked exact 13-column schema, 50-row count, unique row IDs, 13 fields per row, source alignment for all four preserved source fields, and a nonempty identity/source URL for every row. Nonhits are bounded findings and do not assert absence.
