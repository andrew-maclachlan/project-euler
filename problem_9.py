# Problem 9
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-9-special-pythagorean-triplet
def specialPythagoreanTriplet(n) -> int:
	"""
	Returns the product of a*b*c where a+b+c = n and a,b,c are a pythagorean triplet.
	A pythagorean triplet is a set of three integers where a < b < c and a^2 + b^2 = c^2
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

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
