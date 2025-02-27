"""Tests for Problem 33.
"""

from ..projecteuler import digitCancellingFractions

def test_1():
    """digitCancellingFractions() should return a number."""
    assert isinstance(digitCancellingFractions(), int)


def test_2():
    """digitCancellingFractions() should return 100."""
    assert digitCancellingFractions() == 100
