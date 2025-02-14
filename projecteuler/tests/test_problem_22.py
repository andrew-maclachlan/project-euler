"""Tests for Problem 22.
"""

from ..projecteuler import namesScores

test1 = ['THIS', 'IS', 'ONLY', 'A', 'TEST']
test2 = ['I', 'REPEAT', 'THIS', 'IS', 'ONLY', 'A', 'TEST']

with open('data/names.txt', 'r') as f:
    names = f.read()

names = names.replace('"', '').split(',')

def test_1():
    """namesScores(test1) should return a number."""
    assert isinstance(namesScores(test1), int)


def test_2():
    """namesScores(test1) should return 791."""
    assert namesScores(test1) == 791


def test_3():
    """namesScores(test2) should return 1468."""
    assert namesScores(test2) == 1468

def test_4():
    """namesScores(names) should return 871198282."""
    assert namesScores(names) == 871198282
