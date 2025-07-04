"""Tests for Problem 35.
"""

from ..projecteuler import circularPrimes

def test_1():
    """circularPrimes(100) should return a number."""
    assert isinstance(circularPrimes(100), int)


def test_2():
    """circularPrimes(100) should return 13."""
    assert circularPrimes(100) == 13

def test_3():
    """circularPrimes(100000) should return 43."""
    assert circularPrimes(100000) == 43

def test_4():
    """circularPrimes(250000) should return 45."""
    assert circularPrimes(250000) == 45

def test_5():
    """circularPrimes(500000) should return 49."""
    assert circularPrimes(500000) == 49

def test_6():
    """circularPrimes(750000) should return 49."""
    assert circularPrimes(750000) == 49

def test_7():
    """circularPrimes(1000000) should return 55."""
    assert circularPrimes(1000000) == 55
