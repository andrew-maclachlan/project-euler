"""Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example,
32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such
that a + b + c = n.
"""


def special_pythagorean_triplet(n: int) -> int:
    """Return the product of a*b*c where a+b+c = n and a,b,c are a pythagorean triplet.
    """
    a = 1
    b = a + 1
    c = n - b - a

    while a < b < c:
        while b < c:
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
            b += 1
            c = n - b - a
        a += 1
        b = a + 1
        c = n - b - a
