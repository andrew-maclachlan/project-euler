def allPrimeFactors(number) -> list:
	"""
	Returns a list of all prime factors of a given integer.
	"""
	# Return a list of prime factors
	return _allPrimeFactorsIter(number)

def _allPrimeFactorsIter(number, prime_list = None):
		# Initialise List
		if prime_list is None:
			prime_list = []

		# Initialise a variable to try as a factor
		factor_check = 2

		# Find the smallest factor and divide the given integer by this smallest factor. Repeat with the result until there is a list of all factors.
		while factor_check <= number:
			# If the division has no remainder then factor_check is factor.
			if number % factor_check == 0:
				# Append the factor to the list
				prime_list.append(factor_check)

				# Repeat the check with the result of the number divided by the smallest factor.
				return _allPrimeFactorsIter(number / factor_check, prime_list)
			# If there is a remainder then factor_check is not a factor so increment by 1 and try the next highest integer.
			else:
				factor_check += 1

		# Return a list of prime factors
		return prime_list

def isPrime(number) -> bool:
	"""
	Returns True if the provide integer is prime.
	"""

	if number < 2:
		return False

	if number == 2:
		return True

	i = 2
	while i**2 <= number:
		if number % i == 0:
			return False
		
		if i == 2:
			i -= 1
		
		i += 2
	
	return True

def listProduct(list) -> int:
	"""
	Returns the product of a list of integers.
	"""

	product = 1
	for i in list:
		product = product * i

	return product
