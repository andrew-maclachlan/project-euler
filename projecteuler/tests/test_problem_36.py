"""Tests for Project Euler Problem 37
"""

from ..projecteuler import doubleBasePalindromes

def test_1():
    """doubleBasePalindromes(1000) should return a number."""
    assert isinstance(doubleBasePalindromes(1000), int)

def test_2():
    """doubleBasePalindromes(1000) should return 1772."""
    assert doubleBasePalindromes(1000) == 1772

def test_3():
    """doubleBasePalindromes(50000) should return 105795."""
    assert doubleBasePalindromes(50000) == 105795

def test_4():
    """doubleBasePalindromes(500000) should return 286602."""
    assert doubleBasePalindromes(500000) == 286602

def test_5():
    """doubleBasePalindromes(1000000) should return 872187."""
    assert doubleBasePalindromes(1000000) == 872187
