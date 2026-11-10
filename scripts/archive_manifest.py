"""Build or verify the dated research archive's SHA-256 file manifest."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
from pathlib import Path


def build_manifest(root: Path, manifest_path: Path) -> str:
    """Return deterministic CSV content for regular files below root."""
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    if not root.is_dir():
        raise ValueError(f"archive root is not a directory: {root}")

    rows = []
    for path in sorted(root.rglob("*"), key=lambda item: item.relative_to(root).as_posix()):
        if not path.is_file() or path.is_symlink() or path.resolve() == manifest_path:
            continue
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": str(path.stat().st_size),
                "sha256": digest.hexdigest(),
            }
        )

    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=["path", "bytes", "sha256"], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def main() -> int:
    archive_root = Path(__file__).resolve().parents[1] / "research" / "2026-11-09"

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=archive_root, help="archive directory")
    parser.add_argument(
        "--manifest", type=Path, help="manifest path; defaults to ROOT/FILE-MANIFEST.csv"
    )
    parser.add_argument(
        "--check", action="store_true", help="fail if the manifest does not match the files"
    )
    args = parser.parse_args()

    output_path = args.manifest or args.root / "FILE-MANIFEST.csv"
    expected = build_manifest(args.root, output_path)
    if args.check:
        try:
            actual = output_path.read_text(encoding="utf-8")
        except OSError as error:
            print(f"FAIL: cannot read manifest: {error}")
            return 1
        if actual != expected:
            print("FAIL: archive manifest is missing, stale, or out of order")
            return 1
        print("PASS: archive file manifest matches current files and SHA-256 values")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(expected, encoding="utf-8", newline="")
    print(f"Wrote archive manifest: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
