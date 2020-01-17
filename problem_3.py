def largestPrimeFactor(number) -> int:
	"""Returns the largest prime factor of any given integer."""

	# Initialise a variable to try as a factor
	factor_check = 2

	# Find the smallest factor and divide the given integer by this smallest factor. Repeat with the result until the final, largest, factor is found.
	while factor_check < number:
		# If the division has no remainder then factor_check is factor.
		if number % factor_check == 0:
			# Repeat the check with the result of the number divided by the smallest factor.
			return largestPrimeFactor(number / factor_check)
		# If there is a remainder then factor_check is not a factor so increment by 1 and try the next highest integer.
		else:
			factor_check += 1
	
	return int(number)