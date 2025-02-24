# number_conversion/gcd.py

class GCDComputer:
    """
    Computes the Greatest Common Divisor (GCD) using recursion.
    """

    @staticmethod
    def compute(number1: int, number2: int) -> int:
        """
        Computes the GCD of two numbers using recursion.

        Args:
            number1 (int): The first integer.
            number2 (int): The second integer.

        Returns:
            int: The GCD of the input integers.
        """
        if number2 == 0:
            return number1
        else:
            return GCDComputer.compute(number2, number1 % number2)
