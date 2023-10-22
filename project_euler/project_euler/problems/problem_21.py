# problem 21
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-21-amicable-numbers

from common_functions import proper_devisors

def is_amicable(n):
    """
    Returns True if a given integer is amicable
    Amicable Numbers: https://en.wikipedia.org/wiki/Amicable_numbers
    """
    proper_devisors_sum = sum(proper_devisors(n))
    pair_proper_devisors_sum = sum(proper_devisors(proper_devisors_sum))

    if pair_proper_devisors_sum == n and proper_devisors_sum != n:
        return True
    return False

def sumAmicableNum(n):
    """
    Returns the sum of all the amicable numbers under n.
    """
    amicable_pair_sum = sum([i for i in range(1, n) if is_amicable(i)])

    return amicable_pair_sum
