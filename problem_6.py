# Problem 6
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-6-sum-square-difference
def sumSquareDifference(n) -> int:
	"""
	Takes an integer n and returns the difference between the sum of the squares of the first n natural numbers and the square of the sum.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	# Sum the squares
	sum_square = sum(map(lambda i: i ** 2, range(1, n + 1)))

	# Square the sums
	square_sums = sum(range(1, n + 1)) ** 2

	# Return the difference between the two
	return square_sums - sum_squares
