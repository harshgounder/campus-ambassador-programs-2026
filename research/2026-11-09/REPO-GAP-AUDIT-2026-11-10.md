# Repository and research gap audit

- **Audit date:** 10 November 2026
- **Research cutoff:** 9 November 2026
- **Scope:** Full repository structure, core data and report claims, continuation notes, scripts, GitHub metadata, and the quality dimensions in the supplied rubric.
**Conclusion:** This is a substantial research archive with useful provenance and a long correction history. It is not yet a professional, self-checking research system. The most consequential problems were stale claims presented without a clear historical label, a broken continuation handoff, no automated test or CI layer, and no shared validation for the many research CSVs.

## Highest-risk findings

### 1. Continuation state conflicted across files

The append-only `outputs/RESUME-STATE-AND-AUDIT.md` contains multiple rank checkpoints, including ranks 800 and 1,950, as well as the later rank 3,550 state. Under repeated context compression, a model could resume from an obsolete section or mistake an intermediate count for the current one. The archive publication is also described in an older section as still being packaged, even though the archive was published in commit `fc0362c`.

**Fix:** `CURRENT-STATE.md` is now the only current checkpoint. The append-only resume file is explicitly historical. Its old ranks remain for audit history but no longer compete with the current resume point.

### 2. Several top-level documents contradict the actual source data

- `CHECKER.md` described 24 taxonomy codes, 486 organizations, and 174 program rows. At audit time, `scripts/check.py` reports 32 scope codes, `data/master-ai.csv` has 607 rows, and `data/registry.csv` has 207 rows.
- `REPORT-AI-SCOPE.md` and `ALL-ORGS.md` still describe the older 486-organization/24-category snapshot.
- `ALL-PROGRAMS.md` shows 99 `OPEN` rows, while the current baseline registry has 95. The 95 registry rows were last checked on 7 November, so even the correct count is not current application truth.
- `scope/PROFILE.md` contained program-specific pass/fail claims and stacking advice from an earlier point in the project. Those claims were stale, including its treatment of the Qualcomm student route.

**Fix:** The profile has been reduced to applicant facts and unknowns. The current README and action sheet identify older program and organization lists as baseline snapshots. `CHECKER.md` now documents what the 24-check script does and does not prove.

### 3. The source data is split across many files without a single current action ledger

The baseline registry and tracker do not include the later worldwide follow-up work. The 275-row AI priority ledger and hundreds of lane files include mixed states, overlaps, and differing schemas. A reader needs to know which file to open and whether an entry is a confirmed opening, a live-looking form, a future route, an adjacent opportunity, or a lead with unresolved country rules.

**Fix:** `outputs/APPLY-NOW-2026-11-10.md` provides a dated starting point, separates apparent fit from unresolved eligibility, and links to the underlying evidence files. It does not claim that every global program is included. The wide source-ledger reconciliation remains unfinished.

### 4. Current-status language has repeatedly produced false “open” results

The project already corrected several cases where a landing-page CTA or stale directory listing was mistaken for a live application. Examples include Zed's closed form, the expired AWS Group Leader listing versus the distinct active Campus Leader, closed Google Gemini and OpenAI India intakes, and the restricted Adobe and Twilio routes. The same failure mode remains possible in any undated lane file unless the actual form and country requirements are checked.

**Fix:** The action sheet carries observed dates and keeps `open`, `open-appearing`, `rolling`, `undated`, `future`, `closed`, `restricted`, and `unknown` distinct. It instructs the reader to verify the final form and India eligibility before applying.

## Repository quality dimensions

The supplied rubric is treated as a review checklist. This is a static research and data repository, not a web service or deployed infrastructure project. Scores for logging, health endpoints, service metrics, and IaC would be misleading here, so those are marked not applicable unless a future service is introduced.

