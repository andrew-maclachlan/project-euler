"""Tests for Problem 34.
"""

from ..projecteuler import digitFactorial

def test_1():
    """digitFactorial() should return a dict."""
    assert isinstance(digitFactorial(), dict)


def test_2():
    """digitFactorial() should return {sum: 40730, numbers: [145, 40585]}."""
    assert digitFactorial()['sum'] == 40730
    assert digitFactorial()['numbers'][0] == 145
    assert digitFactorial()['numbers'][1] == 40585
