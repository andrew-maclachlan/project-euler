"""Tests for Problem 32.
"""

from ..projecteuler import pandigitalProducts

def test_1():
    """pandigitalProducts(4) should return a number."""
    assert isinstance(pandigitalProducts(4), int)


def test_2():
    """pandigitalProducts(4) should return 12."""
    assert pandigitalProducts(4) == 12


def test_3():
    """pandigitalProducts(6) should return 162."""
    assert pandigitalProducts(6) == 162

def test_4():
    """pandigitalProducts(7) should return 0."""
    assert pandigitalProducts(7) == 0

def test_5():
    """pandigitalProducts(8) should return 13458."""
    assert pandigitalProducts(8) == 13458

def test_6():
    """pandigitalProducts(9) should return 45228."""
    assert pandigitalProducts(9) == 45228
