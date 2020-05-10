def largeSum(number_list, n):
	"""
	Returns the first n digits in the sum of a list of integers.
	"""
	return str(sum(number_list))[:n]
