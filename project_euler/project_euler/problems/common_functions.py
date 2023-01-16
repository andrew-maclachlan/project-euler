"""Sub-module of project-euler containing any functions that are used by more than one problem.
"""

from typing import List


def all_prime_factors(number: int) -> List[int]:
    """Return a list of all prime factors of a given integer.
    """
    return _all_prime_factors_recursion(number)


def _all_prime_factors_recursion(number: int, prime_list=None) -> List[int]:
    # Initialise List
    if prime_list is None:
        prime_list = []

    # Check all potential factors incrementally
    for factor_check in range(2, number + 1):
        # If the division has no remainder then factor_check is a factor.
        if number % factor_check == 0:
            # Append the factor to the list
            prime_list.append(factor_check)

            # Repeat the check with the result of the number divided by the smallest factor.
            return _all_prime_factors_recursion(int(number / factor_check), prime_list)

    # Once all numbers are exhausted then return the list of factors
    return prime_list


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int):

    Returns:
        bool
    """

    if n < 2:
        return False

    if n == 2:
        return True

    for factor_check in range(3, int(n / 2), 2):
        # If n has a factor then it's not prime
        if n % factor_check == 0:
            return False

        # If the square of the factor check is greater than n, all further potential factors would
        # have had their pair already checked, so n is prime.
        if factor_check ** 2 > n:
            return True

    return True
