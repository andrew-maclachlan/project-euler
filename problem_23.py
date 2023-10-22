# Problem 23
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-23-non-abundant-sums

from common_functions import proper_devisors
from itertools import combinations

def is_abundant_number(n):
    """
    Returns True if given integer is abundant.
    Abundant Number: https://en.wikipedia.org/wiki/Abundant_number
    """
    proper_devisors_sum = sum(proper_devisors(n))

    if proper_devisors_sum > n:
        return True
    return False

def sumOfNonAbundantNumbers(n):
    """
    Return the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.
    """
    abundant_numbers = {i for i in range(1, n) if is_abundant_number(i)}
    abundant_numbers_pair_sum = {sum(i) for i in combinations(abundant_numbers, 2)}

    all_numbers_to_n = set(range(1, n+1))
    numbers_without_sum = all_numbers_to_n.difference(abundant_numbers_pair_sum)

    return sum(numbers_without_sum)
