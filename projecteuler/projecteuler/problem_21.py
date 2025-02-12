"""Problem 21: Amicable numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under n.
"""

from .common_functions import proper_devisors

def sumAmicableNum(limit: int) -> int:
    """Return the sum of all the amicable numbers under limit.

    Args:
        limit (int): Number to check the sum of all amicable numbers under.
    
    Returns:
        int: Sum of all amicable numbers under the limit.
    """
    amicable_pair_sum = sum(i for i in range(1, limit) if is_amicable(i))

    return amicable_pair_sum

def is_amicable(n: int) -> bool:
    """Check whether a given integer is amicable.

    Args:
        n (int): Integer to check if amicable.
    
    Returns:
        bool: True if amicable
    
    Notes:
        Amicable Numbers: https://en.wikipedia.org/wiki/Amicable_numbers
    """
    proper_devisors_sum = sum(proper_devisors(n))
    pair_proper_devisors_sum = sum(proper_devisors(proper_devisors_sum))

    if pair_proper_devisors_sum == n and proper_devisors_sum != n:
        return True
    return False
