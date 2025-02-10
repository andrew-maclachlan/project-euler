"""Tests for Problem 1.
"""

from projecteuler import multiples_of_3_and_5


def test_1():
    """multiples_of_3_and_5(10) should return a number."""
    assert isinstance(multiples_of_3_and_5(10), int)


def test_2():
    """multiples_of_3_and_5(49) should return 543."""
    assert multiples_of_3_and_5(49) == 543


def test_3():
    """multiples_of_3_and_5(1000) should return 233168."""
    assert multiples_of_3_and_5(1000) == 233168


def test_4():
    """multiples_of_3_and_5(8456) should return 16687353."""
    assert multiples_of_3_and_5(8456) == 16687353


def test_5():
    """multiples_of_3_and_5(19564) should return 89301183."""
    assert multiples_of_3_and_5(19564) == 89301183
