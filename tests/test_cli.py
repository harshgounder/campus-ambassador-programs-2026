import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_archive.py"


class ValidatorCliTests(unittest.TestCase):
    def test_returns_success_for_valid_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "valid.csv").write_text("id\n1\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0)
        self.assertIn("PASS: 1 CSV files, 1 nonblank data rows", result.stdout)

    def test_returns_failure_for_invalid_tree(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "invalid.csv").write_text("name,region\nAda\n", encoding="utf-8")

            result = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Found 1 CSV structure issue", result.stdout)
