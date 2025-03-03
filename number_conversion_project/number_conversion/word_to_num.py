from number_conversion.conversion_base import ConversionBase
from number_conversion.mappings import word_to_digit_map

class WordToNumConverter(ConversionBase):
    """
    A class to convert numbers written in words into their numeric form.
    """
    
    def __init__(self):
        self.word_to_digit_map = word_to_digit_map
    
    def convert(self, word: str) -> int:
        """
        Converts a word-based number into an integer.
        
        Args:
            word (str): A number written in words
        
        Returns:
            int: The numerical equivalent of the word-based number.
                 Returns -1 if the input contains unrecognized words.
        """
        
        def word_to_digit(part: str, remaining: str, num: str) -> tuple:
            """
            A recursive function to process the input word and map it to its numeric value.
            
            Args:
                part (str): A substring currently being processed.
                remaining (str): The rest of the input word.
                num (str): Accumulated numeric representation.
            
            Returns:
                tuple: (numeric string, leftover unmatched characters)
            """

            if not remaining:
                return num, part
            
            part += remaining[0]

            if part in self.word_to_digit_map:
                num += self.word_to_digit_map[part] 
                part = ''
            return word_to_digit(part, remaining[1:], num)
        num, lft = word_to_digit('', word, '')
        return int(num) if not lft else -1
