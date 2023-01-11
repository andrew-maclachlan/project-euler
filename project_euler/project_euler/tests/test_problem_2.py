"""Tests for Problem 1.
"""

from ..problems import fibo_even_sum


def test_1():
    """fibo_even_sum(10) should return a number."""
    assert isinstance(fibo_even_sum(10), int)


def test_2():
    """Your function should return an even value"""
    assert fibo_even_sum(10) % 2 == 0


def test_3():
    """Your function should sum the even-valued Fibonacci numbers:
    fibo_even_sum(8) should return 10."""
    assert fibo_even_sum(8) == 10


def test_4():
    """fibo_even_sum(10) should return 10."""
    assert fibo_even_sum(8) == 10


def test_5():
    """fibo_even_sum(34) should return 44."""
    assert fibo_even_sum(34) == 44


def test_6():
    """fibo_even_sum(60) should return 44."""
    assert fibo_even_sum(60) == 44


def test_7():
    """fibo_even_sum(1000) should return 798."""
    assert fibo_even_sum(1000) == 798


def test_8():
    """fibo_even_sum(100000) should return 60969."""
    assert fibo_even_sum(100000) == 60696


def test_9():
    """fibo_even_sum(4000000) should return 4613732."""
    assert fibo_even_sum(4000000) == 4613732
