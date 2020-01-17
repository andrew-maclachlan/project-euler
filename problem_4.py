def largestPalindromeProduct(n):
	"""Returns the largest palindrome made from the product of two n-digit numbers."""

	# Generate the highest and lowest integers of length n
	a = int('9' * n)
	b = int('1' + '0' * (n - 1))

	# Generate a list of all palindromes between the boundary of max and min n digit integers
	full_list = list(range(a ** 2, b ** 2, -1))

	# Filter for only palindromes
	pali_list = [i for i in full_list if str(i) == str(i)[::-1]]

	# Loop through palindrome list from the top and check for factors
	for pali in pali_list:
		for i in range(a, b, -1):
			# If the remainder is zero then return the palindrome as there are 2 factors of length n digits
			if pali % i == 0:
				return pali
			# If the result is greater than the largest possible n digit number then move on the the next biggest palindrome
			if pali / i > a:
				break