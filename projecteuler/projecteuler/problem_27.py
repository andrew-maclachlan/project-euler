"""Problem 27: Quadratic primes
Euler discovered the remarkable quadratic formula: n2 + n + 41
 
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n=40, 40**2 + 40 + 41 = 40(40+1)+41 is divisible by 41,
and certainly when n=41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula n2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:
n2 + an + b
where |a| < range and |b| ≤ range
 
Find the product of the coefficients a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from itertools import combinations

from .common_functions import is_prime

def quadraticPrimes(limit: int) -> int:
    """Get the product of the coefficients a and b from the quadratic equation that produces the maximum number of primes for consecutive values of n,
    starting with n=0, where |a| < limit and |b| ≤ limit.

    Args:
        limit (int): Limit of the range of a, b to check, such that |a| < limit and |b| ≤ limit.
    
    Returns:
        int: Product of the best a, b
    """
    # |a| < range
    all_a = range(1-limit, limit)

    # |b| ≤ range
    all_b = range(-limit, limit+1)

    # Generate all combinations of 'a's and 'b's
    all_combinations = combinations([*all_a, *all_b], 2)

    # Store the consequitive primes as keys with (a, b) as the values
    results = {_consecutive_primes(c[0], c[1]): c for c in all_combinations}

    # Get a, b for the maximum consecutive primes
    best_a, best_b = results[max(results.keys())]
    
    return best_a * best_b 

def _consecutive_primes(a: int, b: int) -> int:
    # Start at n = 0
    n = 0

    # Incrementally check each n until a non-prime is returned
    while prime_check := is_prime(n**2 + a*n + b):
        n += 1
    
    return n