# Problem 2
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-2-even-fibonacci-numbers
def fiboEvenSum(n) -> int:
	"""
	Returns the sum of all even numbers in the fibonacci sequence of length n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 2:
		raise ValueError("Input must be greater than 1.")

	# Generate a fibonacci sequence of length n
	fibo_seq = [1, 2]
	while fibo_seq[-1] < n:
		fibo_seq.append(sum(fibo_seq[-2:]))

	# Return the sum of all even numbers in the sequence
	return sum([i for i in fibo_seq if i % 2 == 0])
