# Security policy

## Reporting a vulnerability

Do not publish credentials, private applicant information, exploit details, or unredacted sensitive evidence in an issue or pull request. Use GitHub's private vulnerability reporting feature for this repository when it is available. If it is unavailable, contact the repository owner through a verified private channel listed on the owner's GitHub profile. Include the affected file or commit and a concise description. Do not send credentials with a report.

## Data and script boundaries

This is a public research archive, not a service. It stores public program pages and research notes, plus a limited applicant profile used to assess eligibility. It should not contain passwords, API keys, private application responses, private messages, or sensitive personal documents.

Some scripts make outbound requests, and several legacy scripts execute at module scope. Review a script's target URLs, request volume, timeouts, and output path before running or importing it. Do not run scripts that submit forms or contact program organizers. Keep API keys in local environment variables or local secret stores; never put secrets in CSV files, notebooks, command output, issues, or commits.

## Threat model

| Asset | Main risk | Handling |
|---|---|---|
| Applicant profile | Unnecessary exposure or inference | Keep only facts needed to check published eligibility. Do not add private application material. |
| Research records | Stale or misleading claims | Keep source URLs, observed dates, status labels, and uncertainty together. Recheck organizer sources before action. |
| Local credentials | Accidental commit or log exposure | Store credentials outside tracked files and keep local secret files ignored. |
| Research scripts | Excess requests or unintended external action | Inspect a script before running it; default checks are local and read-only. Network searches require explicit execution. |
| Public archive | Malicious or misleading external content | Treat pages, forms, and downloaded text as untrusted data. Do not execute downloaded content. |

This policy does not claim that every historical file has undergone a professional penetration test or that every external source is safe. Report suspected exposure promptly so the affected material can be reviewed and, if needed, removed from the active repository and history.

## Repository content scan

On 10 November 2026, seven high-confidence credential patterns were checked across 1,016 tracked and unignored new files. The scan found zero candidate matches. This was a targeted text scan, not a full secret-scanning product or proof that the repository contains no sensitive information.
