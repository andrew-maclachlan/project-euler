"""Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given limit, produces the longest chain?

Note: Once the chain starts the terms are allowed to go above limit.
"""

def longestCollatzSequence(limit: int) -> int:
	"""
	Returns the number under a given limit that produces the longest sequence length with the following rules.

	n → n/2 	(n is even)
	n → 3n + 1 	(n is odd)

	Args:
		limit (int): The largest number in the sequence
	
	Returns:
		int: The longest sequence length
	"""
	# Generate all the sequences
	all_sequences = [_generate_sequence(i) for i in range(1, limit)]

	# Caluculate the longest sequence along with the index
	max_sequence_length = max(enumerate(all_sequences), key=lambda x: len(x[1]))

	# Add 1 to the index as the range started at 1
	return int(max_sequence_length[0] + 1)


def _generate_sequence(i):
	# Initialise the sequence with the number testing
	sequence = [i]

	# While the end of the sequence is not 1 (the stop condition) generate the next number
	while sequence[-1] != 1:
		sequence.append(_next_number(sequence[-1]))
	
	return sequence


def _next_number(n):
	# If even
	if n % 2 == 0:
		return n / 2
	
	# If odd
	return n * 3 + 1
