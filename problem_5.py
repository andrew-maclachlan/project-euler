# Problem 5
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-5-smallest-multiple
def smallestMult(n) -> int:
	"""
	Returns the smallest positive integer that is evenly divisible by all the numbers from 1 to n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import allPrimeFactors

	# Generate a list of integers from 1 to n
	integer_list = [*range(1, n + 1)]

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
			final_list.append(list(diff_count))

	# Calculate the product of the integers in the final list
	max_product = 1
	for factor in final_list:
		max_product *= factor
		
	return max_product
