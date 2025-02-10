"""Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
"""

from .common_functions import is_prime


def prime_summation(n: int) -> int:
    """Return the sum of all primes below n.

    Args:
        n (int):

    Returns:
        int
    """
    # Get all primes below n
    all_primes = filter(is_prime, range(n))

    # Return the sum
    return sum(all_primes)
