# Problem 3
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-3-largest-prime-factor
def largestPrimeFactor(n) -> int:
	"""
	Returns the largest prime factor of any given integer.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 2:
		raise ValueError("Input must be greater than 1.")

	# Find the smallest factor and divide the input integer by this smallest factor.
	# Repeat with the result until the final, largest, factor is found.
	factor_check = 2
	while factor_check < n:
		if n % factor_check == 0:
			return largestPrimeFactor(int(n / factor_check))
		else:
			factor_check += 1
	
	return n
