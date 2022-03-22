# Problem 20
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-20-factorial-digit-sum

from math import factorial

def sumFactorialDigits(n):
    """
    Returns the sum of the digits of n!
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    """

    n_factorial = factorial(n)
    n_factorial_sum = sum([int(i) for i in str(n_factorial)])

    return n_factorial_sum
