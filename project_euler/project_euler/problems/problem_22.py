# Problem 22
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-22-names-scores

import numpy as np
from string import ascii_uppercase

def alphabetical_value(word):
    """
    Returns the alphabetical value for a given word: a=1, b=2, c=3,...,z=26
    """
    letters_list = [*ascii_uppercase]
    upper_word = word.upper()

    return sum([letters_list.index(letter)+1 for letter in upper_word])

def namesScores(word_list):
    """
    Given a list of strings:
    - order the list alphabetically
    - calculate the alphabetical value for each word; a=1, b=2, c=3,...,z=26
    - multiply the alphabetical value by the alphabetical positiion to give a word value
    Returns the sum of all word values.
    """
    word_list_arr = np.array(word_list)
    word_list_arr.sort()

    word_values = [alphabetical_value(word) * position for position,word in enumerate(word_list_arr, 1)]

    return sum(word_values)

test1 = ['THIS', 'IS', 'ONLY', 'A', 'TEST']
test2 = ['I', 'REPEAT', 'THIS', 'IS', 'ONLY', 'A', 'TEST']
