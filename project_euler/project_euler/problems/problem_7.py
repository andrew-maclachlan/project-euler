# Problem 7
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-7-10001st-prime

from common_functions import isPrime

def nthPrime(n) -> int:
	"""
	Return the nth prime.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	largest_prime = 2
	prime_counter = 1

	prime_check = 3
	while prime_counter < n:
		if isPrime(prime_check):
			prime_counter += 1
			largest_prime = prime_check
		prime_check += 2

	return largest_prime
