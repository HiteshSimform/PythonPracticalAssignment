from number_conversion.conversion_base import ConversionBase
from number_conversion.mappings import word_to_digit_map

class WordToNumConverter(ConversionBase):
    """
    A class to convert numbers written in words into their numeric form.
    
    Example:
        "twenty one" -> 21
        "three hundred" -> 300
    """
    
    def __init__(self):
        # Dictionary mapping word-based numbers to their numeric string equivalents
        self.word_to_digit_map = word_to_digit_map
    
    def convert(self, word: str) -> int:
        """
        Converts a word-based number into an integer.
        
        Args:
            word (str): A number written in words (e.g., "forty two").
        
        Returns:
            int: The numerical equivalent of the word-based number.
                 Returns -1 if the input contains unrecognized words.
        
        Example:
            convert("one hundred twenty three") -> 123
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
            
            # Base case: If no more characters remain, return the accumulated result
            if not remaining:
                return num, part
            
            # Append the next character to the current segment being processed
            part += remaining[0]
            
            # If the current segment matches a known number word, map it to a digit
            if part in self.word_to_digit_map:
                num += self.word_to_digit_map[part]  # Append the corresponding digit
                part = ''  # Reset the current segment for the next word
            
            # Continue processing the rest of the input
            return word_to_digit(part, remaining[1:], num)
        
        # Start the recursive conversion process
        num, part_left = word_to_digit('', word, '')
        
        # Return the converted integer if the entire word was processed successfully
        return int(num) if not part_left else -1
