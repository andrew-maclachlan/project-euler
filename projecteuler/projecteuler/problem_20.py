"""Problem 20: Factorial digit sum
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits n!
"""

from math import factorial

def sumFactorialDigits(n: int) -> int:
    """Return the sum of the digits of n!

    Args:
        n (int): Number to get the sum of the factorial

    Returns:
        int: Sum of the digits of n!
    """
    
    # Calculate the factorial
    n_factorial = factorial(n)

    # Sum each of the digits individually
    n_factorial_sum = sum(int(i) for i in str(n_factorial))

    return n_factorial_sum
