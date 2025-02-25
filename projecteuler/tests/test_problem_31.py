"""Tests for Problem 29.
"""

from ..projecteuler import coinSums

def test_1():
    """coinSums(50) should return a number."""
    assert isinstance(coinSums(50), int)


def test_2():
    """coinSums(50) should return 451."""
    assert coinSums(50) == 451


def test_3():
    """coinSums(100) should return 4563."""
    assert coinSums(100) == 4563

def test_4():
    """coinSums(150) should return 21873."""
    assert coinSums(150) == 21873

def test_5():
    """coinSums(200) should return 73682."""
    assert coinSums(200) == 73682
