import unittest
from ex5 import syracuse

class TestSyracuse(unittest.TestCase):
    def test_syracuse_three(self):
        # Sequence for 3: 10, 5, 16, 8, 4, 2, 1
        sequence, maximum = syracuse(3)
        self.assertEqual(sequence, [10, 5, 16, 8, 4, 2, 1])
        self.assertEqual(maximum, 16)

    def test_syracuse_one(self):
        # Edge case: sequence is empty, max is the number itself
        sequence, maximum = syracuse(1)
        self.assertEqual(sequence, [])
        self.assertEqual(maximum, 1)

if __name__ == "__main__":
    unittest.main()