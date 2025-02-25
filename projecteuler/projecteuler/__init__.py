"""All completed and cleaned Project Euler problems."""

from .common_functions import all_prime_factors, is_prime

from .problem_1 import multiples_of_3_and_5
from .problem_2 import fibo_even_sum
from .problem_3 import largest_prime_factor
from .problem_4 import largest_palindrome_product
from .problem_5 import smallest_mult
from .problem_6 import sum_square_difference
from .problem_7 import nth_prime
from .problem_8 import largest_product_in_a_series
from .problem_9 import special_pythagorean_triplet
from .problem_10 import prime_summation
from .problem_11 import largest_grid_product
from .problem_12 import divisible_triangle_number
from .problem_13 import largeSum
from .problem_14 import longestCollatzSequence
from .problem_15 import latticePaths
from .problem_16 import powerDigitSum
from .problem_17 import numberLetterCounts
from .problem_18 import maximumPathSumI
from .problem_19 import countingSundays
from .problem_20 import sumFactorialDigits
from .problem_21 import sumAmicableNum
from .problem_22 import namesScores
from .problem_23 import sumOfNonAbundantNumbers
from .problem_24 import lexicographicPermutations
from .problem_25 import digitFibonacci
from .problem_26 import reciprocalCycles
from .problem_27 import quadraticPrimes
from .problem_28 import spiralDiagonals
from .problem_29 import distinctPowers
from .problem_30 import digitnPowers
from .problem_31 import coinSums

p1 = multiples_of_3_and_5
p2 = fibo_even_sum
p3 = largest_prime_factor
p4 = largest_palindrome_product
p5 = smallest_mult
p6 = sum_square_difference
p7 = nth_prime
p8 = largest_product_in_a_series
p9 = special_pythagorean_triplet
p10 = prime_summation
p11 = largest_grid_product
p12 = divisible_triangle_number
p13 = largeSum
p14 = longestCollatzSequence
p15 = latticePaths
p16 = powerDigitSum
p17 = numberLetterCounts
p18 = maximumPathSumI
p19 = countingSundays
p20 = sumFactorialDigits
p21 = sumAmicableNum
p22 = namesScores
p23 = sumOfNonAbundantNumbers
p24 = lexicographicPermutations
p25 = digitFibonacci
p26 = reciprocalCycles
p27 = quadraticPrimes
p28 = spiralDiagonals
p29 = distinctPowers
p30 = digitnPowers
p31 = coinSums

__all__ = [
    'all_prime_factors', 'is_prime',
    'p1', 'multiples_of_3_and_5',
    'p2', 'fibo_even_sum',
    'p3', 'largest_prime_factor',
    'p4', 'largest_palindrome_product',
    'p5', 'smallest_mult',
    'p6', 'sum_square_difference',
    'p7', 'nth_prime',
    'p8', 'largest_product_in_a_series',
    'p9', 'special_pythagorean_triplet',
    'p10', 'prime_summation',
    'p11', 'largest_grid_product',
    'p12', 'divisible_triangle_number',
    'p13', 'largeSum',
    'p14', 'longestCollatzSequence',
    'p15', 'latticePaths',
    'p16', 'powerDigitSum',
    'p17', 'numberLetterCounts',
    'p18', 'maximumPathSumI',
    'p19', 'countingSundays',
    'p20', 'sumFactorialDigits',
    'p21', 'sumAmicableNum',
    'p22,', 'namesScores',
    'p23', 'sumOfNonAbundantNumbers',
    'p24', 'lexicographicPermutations'
    'p25', 'digitFibonacci',
    'p26', 'reciprocalCycles',
    'p27', 'quadraticPrimes',
    'p28', 'spiralDiagonals',
    'p29', 'distinctPowers',
    'p30', 'digitnPowers',
    'p31', 'coinSums'
]

__version__ = "0.1.0"
