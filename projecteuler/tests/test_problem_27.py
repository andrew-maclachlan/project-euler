"""Tests for Problem 27.
"""

from ..projecteuler import quadraticPrimes

def test_1():
    """quadraticPrimes(200) should return a number."""
    assert isinstance(quadraticPrimes(200), int)


def test_2():
    """rquadraticPrimes(200) should return -4925."""
    assert quadraticPrimes(200) == -4925


def test_3():
    """quadraticPrimes(500) should return -18901."""
    assert quadraticPrimes(500) == -18901

def test_4():
    """quadraticPrimes(800) should return -43835."""
    assert quadraticPrimes(800) == -43835

def test_5():
    """quadraticPrimes(1000) should return -59231."""
    assert quadraticPrimes(1000) == -59231
