"""Tests for Problem 12.
"""

from ..problems import divisible_triangle_number


def test_1():
    """divisible_triangle_number(5) should return a number."""
    assert isinstance(divisible_triangle_number(5), int)


def test_2():
    """divisible_triangle_number(5) should return 28."""
    assert divisible_triangle_number(5) == 28


def test_3():
    """divisible_triangle_number(23) should return 630."""
    assert divisible_triangle_number(23) == 630


def test_4():
    """divisible_triangle_number(167) should return 1385280."""
    assert divisible_triangle_number(167) == 1385280


def test_5():
    """divisible_triangle_number(374) should return 17907120."""
    assert divisible_triangle_number(374) == 17907120


def test_6():
    """divisible_triangle_number(500) should return 76576500."""
    assert divisible_triangle_number(500) == 76576500
