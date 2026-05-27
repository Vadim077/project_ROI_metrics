import unittest
from packages.core.metrics import calculate_roi, calculate_cr

class TestMetrics(unittest.TestCase):
    def test_calculate_roi_positive(self):
        self.assertEqual(calculate_roi(150, 100), 50.0)
    
    def test_calculate_roi_negative_cost_raises_error(self):
        with self.assertRaises(ValueError) as context:
            calculate_roi(100, -50)
        self.assertIn("cannot be negative", str(context.exception))

    def test_calculate_cr_zero_clicks(self):
        self.assertEqual(calculate_cr(10, 0), 0.0)

if __name__ == "__main__":
    unittest.main()
