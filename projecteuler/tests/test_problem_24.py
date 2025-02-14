"""Tests for Problem 24.
"""

from ..projecteuler import lexicographicPermutations

def test_1():
    """lexicographicPermutations(699999) should return a number."""
    assert isinstance(lexicographicPermutations(699999), int)


def test_2():
    """lexicographicPermutations(699999) should return 1938246570."""
    assert lexicographicPermutations(699999) == 1938246570


def test_3():
    """lexicographicPermutations(899999) should return 2536987410."""
    assert lexicographicPermutations(899999) == 2536987410

def test_4():
    """lexicographicPermutations(900000) should return 2537014689."""
    assert lexicographicPermutations(900000) == 2537014689

def test_5():
    """lexicographicPermutations(999999) should return 2783915460."""
    assert lexicographicPermutations(999999) == 2783915460
