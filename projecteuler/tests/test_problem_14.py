"""Tests for Problem 14.
"""

from ..projecteuler import longestCollatzSequence


def test_1():
    """longestCollatzSequence(14) should return a number."""
    assert isinstance(longestCollatzSequence(14), int)


def test_2():
    """longestCollatzSequence(14) should return 9."""
    assert longestCollatzSequence(15) == 9


def test_3():
    """longestCollatzSequence(5847) should return 3711."""
    assert longestCollatzSequence(5847) == 3711

def test_4():
    """longestCollatzSequence(46500) should return 35655."""
    assert longestCollatzSequence(46500) == 35655

def test_5():
    """longestCollatzSequence(54512) should return 52527."""
    assert longestCollatzSequence(54512) == 52527

def test_6():
    """longestCollatzSequence(100000) should return 77031."""
    assert longestCollatzSequence(100000) == 77031

def test_7():
    """longestCollatzSequence(1000000) should return 837799."""
    assert longestCollatzSequence(1000000) == 837799
