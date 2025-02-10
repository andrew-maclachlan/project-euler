"""Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number?
"""

from .common_functions import is_prime


def nth_prime(n: int) -> int:
    """Return the nth prime.

    Args:
        n (int):

    Returns:
        int
    """
    prime_counter = 1
    prime_to_check = 3

    while prime_counter < n:
        if is_prime(prime_to_check):
            prime_counter += 1
            largest_prime = prime_to_check
        prime_to_check += 2

    return largest_prime
