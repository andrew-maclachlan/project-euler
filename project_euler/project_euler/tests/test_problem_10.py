"""Tests for Problem 10.
"""

from ..problems import prime_summation


def test_1():
    """prime_summation(17) should return a number."""
    assert isinstance(prime_summation(17), int)


def test_2():
    """prime_summation(17) should return 41."""
    assert prime_summation(17) == 41


def test_3():
    """prime_summation(2001) should return 277050."""
    assert prime_summation(2001) == 277050


def test_4():
    """prime_summation(140759) should return 873608362."""
    assert prime_summation(140759) == 873608362


def test_5():
    """prime_summation(2000000) should return 142913828922."""
    assert prime_summation(2000000) == 142913828922
