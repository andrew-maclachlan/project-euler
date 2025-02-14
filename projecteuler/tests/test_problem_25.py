"""Tests for Problem 25.
"""

from ..projecteuler import digitFibonacci

def test_1():
    """digitFibonacci(5) should return a number."""
    assert isinstance(digitFibonacci(5), int)


def test_2():
    """digitFibonacci(5)  should return 21."""
    assert  digitFibonacci(5) == 21


def test_3():
    """digitFibonacci(10) should return 45."""
    assert digitFibonacci(10) == 45

def test_4():
    """digitFibonacci(15) should return 69."""
    assert digitFibonacci(15) == 69

def test_5():
    """digitFibonacci(20) should return 93."""
    assert digitFibonacci(20) == 93
