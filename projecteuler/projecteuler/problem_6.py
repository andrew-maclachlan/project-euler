"""Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square
of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of
the sum.
"""


def sum_square_difference(n: int) -> int:
    """Return the difference between the sum of the squares of the first n natural numbers and the
    square of the sum.
    """
    # Sum the squares
    sum_squares = sum(map(lambda i: i ** 2, range(1, n + 1)))

    # Square the sums
    square_sums = sum(range(1, n + 1)) ** 2

    # Return the difference between the two
    return square_sums - sum_squares
