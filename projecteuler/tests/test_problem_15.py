"""Tests for Problem 15.
"""

from ..projecteuler import latticePaths


def test_1():
    """latticePaths(4) should return a number."""
    assert isinstance(latticePaths(4), int)


def test_2():
    """latticePaths(4) should return 70."""
    assert latticePaths(4) == 70


def test_3():
    """latticePaths(9) should return 48620."""
    assert latticePaths(9) == 48620

def test_4():
    """latticePaths(20) should return 137846528820."""
    assert latticePaths(20) == 137846528820
