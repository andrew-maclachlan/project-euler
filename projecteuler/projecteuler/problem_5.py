"""Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?
"""

from collections import Counter
from numpy import prod

from .common_functions import all_prime_factors


def smallest_mult(n: int) -> int:
    """Return the smallest positive integer that is evenly divisible by all the numbers from 1 to n.

    Args:
        n (int):

    Returns:
        int
    """
    # Count the factors of all numbers up to and including max_int
    prime_factors_count = [Counter([str(factor) for factor in all_prime_factors(integer)])
                           for integer in range(1, n + 1)]

    # Take the maximum count of each factor using Counter union
    max_prime_factors_count = Counter()
    for counter in prime_factors_count:
        max_prime_factors_count |= counter

    # Take the product of all key value pairs in the counter
    result = prod([int(i) ** max_prime_factors_count[i] for i in max_prime_factors_count])

    return int(result)
