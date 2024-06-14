"""Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
"""

from common_functions import with_caching

@with_caching
def largest_prime_factor(number: int) -> int:
    """Return the largest prime factor of any given integer.

    Args:
        number (int)

    Returns:
        int
    """
    # Try all integers from 2 up to number until a factor is found
    for factor_check in range(2, number):
        # If a factor is found then search for the largest factor in other factor from the pair
        if number % factor_check == 0:
            return largest_prime_factor(int(number / factor_check))

    # If no factors are found then number is prime
    return number
