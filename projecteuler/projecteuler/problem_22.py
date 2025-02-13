"""Problem 22: Names scores
Using names, an array defined in the background containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the array?
"""

import numpy as np
from string import ascii_uppercase

def alphabetical_value(word: str) -> int:
    """Return the alphabetical value for a given word: a=1, b=2, c=3,...,z=26

    Args:
        word (str): Word to calculate the alphabetical value of.
    
    Returns:
        int: The alphabetical value.
    """
    # A-Z uppercase in alphabetical order
    letters_list = [*ascii_uppercase]

    # Convert word to uppercase
    upper_word = word.upper()

    # Calculate value by checking the index+1 in the alphabetised list
    value = sum(letters_list.index(letter)+1 for letter in upper_word)

    return value

def namesScores(word_list: list[str]) -> int:
    """Calculate the alphabetical value of all words in a list.

    Alphabetical value is calculated by:
    - ordering the list alphabetically
    - calculating the alphabetical value for each word; a=1, b=2, c=3,...,z=26
    - multiply the alphabetical value by the alphabetical positiion to give a word value
    
    Args:
        word_list (list[str]): List of words, can be disordered.
    
    Returns:
        int: Alphabetical value
    """
    # Sort the word_list
    word_list.sort()

    # Calculate the alphabetical value for each word
    alphabetical_values = [alphabetical_value(word) for word in word_list]

    # Multiply the alphabetical value by the alphabetical positiion
    word_values = [word * i for i, word in enumerate(alphabetical_values, 1)]

    return sum(word_values)
