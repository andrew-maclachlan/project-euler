"""Problem 30: Digit n powers
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of n powers of their digits.
"""

import numpy as np

def digitnPowers(n_power: int) -> int:
    """Calculate the sum of all the numbers that can be written as the sum of n powers of their digits.

    Args:
        n_power (int): Power to raise all the digits to.

    Return:
        int: Sum of all numbers that can be represented as each of their digits raised to the given power.
    """

    valid_numbers = []

    magnitude = 10
    final_sum = np.inf
    final_i = 1

    # If the end of the order of magnitude is less than the final sum then there are no more valid_numbers
    while final_sum > final_i:
        # Go up in orders of magnitude
        for i in range(1 * magnitude, 10 * magnitude):
            power_sum = sum(int(digit)**n_power for digit in str(i))

            # The the number is valid then add it to the list
            if i == power_sum:
                valid_numbers.append(i)

        # Update the final numbers of the magnitude
        final_sum = power_sum
        final_i = i

        magnitude *= 10

    return sum(valid_numbers)
