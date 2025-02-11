"""Tests for Problem 5.
"""

from ..projecteuler import smallest_mult


def test_1():
    """smallest_mult(5) should return a number."""
    assert isinstance(smallest_mult(5), int)


def test_2():
    """smallest_mult(5) should return 60."""
    assert smallest_mult(5) == 60


def test_3():
    """smallest_mult(7) should return 420."""
    assert smallest_mult(7) == 420


def test_4():
    """smallest_mult(10) should return 2520."""
    assert smallest_mult(10) == 2520


def test_5():
    """smallest_mult(13) should return 360360."""
    assert smallest_mult(13) == 360360

def test_6():
    """smallest_mult(20) should return 232792560."""
    assert smallest_mult(20) == 232792560
