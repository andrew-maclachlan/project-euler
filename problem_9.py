def specialPythagoreanTriplet(n) -> int:
	"""	Returns the product of a*b*c where a+b+c = n and a,b,c are a pythagorean triplet.
		A pythagorean triplet is a set of three integers where a < b < c and a^2 + b^2 = c^2
	"""

	a = 1
	b = a + 1
	c = n - b - a

	while a < b and b < c:
		while b < c:
			if a**2 + b**2 == c**2:
				return a*b*c
			else:
				b += 1
				c = n - b - a
		a += 1
		b = a + 1
		c = n - b - a
