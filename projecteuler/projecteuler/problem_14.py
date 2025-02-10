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
