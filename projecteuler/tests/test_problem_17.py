"""Tests for Problem 17.
"""

from ..projecteuler import numberLetterCounts


def test_1():
    """numberLetterCounts(5) should return a number."""
    assert isinstance(numberLetterCounts(5), int)


def test_2():
    """numberLetterCounts(5) should return 19."""
    assert numberLetterCounts(5) == 19


def test_3():
    """numberLetterCounts(150) should return 1903."""
    assert numberLetterCounts(150) == 1903

def test_4():
    """numberLetterCounts(1000) should return 21124."""
    assert numberLetterCounts(1000) == 21124
