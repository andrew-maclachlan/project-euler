def divisibleTriangleNumber(n) -> int:
	"""
	Returns the lowest triangle number with over n divisors.
	"""
	from common_functions import allPrimeFactors

	max_divisors = 0
	i = 0
	triangle_number = 0
	while max_divisors <= n:
		i += 1
		triangle_number += i
		divisor_count = 1

		prime_factors = allPrimeFactors(triangle_number)
		for number in set(prime_factors):
			divisor_count *= prime_factors.count(number) + 1

		if divisor_count > max_divisors:
			max_divisors = divisor_count

	return triangle_number
