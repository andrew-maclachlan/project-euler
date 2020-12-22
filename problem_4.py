# Problem 4
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-4-largest-palindrome-product
def largestPalindromeProduct(n) -> int:
	"""
	Returns the largest palindrome made from the product of two n-digit numbers.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	# Generate the highest and lowest integers of length n
	a = int('9' * n)
	b = int('1' + '0' * (n - 1))

	# Generate a list of all palindromes between the largest and smallest possible products of 2 n digit numbers
	pali_list = [i for i in range(a ** 2, b ** 2, -1) if str(i) == str(i)[::-1]]

	# Loop through palindrome list from the top and check for factors
	for pali in pali_list:
		for i in range(a, b, -1):
			# If the result is greater than the largest possible n digit number then move on the the next biggest palindrome
			if pali / i > a:
				break
			# If the remainder is zero then return the palindrome as there are 2 factors of length n digits
			if pali % i == 0:
				return pali
