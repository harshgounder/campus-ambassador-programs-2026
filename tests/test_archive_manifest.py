import csv
import hashlib
import tempfile
import unittest
from pathlib import Path

from scripts.archive_manifest import build_manifest


class ArchiveManifestTests(unittest.TestCase):
    def test_uses_sorted_relative_paths_and_excludes_the_manifest(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "z.txt").write_text("last", encoding="utf-8")
            nested = root / "outputs"
            nested.mkdir()
            (nested / "a.txt").write_text("first", encoding="utf-8")
            manifest = root / "FILE-MANIFEST.csv"
            manifest.write_text("old content", encoding="utf-8")

            content = build_manifest(root, manifest)

        rows = list(csv.DictReader(content.splitlines()))
        self.assertEqual([row["path"] for row in rows], ["outputs/a.txt", "z.txt"])

    def test_records_byte_size_and_sha256(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            file_path = root / "evidence.txt"
            file_path.write_bytes(b"evidence")

            content = build_manifest(root, root / "FILE-MANIFEST.csv")

        row = next(csv.DictReader(content.splitlines()))
        self.assertEqual(row["bytes"], "8")
        self.assertEqual(row["sha256"], hashlib.sha256(b"evidence").hexdigest())

    def test_rejects_missing_archive_root(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing"

            with self.assertRaisesRegex(ValueError, "archive root is not a directory"):
                build_manifest(missing, missing / "FILE-MANIFEST.csv")
