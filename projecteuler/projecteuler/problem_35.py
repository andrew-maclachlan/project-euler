"""Problem 35: Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below n, whereas 100 ≤ n ≤ 1000000?
"""

from .common_functions import is_prime

def circularPrimes(n: int) -> int:
    """Return the count of circular primes below n.
    
    Args:
        n (int):
    
    Returns:
        int
    """
    circular_prime_cnt = 0

    for i in range(n):
        if is_prime(i):
            i_str_len = len(str(i))
            if all(is_prime(int(str(i)[-j:] + str(i)[:i_str_len - j])) for j in range(1, i_str_len + 1)):
                circular_prime_cnt += 1

    return circular_prime_cnt
