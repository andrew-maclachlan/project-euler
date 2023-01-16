"""All completed and cleaned Project Euler problems."""

from .common_functions import allPrimeFactors

from .problem_1 import multiples_of_3_and_5
from .problem_2 import fibo_even_sum
from .problem_3 import largest_prime_factor
from .problem_4 import largest_palindrome_product
from .problem_5 import smallest_mult

__all__ = ['multiples_of_3_and_5', 'fibo_even_sum', 'largest_prime_factor',
           'largest_palindrome_product', 'smallest_mult', 'allPrimeFactors']
