"""Tests for Problem 4.
"""

from ..problems import largest_palindrome_product


def test_1():
    """largest_palindrome_product(2) should return a number."""
    assert isinstance(largest_palindrome_product(2), int)


def test_2():
    """largest_palindrome_product(2) should return 9009."""
    assert largest_palindrome_product(2) == 9009


def test_3():
    """largest_palindrome_product(3) should return 906609."""
    assert largest_palindrome_product(3) == 906609
