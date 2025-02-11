"""Tests for Problem 7.
"""

from ..projecteuler import nth_prime


def test_1():
    """nth_prime(6) should return a number."""
    assert isinstance(nth_prime(6), int)


def test_2():
    """nth_prime(6) should return 13."""
    assert nth_prime(6) == 13


def test_3():
    """nth_prime(10) should return 29."""
    assert nth_prime(10) == 29


def test_4():
    """nth_prime(100) should return 541."""
    assert nth_prime(100) == 541


def test_5():
    """nth_prime(1000) should return 7919."""
    assert nth_prime(1000) == 7919


def test_6():
    """nth_prime(10001) should return 104743."""
    assert nth_prime(10001) == 104743
