"""
2. Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Constraints:

        - 1 <= n <= 8

    Example 1:

        - Input: n = 3

        - Output: ["((()))","(()())","(())()","()(())","()()()"]

        - Example 2:

    Example 2:

        - Input: n = 1

        - Output: ["()"] 
"""

from typing import List

class ParenthesesGenerator:
    """
    A class to generate all valid combinations of n pairs of parentheses.
    """
    def __init__(self, n: int):
        self.n = n
        self.combinations: List[str] = []

    def generate(self) -> List[str]:
        """
        Generates all valid parentheses combinations using DFS.
        
        Returns:
            List[str]: A list containing all valid combinations.
        
        Time Complexity: O(4^n / sqrt(n)) - Derived using the Catalan number formula.
        """
        self._backtrack('', 0, 0)
        return self.combinations

    def _backtrack(self, current: str, open_count: int, close_count: int):
        """
        Generate parentheses using backtracking.
        
        Args:
            current (str): The current sequence of parentheses being built.
            open_count (int): Number of open brackets used.
            close_count (int): Number of close brackets used.
        """
        if len(current) == self.n * 2:
            self.combinations.append(current)
            return

        if open_count < self.n:
            self._backtrack(current + '(', open_count + 1, close_count)
        
        if close_count < open_count:
            self._backtrack(current + ')', open_count, close_count + 1)

class UserInput:
    """
    Handle user input.
    """
    @staticmethod
    def get_input() -> int:
        """
        Takes user input and validate non-negative integer.
        
        Returns:
            int: The number of bracket pairs.
        """
        while True:
            try:
                num_brackets = int(input("Enter the number of bracket pairs: "))
                if num_brackets < 0:
                    raise ValueError("Invalid input: Number of brackets cannot be negative.")
                return num_brackets
            except ValueError as e:
                print(e)

def main():
    """
    Main function 
    """
    num_brackets = UserInput.get_input()

    if num_brackets == 0:
        print([])
    else:
        generator = ParenthesesGenerator(num_brackets)
        print(generator.generate())

if __name__ == '__main__':
    main()
