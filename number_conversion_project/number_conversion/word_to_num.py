# number_conversion/word_to_num.py

from number_conversion.conversion_base import ConversionBase

class WordToNumConverter(ConversionBase):
    """
    Converts a word representing a number to its numerical value.
    """

    def __init__(self):
        self.number = ""
        self.word_to_digit_map = {
            "zero": ("0", 4),
            "one": ("1", 3),
            "two": ("2", 3),
            "three": ("3", 5),
            "four": ("4", 4),
            "five": ("5", 4),
            "six": ("6", 3),
            "seven": ("7", 5),
            "eight": ("8", 5),
            "nine": ("9", 4),
        }

    def convert(self, string: str) -> str:
        """
        Converts a word-based number to a numeric string.

        Args:
            string (str): A string representing a number in word form.

        Returns:
            str: The numerical value as a string.

        Raises:
            TypeError: If input string is invalid.
        """
        if not string:
            return ""

        # Check each word manually without loops
        word_list = list(self.word_to_digit_map.keys())  # Convert dictionary keys to list
        
        def check_word(index=0):
            """ Recursively checks if the string starts with a word in word_list. """
            if index >= len(word_list):
                raise TypeError("Invalid input format")
            
            word = word_list[index]
            digit, length = self.word_to_digit_map[word]

            if self.custom_startswith(string, word):  # Custom function replaces startswith()
                return digit, length

            return check_word(index + 1)  # Recursively check next word

        digit, length = check_word()  # Start checking from index 0
        return self.number + digit + self.convert(string[length:])

    def custom_startswith(self, string: str, prefix: str) -> bool:
        """
        Recursively checks if 'string' starts with 'prefix' without using loops or built-in functions.

        Args:
            string (str): The main string to check.
            prefix (str): The prefix to match.

        Returns:
            bool: True if 'string' starts with 'prefix', False otherwise.
        """
        if not prefix:  # If the prefix is empty, it's always a match
            return True
        if not string or string[0] != prefix[0]:  # If main string is empty or first character mismatch
            return False
        return self.custom_startswith(string[1:], prefix[1:])  # Recursively check next characters
