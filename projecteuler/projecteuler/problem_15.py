"""Problem 15: Lattice paths
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

a diagram of 6 2 by 2 grids showing all the routes to the bottom right corner
How many such routes are there through a given gridSize?
"""

def latticePaths(n: int) -> int:
	"""Returns the number of unique paths available when traversing a grid of size n from the top left to bottom right corner,
	when only downward or rightwards movement is allowed.

	Args: 
	 	n (int): Maximum gridsize
	
	Returns:
		int: Number of unique paths
	"""

	lattice = []
	
	for i in range(1, n+1):
		sub_list = [1]
		for j in range(1, i):
			sub_list.append(sub_list[-1] + lattice[i-2][j])
		sub_list.append(sub_list[-1] * 2)

		lattice.append(sub_list)

	return lattice[-1][-1]
