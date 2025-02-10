"""All completed and cleaned Project Euler problems."""

from .common_functions import all_prime_factors, is_prime

from .problem_1 import problem_1, multiples_of_3_and_5
from .problem_2 import problem_2, fibo_even_sum
from .problem_3 import problem_3, largest_prime_factor
from .problem_4 import problem_4, largest_palindrome_product
from .problem_5 import problem_5, smallest_mult
from .problem_6 import problem_6, sum_square_difference
from .problem_7 import problem_7, nth_prime
from .problem_8 import problem_8, largest_product_in_a_series
from .problem_9 import problem_9, special_pythagorean_triplet
from .problem_10 import problem_10, prime_summation
from .problem_11 import problem_11, largest_grid_product
from .problem_12 import problem_12, divisible_triangle_number
from .problem_13 import problem_13, largeSum

__all__ = [
    'all_prime_factors', 'is_prime',
    'problem_1', 'multiples_of_3_and_5', 
    'problem_2', 'fibo_even_sum',
    'problem_3', 'largest_prime_factor',
    'problem_4', 'largest_palindrome_product',
    'problem_5', 'smallest_mult',
    'problem_6', 'sum_square_difference',
    'problem_7', 'nth_prime',
    'problem_8', 'largest_product_in_a_series',
    'problem_9', 'special_pythagorean_triplet',
    'problem_10', 'prime_summation',
    'problem_11', 'largest_grid_product',
    'problem_12', 'divisible_triangle_number',
    'problem_13', 'largeSum',
]

__version__ = "0.1.0"
