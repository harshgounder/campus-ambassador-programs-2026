# AI organization census audit: rows 751–800

Audit date: 2026-11-10. Status cutoff: 2026-11-09. The source census records were read with the header excluded and preserve source `name`, `tier`, and `category` exactly.

## Scope and findings

This slice contains Hugging Face/research identities, individual model maintainers, model/community namespaces, an AI product vendor and a multilingual music platform. A repository, model publisher, username, project, or product label is not automatically a legal organization or a campus-recruiting sponsor. Targeted official-source searches did not confirm a named student ambassador application for 47 of 50 entries. The three more clearly identifiable ecosystem cases are recorded separately in the CSV: BigScience (historical open research workshop, with no current student ambassador intake confirmed), ONNX (community and event participation, not a formal student ambassador route located), and Infomaniak (commercial membership/partner routes, not student ambassador roles). No named entity had an open application or deadline confirmed as of the cutoff.

The CSV's identity URLs point to an identifier/profile when available; they are not evidence of employment, formal organizational identity, student eligibility, or an ambassador program. Search results supplied for many census records included third-party campus-program pages and unrelated names; those were excluded as evidence of affiliation. Negative findings are bounded, not proof that no route exists.

## Cross-organization leads

The rows repeat a clearly labeled, unaffiliated set of broader AI/developer routes to retain practical context: OpenAI Student Collective (India included in Fall 2026, but closed); Claude Campus (global undergraduate route with 18+ and local work-authorization conditions, closed 2026-09-12); Google Developer Groups on Campus; Microsoft Copilot Student Ambassador (country terms require current verification); and Red Hat Academy Student Ambassador (Academy coursework and instructor nomination required). These are leads for separate verification, not opportunities offered by the census entities. No program-specific workload or cash/noncash benefit is inferred for the named entities. The MUJ student's age, current year, ECE fit and country eligibility need checking against an actual open program's terms.

## Structural verification

The output has 50 data rows and 13 columns. Programmatic comparison against source data rows 751–800 (excluding the header) matched every `census_row`, `name`, `tier`, and `category`. First/middle/last checks: row 751 `bigscience` / `org` / `text-gen`; row 775 `hustvl` / `org` / `multimodal`; row 800 `infinitejoy` / `org` / `audio`.

Sources reviewed include official project/community pages for the exceptions above and program pages for cross-organization leads:

- https://bigscience.huggingface.co/
- https://bigscience.notion.site/Organization-292995757b644b1db4acfa9a5705f4ae
- https://onnx.ai/
- https://lfaidata.foundation/
- https://www.infomaniak.com/en/membership
- https://news.infomaniak.com/en/reseller-and-partner-programme
- https://openai.com/form/openai-campus-leaders-interest-form/
- https://claude.com/programs/campus
- https://developers.google.com/community
- https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/copilot-student-ambassador
- https://access.redhat.com/community/learn/academy/become-red-hat-student-ambassador

No applications were submitted and no one was contacted.
