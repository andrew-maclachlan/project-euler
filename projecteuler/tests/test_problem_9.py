"""Tests for Problem 9.
"""

from ..projecteuler import special_pythagorean_triplet


def test_1():
    """special_pythagorean_triplet(24) should return a number."""
    assert isinstance(special_pythagorean_triplet(24), int)


def test_2():
    """special_pythagorean_triplet(24) should return 480."""
    assert special_pythagorean_triplet(24) == 480


def test_3():
    """special_pythagorean_triplet(120) should return 49920, 55080 or 60000."""
    assert special_pythagorean_triplet(120) in [49920, 55080, 60000]


def test_4():
    """special_pythagorean_triplet(100) should return 31875000."""
    assert special_pythagorean_triplet(1000) == 31875000
