"""Tests for Problem 6.
"""

from ..problems import sum_square_difference


def test_1():
    """sum_square_difference(10) should return a number."""
    assert isinstance(sum_square_difference(10), int)


def test_2():
    """sum_square_difference(10) should return 2640."""
    assert sum_square_difference(10) == 2640


def test_3():
    """sum_square_difference(20) should return 41230."""
    assert sum_square_difference(20) == 41230


def test_4():
    """sum_square_difference(100) should return 25164150."""
    assert sum_square_difference(100) == 25164150
