import tempfile
import unittest
from pathlib import Path

from scripts.validate_archive import validate_tree


class TreeScanTests(unittest.TestCase):
    def test_scans_nested_files_and_reports_issues_in_sorted_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "z.csv").write_text("id\n1,extra\n", encoding="utf-8")
            nested = root / "nested"
            nested.mkdir()
            (nested / "a.csv").write_text("id\n1,extra\n", encoding="utf-8")

            file_count, row_count, issues = validate_tree(root)

        self.assertEqual(file_count, 2)
        self.assertEqual(row_count, 2)
        self.assertTrue(issues[0].startswith("nested/a.csv:"))
        self.assertTrue(issues[1].startswith("z.csv:"))

    def test_ignores_build_and_environment_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "good.csv").write_text("id\n1\n", encoding="utf-8")
            for name in (".git", ".venv", ".ruff_cache", "node_modules", "build", "dist", "target"):
                skipped = root / name
                skipped.mkdir()
                (skipped / "ignored.csv").write_text("id\n1\n", encoding="utf-8")

            file_count, row_count, issues = validate_tree(root)

        self.assertEqual((file_count, row_count, issues), (1, 1, []))

    def test_reports_when_scan_root_is_not_a_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "file.csv"
            path.write_text("id\n1\n", encoding="utf-8")

            result = validate_tree(path)

        self.assertEqual(result[:2], (0, 0))
        self.assertIn("scan root is not a directory", result[2][0])

    def test_does_not_follow_symbolic_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.csv"
            target.write_text("id\n1\n", encoding="utf-8")
            root.joinpath("linked.csv").symlink_to(target)

            file_count, row_count, issues = validate_tree(root)

        self.assertEqual((file_count, row_count, issues), (1, 1, []))
