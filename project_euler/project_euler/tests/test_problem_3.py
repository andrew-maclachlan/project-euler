"""Tests for Problem 3.
"""

from ..problems import largest_prime_factor


def test_1():
    """largest_prime_factor(2) should return a number."""
    assert isinstance(largest_prime_factor(2), int)


def test_2():
    """largest_prime_factor(2) should return 2."""
    assert largest_prime_factor(2) == 2


def test_3():
    """largest_prime_factor(3) should return 3."""
    assert largest_prime_factor(3) == 3


def test_4():
    """largest_prime_factor(5) should return 5."""
    assert largest_prime_factor(5) == 5


def test_5():
    """largest_prime_factor(7) should return 7."""
    assert largest_prime_factor(7) == 7


def test_6():
    """largest_prime_factor(8) should return 2."""
    assert largest_prime_factor(8) == 2


def test_7():
    """largest_prime_factor(13195) should return 29."""
    assert largest_prime_factor(13195) == 29


def test_8():
    """largest_prime_factor(600851475143) should return 6857."""
    assert largest_prime_factor(600851475143) == 6857
