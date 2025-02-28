import unittest
from number_conversion.gcd import GCDComputer

class TestGCDComputer(unittest.TestCase):

    def test_gcd_basic(self):
        self.assertEqual(GCDComputer.compute(10, 5), 5)
        self.assertEqual(GCDComputer.compute(48, 18), 6)
        self.assertEqual(GCDComputer.compute(101, 103), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(GCDComputer.compute(0, 5), 5)
        self.assertEqual(GCDComputer.compute(7, 0), 7)

    def test_gcd_same_numbers(self):
        self.assertEqual(GCDComputer.compute(12, 12), 12)

    def test_gcd_large_numbers(self):
        self.assertEqual(GCDComputer.compute(123456, 789012), 12)

if __name__ == '__main__':
    unittest.main()
