def latticePaths(n):
	"""
	Returns the number of unique paths available when traversing a grid of size n from the top left to bottom right corner,
	when only downward or rightwards movement is allowed.
	"""

	lattice = []
	for i in range(1, n + 1):
		sub_list = [1]
		for j in range(1, i):
			sub_list.append(sub_list[-1] + lattice[i - 2][j])
		sub_list.append(sub_list[-1] * 2)

		lattice.append(sub_list)

	return lattice[-1][-1]
