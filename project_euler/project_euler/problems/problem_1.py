"""Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The
sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value number.
"""


def multiples_of_3_and_5(int_limit: int) -> int:
    """Sum the multiples of 3 or 5 below int_limit.

    Args:
        int_limit (int):

    Returns:
        int:
    """
    # Create lists of the multiples of 3 and 5 up to the provided integer and convert to sets
    multiples_of_3 = {*range(3, int_limit, 3)}
    multiples_of_5 = {*range(5, int_limit, 5)}

    # Sum the unique values in both lists
    return sum(multiples_of_3.union(multiples_of_5))
