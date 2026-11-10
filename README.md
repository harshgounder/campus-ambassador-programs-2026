# Campus Ambassador Programs 2026

[![Research status](https://img.shields.io/badge/research-in%20progress-2f855a)](research/2026-11-09/README.md)
[![Quality checks](https://github.com/harshgounder/campus-ambassador-programs-2026/actions/workflows/quality.yml/badge.svg?branch=master)](https://github.com/harshgounder/campus-ambassador-programs-2026/actions/workflows/quality.yml)
[![Scope](https://img.shields.io/badge/scope-worldwide-2455a4)](research/2026-11-09/CURRENT-STATE.md)
[![Status cutoff](https://img.shields.io/badge/status%20cutoff-09%20Nov%202026-6f42c1)](research/2026-11-09/README.md)
[![GitHub stars](https://img.shields.io/github/stars/harshgounder/campus-ambassador-programs-2026?style=social)](https://github.com/harshgounder/campus-ambassador-programs-2026/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/harshgounder/campus-ambassador-programs-2026/master)](https://github.com/harshgounder/campus-ambassador-programs-2026/commits/master)
[![Repository size](https://img.shields.io/github/repo-size/harshgounder/campus-ambassador-programs-2026)](https://github.com/harshgounder/campus-ambassador-programs-2026)

A source-backed, worldwide search for student, campus, developer, and community ambassador programs, with dated status checks and eligibility notes.

**Research is in progress.** The current status cutoff is 9 November 2026. Checks performed on 10 November are dated as such and do not automatically prove that an application was open on the cutoff date. This repository does not claim that every program worldwide has been found.

## Contents

- [Current research status](#current-research-status)
- [Start with these files](#start-with-these-files)
- [Scope and applicant profile](#scope-and-applicant-profile)
- [Count reconciliation](research/2026-11-09/outputs/SCOPE-AND-COUNT-RECONCILIATION-2026-11-10.md)
- [Research method](#research-method)
- [How to read status and eligibility](#how-to-read-status-and-eligibility)
- [Data guide](#data-guide)
- [AI and machine learning coverage](#ai-and-machine-learning-coverage)
- [Repository layout](#repository-layout)
- [Development and validation](#development-and-validation)
- [Research limitations](#research-limitations)
- [Contributing and security](#contributing-and-security)
- [Reuse](#reuse)

## Current research status

The figures below describe separate research collections. They are not counts of currently open programs, eligible opportunities, or a complete worldwide census.

| Collection | Current snapshot | What the number means |
|---|---:|---|
| Original program registry | 207 rows | The dated baseline registry in data/registry.csv. It is not the consolidated 9 November global results table. |
| Original application tracker | 95 rows | A working tracker from the earlier project phase. Check each source before acting. |
| Curated organization list | 607 rows | The original curated AI organization list in data/master-ai.csv. |
| AI organization census | 51,372 names | A mixed-tier discovery census. A name is a search lead, not a verified program. |
| Separate AI universe | 13,981 names | A distinct discovery set that overlaps the census and other records. These are not program counts. |
| AI priority ledger | 275 mixed-status records | The 10 November working ledger. It includes open, closed, future, restricted, unclear, and adjacent routes. |
| Curated AI organization audit | 5,745 of 5,745 rows | Exact-name source screening across the org and curated tiers. A screen is not proof that every alias or private community was found. |
| Small-tier AI audit | 3,550 of 9,304 rows | Source-aligned ranks screened in contiguous batches. The next rank is 3,551. |
| Individual-tier AI accounts | 36,323 names | Not yet screened one by one. |
| Dated research outputs | 410 CSV files, 53,734 data rows | Structural parse and consistent row-width check recorded on 10 November. These are research rows, not opportunities. |

These figures measure different datasets, units, and stages of research. They overlap and must not be added together as opportunities. The apply-now sheet is a priority list, not a full count of open routes. It now includes two further routes found in 10 November checks, while keeping their eligibility and date limits visible. Read the [count reconciliation](research/2026-11-09/outputs/SCOPE-AND-COUNT-RECONCILIATION-2026-11-10.md) before comparing numbers. The AI organization census and the program ledgers answer different questions. The census helps identify organizations and projects to investigate. Only a source-backed program record can support a claim about a role, intake, deadline, or applicant eligibility.

## Start with these files

| File | Purpose |
|---|---|
| [Current project state](research/2026-11-09/CURRENT-STATE.md) | One current continuation point, current census rank, and the order of unfinished work. |
| [Apply-now action sheet](research/2026-11-09/outputs/APPLY-NOW-2026-11-10.md) | Current routes checked on 10 November, profile fit, deadlines, costs, and unresolved eligibility. |
| [Scope and count reconciliation](research/2026-11-09/outputs/SCOPE-AND-COUNT-RECONCILIATION-2026-11-10.md) | Explains the large discovery counts, smaller program counts, and why the action table is only a priority subset. |
| [Cross-sector candidate report](research/2026-11-09/outputs/all-sector-open-route-candidates-2026-11-10.md) | 194 source-reconciled open-looking or unresolved candidates from selected non-AI-specific global and cross-sector lanes. This is not the entire universe. |
| [Direct AI/ML route rechecks](research/2026-11-09/outputs/ai-open-routes-direct-recheck-001-104-2026-11-10.md) and [second batch](research/2026-11-09/outputs/ai-open-routes-direct-recheck-105-207-2026-11-10.md) | Official-page checks for 207 AI/ML candidates, with open, undated, uncertain, adjacent, and closed states separated. |
| [Technology-wide coverage audit](research/2026-11-09/outputs/technology-wide-scope-audit-2026-11-10.md) | Current coverage by technology area and the work still required for a broad map. |
| [Repository gap audit](research/2026-11-09/REPO-GAP-AUDIT-2026-11-10.md) | Research coverage gaps, stale records, and improvements based on the supplied quality rubric. |
| [Research archive guide](research/2026-11-09/README.md) | Current checkpoint, archive layout, counts, and resume order. |
| [Current AI research queue](research/2026-11-09/outputs/AI-RESEARCH-COVERAGE-AND-QUEUE-2026-11-10.md) | AI field map, completed census ranges, remaining work, and the next research queue. |
| [Historical continuation log](research/2026-11-09/outputs/RESUME-STATE-AND-AUDIT.md) | Append-only intent reconstruction and checkpoints. Use `CURRENT-STATE.md` for today's resume point. |
| [Worldwide application checks](research/2026-11-09/outputs/WORLDWIDE-APPLICATIONS-BRAVE-CHECKED.md) | Direct page and form observations, with dates and unresolved conditions. |
| [AI priority ledger](research/2026-11-09/outputs/ai-ml-priority-verification-delta-2026-11-09.csv) | Mixed-status AI and adjacent technology records. Read each row's evidence and limitation fields. |
| [Small-tier AI audit queue](research/2026-11-09/outputs/ai-orgs-small-tier-search-ledger-2026-11-10.csv) | Source-aligned queue of 9,304 small-tier names and audit ranks. |
| [Output file index](research/2026-11-09/outputs/FILE-INDEX.md) | Searchable links to the saved output files. |
| [Full file manifest](research/2026-11-09/FILE-MANIFEST.csv) | File sizes and SHA-256 checksums for the dated archive. |

The earlier [REPORT.md](REPORT.md), [START-HERE.md](START-HERE.md), and [ALL-PROGRAMS.md](ALL-PROGRAMS.md) remain available as dated baseline material. They are not the current application shortlist. Each file now has a note explaining its snapshot date and current replacement.

## Scope and applicant profile

The research targets ambassador and closely related student leadership routes that may accept this applicant profile:

- At least 18 years old.
- Second-year B.Tech student in Electrical and Computer Engineering at Manipal University Jaipur, India.
- Expected graduation in 2029.
- Open to remote, campus-based, and online roles.

The search is worldwide and covers every industry and subject area. The full technology industry is a major lane, with AI and machine learning as the highest research priority. Examples provided during the work are prompts to expand discovery, not limits on what is searched. India is one eligibility check because it is the applicant's location, not a limit on where programs are sought. A program is not treated as India-eligible solely because its page uses words such as global or worldwide. Restrictions by country, university type, degree, year, age, language, prior contribution, workload, and application capacity are recorded when published or remain marked unknown.

The project includes campus ambassador, student partner, campus leader, developer champion, chapter lead, community organizer, technical advocate, and comparable roles. Adjacent fellowships, creator programs, research internships, competitions, event campaigns, or product referral schemes are kept distinct from ambassador appointments.

The original scope files describe the earlier project phase. The dated archive carries the current worldwide scope and resume instructions.

## Research method

The work follows a discovery and verification sequence:

1. Build candidate lists from organization catalogs, public repositories, field maps, product ecosystems, communities, and regional sources.
2. Search beyond the title ambassador. Relevant terms include campus lead, student partner, chapter lead, developer champion, community advocate, evangelist, educator, user-group organizer, and local-language equivalents.
3. Resolve the organization and program identity before accepting a search result or directory entry as relevant.
4. Prefer the organizer's own program page, application form, rules, or dated announcement. Use directories, social posts, and search results to discover candidates, not as automatic proof of current status.
5. Record the observed date, application route, deadline, geography, published requirements, workload, compensation, and unresolved questions where available.
6. Compare each published requirement with the applicant profile. Keep unclear and conflicting requirements visible.
7. Recheck the original source close to the status cutoff when possible. A working form, page response, or undated announcement does not alone establish that a cohort is accepting applications.

Source strength varies by claim. An organizer page may establish a role exists, while a separate application form may establish its current fields. A third-party post can be useful discovery evidence but may not establish selection authority or eligibility. Individual records retain links and notes so those distinctions can be reviewed.

## How to read status and eligibility

The research uses separate status labels instead of folding uncertain cases into open:

| Status | Meaning |
|---|---|
| Open | The organizer explicitly presents an active application window for the stated period. |
| Open-appearing | A route or form appears active, but the source does not establish all details or the exact cutoff state. |
| Rolling | The organizer says applications are reviewed on an ongoing basis or accepts them year-round. |
| Undated route | An application or contact route exists, but current acceptance is not confirmed. |
| Future | A later cycle or opening is announced, or the route is not yet open. |
| Closed | The relevant cycle has ended or the organizer says applications are closed. |
| Restricted | A published requirement excludes the applicant or the role is limited to a different group or location. |
| Unknown | Available evidence does not resolve the current status or a material eligibility condition. |
| Adjacent | A related opportunity exists but is not clearly an ambassador appointment. |

Eligibility is assessed from published rules, not assumptions. A live link is not the same as an open cohort. A student meeting age and degree requirements may still face country, campus, language, selection, or capacity limits.

## Data guide

The baseline registry and follow-up archive are deliberately separate. New follow-up records have not been silently merged into the legacy registry.

| File | Description |
|---|---|
| data/registry.csv | 207 baseline program records with status, deadline, link, evidence, and last-checked fields. |
| data/tracker.csv | 95 records in the earlier application tracker. |
| data/master-ai.csv | 607 curated AI organization records with category and country. |
| data/ai-orgs-census.csv | 51,372 names grouped by source tier, with category and source metadata. |
| data/ai-universe.csv | 13,981-name AI universe source used in the original research phase. |
| data/coverage.json | Coverage calculation from the original project tooling. |
| data/domain_corrections.csv | Domain corrections applied to the original organization coverage work. |
| research/2026-11-09/outputs | Dated follow-up findings, audit slices, search results, and evidence notes. |
| research/2026-11-09/work | Saved raw research responses and helper files used in that research pass. |

The archive has an [output index](research/2026-11-09/outputs/README.md) and a [work index](research/2026-11-09/work/README.md). The complete checksum list is available as the [file manifest](research/2026-11-09/FILE-MANIFEST.csv).

## AI and machine learning coverage

AI has first priority and is treated as a broad technical field. The research map includes:

- Learning theory, statistics, optimization, supervised and unsupervised learning, self-supervision, transfer, continual and federated learning, causal methods, reinforcement learning, planning, and neuro-symbolic systems.
- Model families and architectures, including language and foundation models, generative methods, graph learning, efficient models, world models, and multi-agent systems.
- Language technology, speech and audio, computer vision, video, document understanding, multimodal systems, and low-resource languages.
- Robotics, embodied AI, control, autonomous systems, simulation, and edge intelligence.
- Scientific and applied AI across health, biology, chemistry, climate, energy, agriculture, geospatial work, education, finance, and accessibility.
- Data, knowledge, datasets, retrieval, evaluation, infrastructure, chips, accelerators, training, inference, compilers, serving, MLOps, and compute access.
- Safety, security, governance, privacy, robustness, interpretability, standards, red teaming, and AI-enabled cybersecurity.
- Open-source projects, labs, campus chapters, community groups, conferences, and regional ecosystems, including Chinese and other local-language sources.

Broad discovery across all fields continues while the AI and full technology maps are developed. The technology search includes computer science, software engineering, languages and frameworks, developer tools, open source, cloud and DevOps, data platforms, cybersecurity, chips and hardware, embedded systems, telecom and networking, robotics, quantum, startups, and other areas. Web3 and cryptocurrency are some parts of that field, not the entire technology scope. Other industries and communities remain in scope too.

## Repository layout

- data/ contains baseline program and organization tables plus source and audit files.
- scripts/ contains the original collection, checking, coverage, and correction tools.
- scope/ records the original project scope, AI taxonomy, and applicant profile.
- research/2026-11-09/ contains the dated worldwide follow-up archive, including its outputs, raw work files, indexes, and manifest.
- research/2026-11-09/CURRENT-STATE.md is the only current resume point; the resume log under outputs/ is historical.
- REPORT.md and related root documents are earlier snapshots and method notes.
- evidence/ is retained from the early project structure; the saved evidence pages are documented in EVIDENCE.md and the dated archive.

This layout keeps the original baseline data recognizable while giving the follow-up a clear date and its own index.

## Development and validation

Python 3.11 or newer is supported. Install the pinned runtime and development tools, then run the local checks from the repository root:

```sh
python -m pip install -r requirements.lock
ruff check scripts tests
python -m unittest discover -s tests -v
python scripts/check.py
python scripts/validate_archive.py
python scripts/archive_manifest.py --check
pip-audit --no-deps --timeout 5 --progress-spinner off -r requirements.lock
```

GitHub Actions runs the same checks for pushes and pull requests. Dependency and workflow updates are checked weekly. The default checks are local and read-only. They do not open websites, fill forms, or contact program organizers.

The 24-check baseline gate in `scripts/check.py` enforces structural floors for the original project artifacts. `scripts/validate_archive.py` checks CSV syntax and consistent row widths throughout the repository. `scripts/archive_manifest.py --check` verifies the dated archive's file sizes and SHA-256 values. `ruff` checks Python style and common errors; the unit tests cover the CSV and archive validation tools and key dataset contracts. `pip-audit` checks the pinned Python dependencies against its vulnerability sources.

These checks do not verify current program status, prove worldwide completeness, validate every semantic field, or decide whether two differently named records are the same program. A successful check is not proof that every research claim is correct.

## Research limitations

Search coverage cannot prove that every program has been discovered. Private groups, closed messaging channels, changing pages, local terminology, and unindexed forms can hide opportunities. Search results can be stale, duplicated, or about a different organization. Status may change after observation. Recheck the organizer source before applying and treat unknown conditions as unknown.

No application forms have been submitted as part of this research. Inspection of a public form does not mean that data was entered or an application was sent.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for the evidence and status rules, local workflow, and validation commands. Read [SECURITY.md](SECURITY.md) before running network scripts or reporting a suspected exposure. Repository maintenance changes are summarized in [CHANGELOG.md](CHANGELOG.md).

## Reuse

This repository currently has no LICENSE file. No open-source reuse terms have been declared. Contact the repository owner before reusing the code or datasets.

[Back to top](#campus-ambassador-programs-2026)
