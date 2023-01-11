# Problem 10
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-10-summation-of-primes
def primeSummation(n) -> int:
	"""
	Returns the sum of all primes below n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import isPrime

	return sum(filter(isPrime, range(n)))
