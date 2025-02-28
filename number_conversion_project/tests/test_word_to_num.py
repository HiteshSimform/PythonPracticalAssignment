import unittest
from number_conversion.word_to_num import WordToNumConverter

class TestWordToNumConverter(unittest.TestCase):

    def setUp(self):
        self.converter = WordToNumConverter()

    def test_single_digit(self):
        self.assertEqual(self.converter.convert("zero"), "0")
        self.assertEqual(self.converter.convert("one"), "1")
        self.assertEqual(self.converter.convert("nine"), "9")

    def test_multiple_digits(self):
        self.assertEqual(self.converter.convert("onezero"), "10")
        self.assertEqual(self.converter.convert("twotwo"), "22")
        self.assertEqual(self.converter.convert("fivefour"), "54")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            self.converter.convert("invalidword")

if __name__ == '__main__':
    unittest.main()
