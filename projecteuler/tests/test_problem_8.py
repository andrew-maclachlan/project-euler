"""Tests for Problem 8.
"""

from ..projecteuler import largest_product_in_a_series


def test_1():
    """largest_product_in_a_series(4) should return a number."""
    assert isinstance(largest_product_in_a_series(4), int)


def test_2():
    """largest_product_in_a_series(4) should return 5832."""
    assert largest_product_in_a_series(4) == 5832


def test_3():
    """largest_product_in_a_series(13) should return 23514624000."""
    assert largest_product_in_a_series(13) == 23514624000