| Dimension | State found at audit | Relevant fix or boundary |
|---|---|---|
| B. Test coverage | The repository originally had no tracked tests. It now has six focused test modules and 19 tests for CSV parsing, tree scanning, CLI behavior, manifest hashing, and key data contracts. These tests were added during the 10 Nov quality pass, so there is no mature test history and the network collectors remain untested. | Keep coverage tied to deterministic behavior. Add tests before changing collectors or research semantics; do not treat the new suite as broad behavioral coverage. |
| C. Code cleanliness | The repository now has a pinned Ruff configuration. All 35 scripts and test modules pass the configured lint and format checks. The current scripts contain 3,770 nonblank lines, a 90th-percentile file size of 157 lines, and one file over 500 lines (`scripts/master_ai.py`, a hardcoded historical organization builder). | Retain the lint gate and keep future code modular. Refactor the large historical builder only alongside tests that protect its output. |
| D. Architecture and robustness | Primarily standalone scripts; `requests` is the only third-party runtime import. Some legacy network scripts execute at module scope. The two new archive tools have deterministic functions and explicit command entry points. | Document supported Python and execution context. New tools should be safe to import. Logging, error tracking, health endpoints, and service metrics are not applicable to this static research repository. |
| E. Dependency health | Runtime and development dependencies are declared. `requirements.lock` is a hash-complete lock compiled for Python 3.11; weekly Dependabot updates cover Python packages and GitHub Actions. | Keep runtime dependencies small and review automated updates. Vulnerability audit result is recorded after the final CI run. |
| F. Docs and onboarding | The root README is detailed and GitHub About/topics were already present. Current status and resume files now lead the reading path; `CONTRIBUTING.md`, `SECURITY.md`, and `CHANGELOG.md` were added. | Keep the current checkpoint and dated action sheet synchronized. A repository license is still a repository-owner decision and was not invented. |
| H. CI/CD | The repository now has a read-only GitHub Actions quality workflow for lint, tests, the baseline gate, CSV structure, manifest consistency, and dependency audit. There is no deploy target to automate. | Maintain the quality workflow. Type checking and deployment are not current project needs. |
| I. Security hygiene | Local environment and secret files are ignored. A security policy and data-handling boundaries are documented. A content scan of tracked and newly changed files is recorded below before publication. | Keep secrets and private application material out of the public archive. Dependency audit can only cover declared Python packages and known advisories. |
| K. History and maintenance | Existing history includes a large 777-path archive snapshot. It remains untouched. A changelog now records the 10 Nov maintenance work. | Use small, scoped commits from this point forward. Do not rewrite the existing public history. |
| M. Reproducibility | Runtime and development dependencies are pinned with hashes. `archive_manifest.py` creates or checks a deterministic SHA-256 inventory; CSV structure validation can run without network access. Search-provider output remains evidence, not reproducible ground truth. | Regenerate and verify the manifest after every dated archive change. Keep discovery inputs distinct from verified program records. |
| N. Pipeline and data quality | The new repository-wide structural scan checked 428 CSV files and 190,134 nonblank data rows with consistent parsing and widths. Tests also protect core registry, tracker, and AI-ledger fields. These checks do not detect duplicate program identities, false status, malformed semantic values, or missing eligibility. A prior AI ledger audit found a URL list placed in a compensation field. | Add targeted semantic rules when schemas stabilize. Continue source-level review and program deduplication. Never use structural row counts as opportunity counts. |
| O. IaC quality | Not applicable. No application infrastructure, cloud deployment, Terraform, or Kubernetes is part of this repository. | Do not add IaC merely to satisfy a generic score. Revisit only if a deployed service is added. |
| P. Secrets and threat modeling | The repository now has a concise threat model and safe-reporting instructions in `SECURITY.md`. Credential storage and a professional threat assessment remain outside this static public project. | Keep credentials and unsubmitted form data out of tracked files. Revisit the model if the repository starts handling private applications or becomes a service. |

## Validation performed on 10 November

- Ruff lint and format checks passed across the 35 Python scripts and 6 test modules.
- The test suite passed all 19 tests.
- The original project checker passed all 24 checks.
- The repository-wide CSV scan parsed 428 files and 190,134 nonblank data rows with zero structural issues.
- A targeted scan checked 1,016 tracked and unignored new files against seven high-confidence credential patterns. It found zero candidate matches. This was not a full secret-scanning product.
- `pip-audit` 2.10.1 reported no known vulnerabilities in the 30 pinned runtime and development packages in `requirements.lock`. The advisory lookup depends on its external vulnerability data source.
- The archive manifest is regenerated and checked separately after the final file synchronization.

## Research coverage gaps that remain

1. The 5,745 organization and curated AI-name screen is complete as a bounded exact-name screen. It does not prove that all AI organizations or programs have been found.
2. AI small-tier ranks 3,551 through 9,304 remain. All 36,323 individual-tier accounts remain outside the exact-name review. Prioritize likely organizations, labs, projects, and organizers among them.
3. The 275-row AI ledger is mixed-status and not consolidated with the main registry. Some later research lanes were checked on 10 November and do not establish their 9 November state.
4. The broad CS, software, developer tools, cloud, cyber, hardware, startups, and wider technology map has not been systematically completed. Existing first-wave, Opportunity Max, GitHub, Hacker News, local-language, and browser files are lead sources, not a completeness proof.
5. Search coverage is not even across small companies and local-language communities. China and other regional work exists, but the remaining follow-up queue is still substantial.
6. Individual application forms have not been submitted. No organizer has confirmed unresolved country, campus, capacity, payment, or age questions on the user's behalf.

## Order of work

1. Keep the apply-now sheet dated and refresh time-sensitive openings from organizer pages and actual forms.
2. Resume AI small-tier screening at rank 3,551 in reproducible 50-row slices while continuing targeted program discovery across the full AI/ML map.
3. Reconcile valid opportunities into one stable identifier and one canonical record, retaining closed and uncertain states rather than deleting inconvenient results.
4. Finish the remaining AI source and community lanes, including non-LLM subfields, localized and Chinese channels, open-source projects, labs, forums, and technical communities.
5. Then complete the systematic worldwide CS, software, cybersecurity, cloud, hardware, startup, and broader technology pass.
6. Recheck every actionable record against the organizer's own page or application, keep the 9 November cutoff separate from later observations, and update this audit as coverage improves.
