def fiboEvenSum(n):
	"""Returns the sum of all even numbers in the fibonacci sequence of length n."""

	# Initialise the start of the fibonacci sequence
	fibo_seq = [1, 2]

	# Generate the fibonacci sequence of length n
	for i in range(n - 2):
		fibo_seq.append(fibo_seq[-2:])

	# Filter the sequence for only even numbers
	fibo_seq_even = [i for i in fibo_seq if i % 2 == 0]

	# Sum the list
	final_sum = sum(fibo_seq_even)

	# Return final_sum
	return final_sum