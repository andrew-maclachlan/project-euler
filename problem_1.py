# Problem 1
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-1-multiples-of-3-and-5
def multiplesOf3and5(n) -> int:
	"""
	Returns the sum of all the multiples of 3 or 5 below n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")
	
	# Create lists of the multiples of 3 and 5 up to the provided integer
	list_of_3s = list(range(3, n, 3))
	list_of_5s = list(range(5, n, 5))

	# Sum the 2 lists
	return sum(set(list_of_3s + list_of_5s))
