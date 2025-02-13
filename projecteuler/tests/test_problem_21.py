"""Tests for Problem 21.
"""

from ..projecteuler import sumAmicableNum


def test_1():
    """sumAmicableNum(1000) should return a number."""
    assert isinstance(sumAmicableNum(1000), int)


def test_2():
    """sumAmicableNum(1000) should return 504."""
    assert sumAmicableNum(1000) == 504


def test_3():
    """sumAmicableNum(2000) should return 2898."""
    assert sumAmicableNum(2000) == 2898

def test_4():
    """sumAmicableNum(5000) should return 8442."""
    assert sumAmicableNum(5000) == 8442

def test_5():
    """sumAmicableNum(10000) should return 31626."""
    assert sumAmicableNum(10000) == 31626
