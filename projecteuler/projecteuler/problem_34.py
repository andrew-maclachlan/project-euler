"""Problem 34: Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Personal Note: This is slightly unusual as no limit is provided. I suspect there is a proof that only 2 solutions exist.
    I have added a limit of 100,000.
"""

from math import factorial

def digitFactorial() -> dict:
    """Calculate the numbers and sum of the numbers that are equal to the sum of the factorial of their digits.

    Returns:
        dict:
    """
    output = []

    for test_num in range(3, 100000):
        test_sum = sum(factorial(int(digit)) for digit in str(test_num))
        if test_num == test_sum:
            output.append(test_num)

    return {
        'sum': sum(output),
        'numbers': output
    }
