def sumSquareDifference(n) -> int:
	""" Takes an integer n and returns the difference between the sum of the squares of the first n natural numbers and the square of the sum. """

	# Sum the squares
	sum_squares = 0
	for i in range(1, n + 1):
		sum_squares += i ** 2

	# Square the sums
	square_sums = sum(range(1, n + 1)) ** 2

	# Return the difference between the two
	return square_sums - sum_squares
