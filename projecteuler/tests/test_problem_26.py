"""Tests for Problem 26.
"""

from ..projecteuler import reciprocalCycles

def test_1():
    """reciprocalCycles(700) should return a number."""
    assert isinstance(reciprocalCycles(700), int)


def test_2():
    """reciprocalCycles(700) should return 659."""
    assert  reciprocalCycles(700) == 659


def test_3():
    """reciprocalCycles(800) should return 743."""
    assert reciprocalCycles(800) == 743

def test_4():
    """reciprocalCycles(900) should return 887."""
    assert reciprocalCycles(900) == 887

def test_5():
    """reciprocalCycles(1000) should return 983."""
    assert reciprocalCycles(1000) == 983
