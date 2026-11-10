# Repository validation

Run the legacy project gate from the repository root:

```sh
python scripts/check.py
```

The script reads local files only. It does not search the web, submit applications, or change data. It exits nonzero if any of its 24 structural gates fail.

## What the 24 checks cover

- Presence and minimum size of the AI scope, curated organization list, program registry, tracker, census, universe, correction table, reports, coverage output, and wave plan.
- Whether every scope code appears in the curated list, the curated records have country/region labels, category counts meet the floor, and at least 20 country/region labels appear.
- Presence of `last_checked` on registry rows, at least one `OPEN` row, and an India or global region entry.
- Minimum counts for the organization census, org and curated tiers, AI-adjacent source layer, universe, tracker, domain corrections, and processed notable-scan names.

## Counts observed on 10 November 2026

These values are a dated structural snapshot, not current opportunity counts. The program source registry itself has not been rechecked after 7 November.

| Item | Observed value |
|---|---:|
| AI scope codes read by the checker | 32 |
| Curated AI organizations in `data/master-ai.csv` | 607 |
| Distinct country and region labels in that file | 37 |
| Baseline rows in `data/registry.csv` | 207 |
| Baseline rows marked `OPEN` | 95, last checked 7 November |
| Original tracker rows | 95 |
| AI organization census rows | 51,372 |
| Org plus curated census rows | 5,745 |
| AI-adjacent source rows | 167 |
| AI universe rows | 13,981 |
| Domain correction rows | 364 |
| Processed notable-scan names | 1,097 |

At the snapshot above, `python scripts/check.py` reported 24 passed and 0 failed. The assertion floors are intentionally lower than these observed values and can allow stale or weak content to pass.

## What this does not prove

The gate does not establish that a program is open now, accepts applicants in India, fits the user's requirements, has a valid application form, or is unique across files. It does not prove broad or worldwide completeness, semantic correctness of every CSV field, or that every organization has been researched. Passing the script is a structural floor only.

For the dated worldwide work, use [the current project state](research/2026-11-09/CURRENT-STATE.md), [the current action sheet](research/2026-11-09/outputs/APPLY-NOW-2026-11-10.md), and [the repository gap audit](research/2026-11-09/REPO-GAP-AUDIT-2026-11-10.md). The archive's CSV structure is checked separately by `scripts/validate_archive.py`; its limits are documented in the audit.
