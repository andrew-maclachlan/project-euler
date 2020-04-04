def primeSummation(n) -> int:
	"""	Returns the sum of all primes below n.
	"""

	from common_functions import isPrime

	primes_sum = 0
	for i in range(n):
		if isPrime(i):
			primes_sum += i

	return primes_sum
