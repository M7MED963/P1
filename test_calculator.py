import unittest
import math
from src.calculator import evaluate_expression

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(evaluate_expression("2+3"), "5")

    def test_power(self):
        self.assertEqual(evaluate_expression("2^3"), "8")

    def test_square_root(self):
        self.assertEqual(evaluate_expression("√(9)"), "3.0")

    def test_log(self):
        self.assertAlmostEqual(float(evaluate_expression("log(1000)")), 3.0, places=2)

    def test_ln(self):
        self.assertAlmostEqual(float(evaluate_expression("ln(e)")), 1.0, places=2)

    def test_exponential(self):
        self.assertAlmostEqual(float(evaluate_expression("e^(2)")), math.exp(2), places=2)

if __name__ == "__main__":
    unittest.main()
