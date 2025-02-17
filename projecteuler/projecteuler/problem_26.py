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
    # Calulate decimals
    decimals = [_unit_fraction_calculator(n, 10000) for n in range(2, limit)]

    # Extract the portion after the . as a string
    strings = [str(n).split('.')[1] for n in decimals]

    # Reverse the strings
    reverse_strings = [s[::-1] for s in strings]

    # Repeat Unit Lengths
    repeat_unit_lengths = [
        min([len(s[:i]) for i in range(1, len(s)) if s[:(i * 2)] == (s[:i] * 2)], default=0)
        for s in reverse_strings]

    # Index with max repeat unit length
    max_index = repeat_unit_lengths.index(max(repeat_unit_lengths))

    # Return + 2 as the range started at 2 
    return max_index + 2


def _unit_fraction_generator(devisor: int):
    dividend = 10
    answer_string = '0.'

    while True:
        calc = divmod(dividend, devisor)

        answer_string += str(calc[0])
        dividend = int(calc[1] * 10)

        yield answer_string


def _unit_fraction_calculator(devisor: int, n_decimals: int = 10):
    step = _unit_fraction_generator(devisor)

    all_steps = [next(step) for _ in range(n_decimals)]

    return all_steps[-1]
