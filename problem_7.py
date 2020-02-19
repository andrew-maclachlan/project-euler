from common_functions import isPrime

def nthPrime(n):
	""" Return the nth prime """

	largest_prime = 2
	prime_counter = 1

	prime_check = 3
	while prime_counter < n:
		if isPrime(prime_check):
			prime_counter += 1
			largest_prime = prime_check
		prime_check += 2

	return largest_prime