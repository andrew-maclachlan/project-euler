def sumSquareDifference(n) -> int:
	""" Takes an integer (n) and returns the difference between the sum of the squares of the first n natural numbers and the square of the sum. """

	# Sum the squares
	sum_squares = 0
	i = 1
	while i <= n:
		sum_squares += i ** 2
		i += 1

	# Square the sums
	square_sums = 0
	j = 1
	while j <= n:
		square_sums += j
		j += 1
	square_sums = square_sums ** 2

	# Return the difference between the two
	return square_sums - sum_squares