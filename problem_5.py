def smallestMult(n) -> int:
	"""Returns the smallest positive integer that is evenly divisible by all the numbers from 1 to n."""

	# Generate a list of integers from 1 to n
	factor_list = list(range(n, 0, -1))
	
	# Generate maximum product. This will be the upper limit as it is all factor mulitplied together
	max_product = 1
	for factor in factor_list:
		max_product *= factor
	
	# Get max factor from the list and set it as the first check
	max_factor = max(factor_list)
	multiple_check = max_factor

	# If the smallest multiple check becomes larger than the max_product then max_product is also the smallest mult
	while multiple_check < max_product:
		# Check whether each factor divides equally and if any doesn't the break the loop and move on the the next iteration. If all factors divide equally then return the checked integer.
		for factor in factor_list:
			if multiple_check % factor != 0:
				multiple_check += max_factor
				break
		else:
			return multiple_check
	return max_productexit()