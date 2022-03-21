# Problem 16
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-16-power-digit-sum

def powerDigitSum(n)->int:
	"""
	Returns the sum of the digits of the number 2**n
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	power = str(2 ** n)
	digit_sum sum([int(i) for i in power])

	return digit_sum
