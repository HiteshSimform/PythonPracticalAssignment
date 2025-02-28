from typing import List
def findAnagram(numberOfWords: int, anagramWords: List[str]):
    '''
    findAnagram() function finds all the anagram functions from the List and
    prints them by grouping anagram words together.
    '''
    words = {}
    result = []
    for word in anagramWords:
        key = ''.join(sorted(word))

        if key in words.keys():
            words[key].append(word)
        else:
            words[key] = []
            words[key].append(word)
        
    for vals in words.values():
        result.append(vals)
    print(result)


def main():
    '''
    main() function takes number of words to be entered as input by user.
    Further it takes List of words as input and also checks for validity of count of words enter by user.
    '''
    numberOfWords: int = int(input("Number of words: "))
    anagramWords: List[str] = []
    if numberOfWords == 0:
        print(anagramWords)
    elif numberOfWords < 0:
        raise ValueError('Invalid input')
    else:
        for i in range(numberOfWords):
            anagramWords.append(input())
        findAnagram(numberOfWords, anagramWords)


if __name__ == '__main__':
    main()