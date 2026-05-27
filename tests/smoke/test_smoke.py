import subprocess
import unittest

class TestSmokeMain(unittest.TestCase):
    def test_main_runs_without_errors(self):
        result = subprocess.run(["python", "-m", "app.cli.main", "tests/fixtures/sample_data.json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Ads Metrics Report", result.stdout)

if __name__ == "__main__":
    unittest.main()