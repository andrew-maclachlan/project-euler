"""Tests for Problem 23.
"""

from ..projecteuler import sumOfNonAbundantNumbers

def test_1():
    """sumOfNonAbundantNumbers(10000) should return a number."""
    assert isinstance(sumOfNonAbundantNumbers(10000), int)


def test_2():
    """sumOfNonAbundantNumbers(10000) should return 3731004."""
    assert sumOfNonAbundantNumbers(10000) == 3731004


def test_3():
    """sumOfNonAbundantNumbers(15000) should return 4039939."""
    assert sumOfNonAbundantNumbers(15000) == 4039939

def test_4():
    """sumOfNonAbundantNumbers(20000) should return 4159710."""
    assert sumOfNonAbundantNumbers(20000) == 4159710

def test_5():
    """sumOfNonAbundantNumbers(28123) should return 4179871."""
    assert sumOfNonAbundantNumbers(28123) == 4179871
