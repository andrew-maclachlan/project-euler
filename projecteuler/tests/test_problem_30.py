"""Tests for Problem 29.
"""

from ..projecteuler import digitnPowers

def test_1():
    """digitnPowers(2) should return a number."""
    assert isinstance(digitnPowers(2), int)


def test_2():
    """digitnPowers(2) should return 0."""
    assert digitnPowers(2) == 0


def test_3():
    """digitnPowers(3) should return 1301."""
    assert digitnPowers(3) == 1301

def test_4():
    """digitnPowers(4) should return 19316."""
    assert digitnPowers(4) == 19316

def test_5():
    """digitnPowers(5) should return 443839."""
    assert digitnPowers(5) == 443839
