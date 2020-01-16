# Packages
import numpy as np

def multiplesOf3and5(number) -> int:
	""" Takes an integer as an input and returns the sum of all the multiples of 3 or 5 below the provided integer """
	
	# Create lists of the multiples of 3 and 5 up to and including the provided integer
	list_of_3s = list(range(3, number + 1, 3))
	list_of_5s = list(range(5, number + 1, 5))

	# Sum the 2 lists
	final_sum = np.sum(list_of_3s + list_of_5s)

	# Return the answer
	return final_sum