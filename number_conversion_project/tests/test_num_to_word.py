# tests/test_num_to_word.py

import unittest
from number_conversion.num_to_word import NumToWordConverter

class TestNumToWordConverter(unittest.TestCase):

    def setUp(self):
        self.converter = NumToWordConverter()

    def test_single_digit(self):
        self.assertEqual(self.converter.convert("0"), "zero")
        self.assertEqual(self.converter.convert("1"), "one")
        self.assertEqual(self.converter.convert("9"), "nine")

    def test_multiple_digits(self):
        self.assertEqual(self.converter.convert("10"), "zeroone")
        self.assertEqual(self.converter.convert("22"), "twotwo")
        self.assertEqual(self.converter.convert("54"), "fivefour")

    def test_empty_string(self):
        self.assertEqual(self.converter.convert(""), "")

if __name__ == '__main__':
    unittest.main()
