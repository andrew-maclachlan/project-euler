from common_functions import allPrimeFactors

def nthPrime(n):
	""" Return the nth prime """

	largest_prime = 2
	prime_counter = 1

	prime_check = 3
	while prime_counter < n:
		if len(allPrimeFactors(prime_check)) == 1: # This check is slow at high values of n
			prime_counter += 1
			largest_prime = prime_check
		prime_check += 2

	return largest_prime