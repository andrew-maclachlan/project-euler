def longestCollatzSequence(limit):
	"""
	Returns the number under a given limit that produces the longest sequence length with the following rules.

	n → n/2 	(n is even)
	n → 3n + 1 	(n is odd)
	"""

	max_sequence_length = 0
	max_sequence_number = 1

	for i in range(1, limit):
		n = i
		sequence_length = 1
		while n != 1:
			if n % 2 == 0:
				n = n / 2
			else:
				n = n * 3 + 1
			sequence_length += 1
		if sequence_length > max_sequence_length:
			max_sequence_length = sequence_length
			max_sequence_number = i

	return int(max_sequence_number)
