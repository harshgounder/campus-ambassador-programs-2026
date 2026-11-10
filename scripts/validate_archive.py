"""Check CSV structure throughout the repository without network access."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

SKIP_DIRECTORIES = {".git", ".venv", ".ruff_cache", "node_modules", "build", "dist", "target"}


def validate_csv(path: Path, relative_to: Path | None = None) -> tuple[int, list[str]]:
    """Return the number of nonblank data rows and structural issues for one CSV."""
    label = path.relative_to(relative_to) if relative_to else path.name
    issues: list[str] = []
    row_count = 0

    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle, strict=True)
            try:
                header = next(reader)
            except StopIteration:
                return 0, [f"{label}: file has no header row"]

            if not header:
                return 0, [f"{label}: header row is empty"]

            seen: set[str] = set()
            for column_number, value in enumerate(header, start=1):
                name = value.strip()
                if not name:
                    issues.append(f"{label}: empty header name at column {column_number}")
                elif name in seen:
                    issues.append(f"{label}: duplicate header name {name!r}")
                seen.add(name)

            expected_columns = len(header)
            for line_number, row in enumerate(reader, start=2):
                if not row:
                    continue
                row_count += 1
                if len(row) != expected_columns:
                    issues.append(
                        f"{label}: row {line_number} has {len(row)} columns; "
                        f"expected {expected_columns}"
                    )
    except (OSError, UnicodeError, csv.Error) as error:
        issues.append(f"{label}: could not parse CSV: {error}")

    return row_count, issues


def validate_tree(root: Path) -> tuple[int, int, list[str]]:
    """Scan CSV files below root, excluding version-control and build directories."""
    root = root.resolve()
    if not root.is_dir():
        return 0, 0, [f"{root}: scan root is not a directory"]

    files = sorted(
        path
        for path in root.rglob("*.csv")
        if path.is_file()
        and not path.is_symlink()
        and not (SKIP_DIRECTORIES & set(path.relative_to(root).parts))
    )
    if not files:
        return 0, 0, [f"{root}: no CSV files found"]

    row_count = 0
    issues: list[str] = []
    for path in files:
        file_rows, file_issues = validate_csv(path, relative_to=root)
        row_count += file_rows
        issues.extend(file_issues)
    return len(files), row_count, issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root to scan (defaults to the root containing this script)",
    )
    args = parser.parse_args()

    file_count, row_count, issues = validate_tree(args.root)
    if issues:
        print(f"Found {len(issues)} CSV structure issue(s) across {file_count} files.")
        for issue in issues:
            print(f"FAIL {issue}")
        return 1

    print(f"PASS: {file_count} CSV files, {row_count} nonblank data rows, 0 structure issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
