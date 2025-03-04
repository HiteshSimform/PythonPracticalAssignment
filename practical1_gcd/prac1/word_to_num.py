from prac1.conversion_base import ConversionBase
from prac1.mappings import word_to_digit_map

class WordToNumConverter(ConversionBase):
    """
    Convert a number written in words into its integer representation.
    """

    def __init__(self):
        """
        Initializes the WordToNumConverter with a mapping of words to digits.
        """
        self.word_to_digit_map = word_to_digit_map

    def convert(self, word: str) -> int:
        """
        Converts Number in words to Integer

        Args:
            word (str): Number in word form

        Returns:
            int: Return the number which is in string input
        Raises:
            ValueError: If invalid inputs or empty input
        """

        is_empty = True
        for char in word:
            if char != ' ':
                is_empty = False
                break
        if is_empty:
            raise ValueError("Error: Input cannot be empty")

        def word_to_digit(part, remaining, num):
            """
            Converts word-based numbers into numeric string (Recursion)

            Args:
                part (str): Substring for word to digit convert
                remaining (str): The remaining input string to process.
                num (str): The accumulated numeric string.

            Returns:
                tuple: The converted numeric string and any leftover invalid part.
            """
            if not remaining:
                return num, part

            part += remaining[0]
            exists = False
            for key in self.word_to_digit_map:
                if key == part:
                    exists = True
                    break

            if exists:
                num += self.word_to_digit_map[part]
                part = ''
                
            return word_to_digit(part, remaining[1:], num)

        num_str, lft = word_to_digit('', word, '')

        if lft:
            raise ValueError(f"Error: Invalid word found: '{lft}'.")

        result = 0
        for digit in num_str:
            digit_value = -1 
            for i in range(10):
                if digit == str(i):
                    digit_value = i
                    break
            if digit_value == -1:
                raise ValueError(f"Error: Unexpected character '{digit}' in number.")
            result = result * 10 + digit_value

        return result
