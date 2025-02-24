# main.py

from number_conversion.word_to_num import WordToNumConverter
from number_conversion.num_to_word import NumToWordConverter
from number_conversion.gcd import GCDComputer

def main():
    try:
        # Create converter objects
        word_to_num_converter = WordToNumConverter()
        num_to_word_converter = NumToWordConverter()

        # Prompt user for input
        inputstr1 = input("Please enter input 1: ").lower()
        inputnum1 = int(word_to_num_converter.convert(inputstr1))

        inputstr2 = input("Please enter input 2: ").lower()
        inputnum2 = int(word_to_num_converter.convert(inputstr2))

        # Compute GCD
        gcd_num = str(GCDComputer.compute(inputnum1, inputnum2))

        # Display result
        print(f"GCD of {inputstr1} and {inputstr2} is {num_to_word_converter.convert(gcd_num)}")

    except TypeError:
        print("Please Enter a valid Word.")
    except ValueError:
        print("Invalid numeric value entered.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
