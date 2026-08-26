from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from risk_engine import risk_band


class TestRiskBand(unittest.TestCase):

    def test_critical(self):
        self.assertEqual(risk_band(95), "CRITICAL")

    def test_high(self):
        self.assertEqual(risk_band(84), "HIGH")

    def test_medium(self):
        self.assertEqual(risk_band(66), "MEDIUM")

    def test_low(self):
        self.assertEqual(risk_band(30), "LOW")

    def test_informational(self):
        self.assertEqual(risk_band(10), "INFORMATIONAL")


if __name__ == "__main__":
    unittest.main()
