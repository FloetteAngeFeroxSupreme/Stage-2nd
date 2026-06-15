import unittest

# Assuming ex6.py is in the same directory as this test file.
from ex6 import calculatrice

class TestCalculatrice(unittest.TestCase):

    def test_addition_positive(self):
        self.assertEqual(calculatrice(2, 3, "+"), 5)

    def test_addition_with_zero(self):
        self.assertEqual(calculatrice(0, 3, "+"), 3)

    def test_addition_negative(self):
        self.assertEqual(calculatrice(-2, -3, "+"), -5)

    def test_addition_mixed(self):
        self.assertEqual(calculatrice(-2, 3, "+"), 1)

    def test_subtraction_positive(self):
        self.assertEqual(calculatrice(2, 3, "-"), -1)

    def test_subtraction_with_zero(self):
        self.assertEqual(calculatrice(2, 0, "-"), 2)

    def test_subtraction_negative(self):
        self.assertEqual(calculatrice(-2, -3, "-"), 1)

    def test_multiplication_positive(self):
        self.assertEqual(calculatrice(2, 3, "*"), 6)

    def test_multiplication_with_zero(self):
        self.assertEqual(calculatrice(2, 0, "*"), 0)

    def test_multiplication_negative(self):
        self.assertEqual(calculatrice(-2, 3, "*"), -6)

    def test_division_positive(self):
        self.assertEqual(calculatrice(6, 3, "/"), 2.0)

    def test_division_negative(self):
        self.assertEqual(calculatrice(-6, 3, "/"), -2.0)

    def test_division_by_zero(self):
        self.assertEqual(calculatrice(6, 0, "/"), "impossible")

    def test_invalid_operator(self):
        self.assertEqual(calculatrice(2, 3, "%"), "opérateur invalide")
        self.assertEqual(calculatrice(2, 3, "x"), "opérateur invalide")

if __name__ == '__main__':
    unittest.main()