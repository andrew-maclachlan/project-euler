"""Tests for Problem 16.
"""

from ..projecteuler import powerDigitSum


def test_1():
    """powerDigitSum(15) should return a number."""
    assert isinstance(powerDigitSum(15), int)


def test_2():
    """powerDigitSum(15) should return 36."""
    assert powerDigitSum(15) == 26


def test_3():
    """powerDigitSum(128) should return 166."""
    assert powerDigitSum(128) == 166

def test_4():
    """powerDigitSum(1000) should return 1366."""
    assert powerDigitSum(1000) == 1366
