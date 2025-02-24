# number_conversion/num_to_word.py

from number_conversion.mappings import digits
from number_conversion.conversion_base import ConversionBase

class NumToWordConverter(ConversionBase):
    """
    Converts a number to its word representation.
    """

    def __init__(self):
        self.output = ""

    def convert(self, num: str) -> str:
        """
        Converts a numeric string into words.

        Args:
            num (str): A string representing a numeric value.

        Returns:
            str: A word representation of the number.
        """
        if num == '':
            return ''
        return self.output + digits[num[0]] + self.convert(num[1:])
