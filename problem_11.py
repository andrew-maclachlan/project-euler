def largestGridProduct(grid, n) -> int:
	"""
	Takes a 2D grid (list of lists) and returns the greatest product of length n from adjacent numbers.
	"""
	from common_functions import listProduct

	max_product = 0

	def sub_grid_sweep(grid, sub_max_product = 0) -> int:
		# Horizontal Sweep
		for i in grid:
			product = listProduct(i)
			if product > sub_max_product:
				sub_max_product = product

		# Vertical Sweep
		for i in zip(*grid[::-1]):
			product = listProduct(i)
			if product > sub_max_product:
				sub_max_product = product

		# Diagonal \ lr
		diag_sum_lr = 1
		for i,j in enumerate(grid):
			diag_sum_lr *= j[i]
			if diag_sum_lr > sub_max_product:
				sub_max_product = diag_sum_lr

		# Diagonal / rl
		diag_sum_rl = 1
		for i,j in enumerate(grid):
			diag_sum_rl *= j[-(i+1)]
			if diag_sum_rl > sub_max_product:
				sub_max_product = diag_sum_rl

		return sub_max_product

	for row in range(0, len(grid) - n + 1):
		for col in range(0, len(grid) - n + 1):
				sub_grid = [i[col:col + n] for i in grid[row:row + n]]
				sub_max = sub_grid_sweep(sub_grid)
				if sub_max > max_product:
					max_product = sub_max

	return max_product
