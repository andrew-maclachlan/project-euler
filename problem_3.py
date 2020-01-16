def largestPrimeFactor(number) -> int:
	"""Returns the largest prime factor of any given integer."""

	i = 2
	while i < number:
		if number % i == 0:
			return largestPrimeFactor(number / i)
		i += 1
	
	return int(number)