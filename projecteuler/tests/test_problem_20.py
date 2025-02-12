"""Tests for Problem 19.
"""

from ..projecteuler import sumFactorialDigits


def test_1():
    """sumFactorialDigits(10) should return a number."""
    assert isinstance(sumFactorialDigits(10), int)


def test_2():
    """sumFactorialDigits(10) should return 27."""
    assert sumFactorialDigits(10) == 27


def test_3():
    """sumFactorialDigits(25) should return 72."""
    assert sumFactorialDigits(25) == 72

def test_4():
    """sumFactorialDigits(50) should return 216."""
    assert sumFactorialDigits(50) == 216

def test_5():
    """sumFactorialDigits(75) should return 432."""
    assert sumFactorialDigits(75) == 432

def test_6():
    """sumFactorialDigits(100) should return 648."""
    assert sumFactorialDigits(100) == 648
