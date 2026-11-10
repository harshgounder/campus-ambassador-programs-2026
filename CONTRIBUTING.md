# Contributing

This repository combines a dated research archive with the tools and baseline data used to maintain it. The archive is intentionally incomplete and time-sensitive. Contributions should preserve source trails and make the research state easier to review.

## Before changing research records

- Prefer the organizer's own program page, application form, rules, or dated announcement for claims about a role, intake, deadline, and eligibility.
- Record the source URL and the date it was checked. Keep a later observation separate from the 9 November 2026 cutoff.
- Keep `open`, `open-appearing`, `rolling`, `undated route`, `future`, `closed`, `restricted`, `unknown`, and `adjacent` distinct. Do not infer an open intake from a working link or an undated Apply button.
- Compare country, student status, degree, year, age, language, experience, campus, capacity, time, and cost requirements with published criteria. Leave unresolved requirements marked as unknown.
- Preserve closed and conflicting evidence when it prevents a false positive. Reconcile duplicates using source evidence instead of deleting a record because it is inconvenient.
- Keep discovery leads, verified program records, application submissions, and adjacent opportunities as separate concepts.
- Do not add personal application data, private form responses, credentials, or organizer messages without the applicant's direction.

## Code and data changes

- Keep source data and generated output changes reviewable. Do not regenerate the entire research archive to make a small correction.
- Add or update tests for changed behavior. Tests must be deterministic and must not submit forms, contact organizers, or depend on a live website.
- Keep new tools safe to import. Many legacy research scripts execute at module scope, so do not import them as libraries; read the script and run it only when you intend its file or network operations.
- Update the current state, relevant index, and archive manifest when changing dated research files.
- Use small commits with a clear purpose. Do not rewrite the published history.

## Local checks

Use Python 3.11 or newer. From the repository root, install the pinned development environment and run the same checks used by CI:

```sh
python -m pip install -r requirements.lock
ruff check scripts tests
python -m unittest discover -s tests -v
python scripts/check.py
python scripts/validate_archive.py
python scripts/archive_manifest.py --check
pip-audit --no-deps --timeout 5 --progress-spinner off -r requirements.lock
```

The CSV validator checks syntax and row widths. It does not validate opportunity status, source authority, eligibility, completeness, or duplicate identity. The original project checker enforces baseline structural rules. The manifest checker compares archive files with their recorded sizes and SHA-256 hashes.
