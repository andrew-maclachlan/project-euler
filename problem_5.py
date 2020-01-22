# Some other useful functions
from common_functions import allPrimeFactors

def smallestMult(n) -> int:
	"""Returns the smallest positive integer that is evenly divisible by all the numbers from 1 to n."""

	# Generate a list of integers from 1 to n
	integer_list = list(range(1, n + 1))

	# List of factors that will provide the min product
	final_list = []

	# Loop through all the integers up to and including the provided n
	for integer in integer_list:
		# Return a list of prime factors of the current factor
		prime_factors = allPrimeFactors(integer)

		# Loop through each of the numbers in the unique list of prime factors
		for number in set(prime_factors):
			# Count the difference in the number of each prime factor against what is already in the final_list
			diff_count = prime_factors.count(number) - final_list.count(number)

			# Append the number of missing factors to the final list
			for i in range(diff_count):
				final_list.append(number)

	# Calculate the product of the integers in the final list
	max_product = 1
	for factor in final_list:
		max_product *= factor
		
	return max_product