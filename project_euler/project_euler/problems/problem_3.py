"""Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the given number?
"""


def largest_prime_factor(prime_lim: int) -> int:
    """Return the largest prime factor of any given integer.
    """
    # Try all integers from 2 up to prime_lim until a factor is found
    for factor_check in range(2, prime_lim):
        # If a factor is found then search for the largest factor in other factor from the pair
        if prime_lim % factor_check == 0:
            return largest_prime_factor(int(prime_lim / factor_check))

    # If no factors are found then prime_lim is prime
    return prime_lim
