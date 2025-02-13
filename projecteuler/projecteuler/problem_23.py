"""Problem 23: Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.
"""
from itertools import combinations_with_replacement

from .common_functions import proper_devisors


def sumOfNonAbundantNumbers(limit: int) -> int:
    """Return the sum of all positive integers <= limit which cannot be written as the sum of two abundant numbers.

    Args:
        limit (int): Limit to check the sum below
    
    Returns:
        int: Sum of all positive integers that cannot be written as the sum of two abundant numbers
    """
    # All abundant numbers under the limit
    abundant_numbers = {i for i in range(1, limit) if is_abundant_number(i)}

    # Calculate the sum of all pairs of abundant numbers
    abundant_numbers_pair_sum = {sum(i) for i in combinations_with_replacement(abundant_numbers, 2)}

    # Get the numbers under the limit not in the sum of pairs
    numbers_without_sum = set(range(1, limit+1)).difference(abundant_numbers_pair_sum)

    return sum(numbers_without_sum)


def is_abundant_number(n: int) -> bool:
    """Check if the integer is abundant.
    
    Args:
        n (int): Integer to check for abundance.
    
    Returns:
        bool: True if number is abundant
    
    Notes:
        Abundant Number: https://en.wikipedia.org/wiki/Abundant_number
    """
    # Calculate the sum of all proper divisors
    proper_devisors_sum = sum(proper_devisors(n))

    # Check if the divisor sum is greater the number
    if proper_devisors_sum > n:
        return True
    return False
