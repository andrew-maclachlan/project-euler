"""Problem 26: Reciprocal cycles
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def reciprocalCycles(limit : int) -> int:
    """Get the denominator of the unit fraction with the longest recurring cycle of digits in the decimal representation.

    Args:
        limit (int): Check denominators under this limit, i.e. up to 1/limit-1
    
    Return:
        int: Denominator that returns the decimal with the longest recurring cycle.
    """
    # Repeat decimal lengths
    repeat_unit_lengths = [_unit_fraction_generator(n) for n in range(1, limit)]

    # Index with max repeat unit length
    max_index = repeat_unit_lengths.index(max(repeat_unit_lengths))

    # Return + 1 to account for 0 vs 1 indexed list
    return max_index + 1


def _unit_fraction_generator(devisor: int):
    # Dividend starts at 10 
    dividend = 10

    # Dictionary to track which remainders have been seen before, value is i where seen
    seen_remainders = {}

    i = 0
    while True:
        # Get the quotient and remainder
        _, remainder = divmod(dividend, devisor)

        # No remainder means no repeating decimals in result
        if not remainder:
            return 0

        # If the remainder has been seen before then the decimal loop is about to repeat
        if remainder in seen_remainders:
            # Return current difference between time remainder last seen and current i
            return i - seen_remainders[remainder]
        
        # If remainder not seen before then add to the dictionary and pass the remainder as the new dividend
        if remainder not in seen_remainders:
            seen_remainders[remainder] = i
            dividend = remainder * 10
            i += 1
