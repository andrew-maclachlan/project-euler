"""Tests for Problem 19.
"""

from ..projecteuler import countingSundays


def test_1():
    """countingSundays(1943, 1946) should return a number."""
    assert isinstance(countingSundays(1943, 1946), int)


def test_2():
    """countingSundays(1943, 1946) should return 6."""
    assert countingSundays(1943, 1946) == 6


def test_3():
    """countingSundays(1995, 2000) should return 10."""
    assert countingSundays(1995, 2000) == 10

def test_3():
    """countingSundays(1901, 2000) should return 171."""
    assert countingSundays(1901, 2000) == 171
