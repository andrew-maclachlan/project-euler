"""Problem 33: Digit cancelling fractions
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from itertools import product
from fractions import Fraction

import numpy as np

def digitCancellingFractions():
    """Calculate the value of the denominator from the 4 fractions under 1 that can have common digits in the numerator and denominator and the result is the same.

    Returns:
        int: Denominator
    """
    # Valid ractions
    valid_fractions = []

    # All numerateo and denominator combinations
    num_den_combos = product(range(10, 99), range(10, 99))

    # Loop through all combinations
    for combo in num_den_combos:

        # Split out numerator and denominator
        num, den = combo

        # Shared digit between num and den
        shared_digit = list(set(str(num)).intersection(set(str(den))))
        shared_digit_str = shared_digit[0] if shared_digit else ''

        if shared_digit_str and shared_digit_str != '0' and num / den < 1:
            # Remove shared digit
            combo_altered = (
                int(str(num).replace(shared_digit_str, '', 1)),
                int(str(den).replace(shared_digit_str, '', 1))
            )
        
            # Avoid divide by zero
            if combo_altered[1] == 0:
                continue

            # Check whether the fraction is the same after removing the value
            if num / den == combo_altered[0] / combo_altered[1]:
                valid_fractions.append(combo)

    # Denominator of the product of all valid
    den_product = Fraction(np.prod([Fraction(num, den) for num, den in valid_fractions])).denominator

    return den_product
