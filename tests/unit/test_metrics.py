import unittest
from packages.core.metrics import calculate_roi, calculate_cr, calculate_profit

class TestMetrics(unittest.TestCase):
    def test_calculate_roi_positive(self):
        self.assertAlmostEqual(calculate_roi(150, 100), 50.0, places=2)
    
    def test_calculate_roi_negative_cost_raises_error(self):
        with self.assertRaises(ValueError) as context:
            calculate_roi(100, -50)
        self.assertIn("cannot be negative", str(context.exception))

    def test_calculate_cr_zero_clicks(self):
        self.assertAlmostEqual(calculate_cr(10, 0), 0.0, places=2)

    def test_calculate_profit_standard(self):
        self.assertAlmostEqual(calculate_profit(1500, 500), 1000.0, places=2)

    def test_negative_leads_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cr(clicks=100, leads=-5)
            pass

    def test_calculate_roi_zero_cost(self):
        with self.assertRaises(ValueError):
            calculate_roi(100, 0)

    def test_negative_clicks_raises_error(self):
        with self.assertRaises(ValueError):
            calculate_cr(clicks=-10, leads=5)

if __name__ == "__main__":
    unittest.main()
