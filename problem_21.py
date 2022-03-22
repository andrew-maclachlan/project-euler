# problem 21
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-21-amicable-numbers

def proper_devisors(n):
    """
    Returns the set of all proper divisors of an integer n
    Proper Divisors: https://en.wikipedia.org/wiki/Divisor#proper_divisor
    """
    return {i for i in range(1, n) if n % i == 0}

def is_amicable(n):
    """
    Returns True if a given integer is amicable
    Amicable Numbers: https://en.wikipedia.org/wiki/Amicable_numbers
    """
    proper_devisors_sum = sum(proper_devisors(n))
    pair_proper_devisors_sum = sum(proper_devisors(proper_devisors_sum))

    if pair_proper_devisors_sum == n and proper_devisors_sum != n:
        return True
    return False

def sumAmicableNum(n):
    """
    Returns the sum of all the amicable numbers under n.
    """
    amicable_pair_sum = sum([i for i in range(1, n) if is_amicable(i)])

    return amicable_pair_sum
