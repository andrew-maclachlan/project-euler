"""Tests for Problem 28.
"""

from ..projecteuler import spiralDiagonals

def test_1():
    """spiralDiagonals(101) should return a number."""
    assert isinstance(spiralDiagonals(101), int)


def test_2():
    """spiralDiagonals(101) should return 692101."""
    assert spiralDiagonals(101) == 692101


def test_3():
    """spiralDiagonals(303) should return 18591725."""
    assert spiralDiagonals(303) == 18591725

def test_4():
    """spiralDiagonals(505) should return 85986601."""
    assert spiralDiagonals(505) == 85986601

def test_5():
    """spiralDiagonals(1001) should return 669171001."""
    assert spiralDiagonals(1001) == 669171001
