"""Tests for Problem 29.
"""

from ..projecteuler import distinctPowers

def test_1():
    """distinctPowers(15) should return a number."""
    assert isinstance(distinctPowers(15), int)


def test_2():
    """distinctPowers(15) should return 177."""
    assert distinctPowers(15) == 177


def test_3():
    """distinctPowers(20) should return 324."""
    assert distinctPowers(20) == 324

def test_4():
    """distinctPowers(25) should return 519."""
    assert distinctPowers(25) == 519

def test_5():
    """distinctPowers(30) should return 755."""
    assert distinctPowers(30) == 755
