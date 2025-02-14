"""Problem 24: Lexicographic permutations
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210
What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations 


def lexicographicPermutations(n: int) -> int:
    """Get the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9

    Args:
        n (int): Term in the list to return

    Returns:
        int: nth permutation
    """
    # All digits as a string
    all_digits = ''.join(str(i) for i in range(0, 10))

    # All Permutations
    all_permutations = [''.join(i) for i in permutations(all_digits)]

    # Order the list
    all_permutations.sort()

    return int(all_permutations[n])
