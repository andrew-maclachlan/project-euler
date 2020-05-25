# Problem 1
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-1-multiples-of-3-and-5
def multiplesOf3and5(n) -> int:
	"""
	Returns the sum of all the multiples of 3 or 5 below n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")
	
	# Create lists of the multiples of 3 and 5 up to the provided integer
	list_of_3s = list(range(3, n, 3))
	list_of_5s = list(range(5, n, 5))

	# Sum the 2 lists
	return sum(set(list_of_3s + list_of_5s))

# Problem 2
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-2-even-fibonacci-numbers
def fiboEvenSum(n):
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

# Problem 3
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-3-largest-prime-factor
def largestPrimeFactor(n) -> int:
	"""
	Returns the largest prime factor of any given integer.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 2:
		raise ValueError("Input must be greater than 1.")

	# Find the smallest factor and divide the input integer by this smallest factor. Repeat with the result until the final, largest, factor is found.
	factor_check = 2
	while factor_check < n:
		if n % factor_check == 0:
			return largestPrimeFactor(int(n / factor_check))
		else:
			factor_check += 1
	
	return n

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

# Problem 5
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-5-smallest-multiple
def smallestMult(n) -> int:
	"""
	Returns the smallest positive integer that is evenly divisible by all the numbers from 1 to n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import allPrimeFactors

	# Generate a list of integers from 1 to n
	integer_list = list(range(1, n + 1))

	# List of factors that will provide the min product
	final_list = []

	# Loop through all the integers up to and including the provided n
	for integer in integer_list:
		# Return a list of prime factors of the current factor
		prime_factors = allPrimeFactors(integer)

		# Loop through each of the numbers in the unique list of prime factors
		for number in set(prime_factors):
			# Count the difference in the number of each prime factor against what is already in the final_list
			diff_count = prime_factors.count(number) - final_list.count(number)

			# Append the number of missing factors to the final list
			final_list.append(list(diff_count))

	# Calculate the product of the integers in the final list
	max_product = 1
	for factor in final_list:
		max_product *= factor
		
	return max_product

# Problem 6
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-6-sum-square-difference
def sumSquareDifference(n) -> int:
	"""
	Takes an integer n and returns the difference between the sum of the squares of the first n natural numbers and the square of the sum.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	# Sum the squares
	sum_square = sum(map(lambda i: i ** 2, range(1, n + 1)))

	# Square the sums
	square_sums = sum(range(1, n + 1)) ** 2

	# Return the difference between the two
	return square_sums - sum_squares

# Problem 7
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-7-10001st-prime
def nthPrime(n) -> int:
	"""
	Return the nth prime.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import isPrime

	largest_prime = 2
	prime_counter = 1

	prime_check = 3
	while prime_counter < n:
		if isPrime(prime_check):
			prime_counter += 1
			largest_prime = prime_check
		prime_check += 2

	return largest_prime

# Problem 8
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-8-largest-product-in-a-series
def largestProductinaSeries(n) -> int:
	"""
	Returns the n adjacent digits in a 1000-digit number that have the greatest product.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import listProduct

	# 1000 Digit number
	long_number = [7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,3,4,9,1,9,4,9,3,4,9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,9,8,4,8,0,1,8,6,9,4,7,8,8,5,1,8,4,3,8,5,8,6,1,5,6,0,7,8,9,1,1,2,9,4,9,4,9,5,4,5,9,5,0,1,7,3,7,9,5,8,3,3,1,9,5,2,8,5,3,2,0,8,8,0,5,5,1,1,1,2,5,4,0,6,9,8,7,4,7,1,5,8,5,2,3,8,6,3,0,5,0,7,1,5,6,9,3,2,9,0,9,6,3,2,9,5,2,2,7,4,4,3,0,4,3,5,5,7,6,6,8,9,6,6,4,8,9,5,0,4,4,5,2,4,4,5,2,3,1,6,1,7,3,1,8,5,6,4,0,3,0,9,8,7,1,1,1,2,1,7,2,2,3,8,3,1,1,3,6,2,2,2,9,8,9,3,4,2,3,3,8,0,3,0,8,1,3,5,3,3,6,2,7,6,6,1,4,2,8,2,8,0,6,4,4,4,4,8,6,6,4,5,2,3,8,7,4,9,3,0,3,5,8,9,0,7,2,9,6,2,9,0,4,9,1,5,6,0,4,4,0,7,7,2,3,9,0,7,1,3,8,1,0,5,1,5,8,5,9,3,0,7,9,6,0,8,6,6,7,0,1,7,2,4,2,7,1,2,1,8,8,3,9,9,8,7,9,7,9,0,8,7,9,2,2,7,4,9,2,1,9,0,1,6,9,9,7,2,0,8,8,8,0,9,3,7,7,6,6,5,7,2,7,3,3,3,0,0,1,0,5,3,3,6,7,8,8,1,2,2,0,2,3,5,4,2,1,8,0,9,7,5,1,2,5,4,5,4,0,5,9,4,7,5,2,2,4,3,5,2,5,8,4,9,0,7,7,1,1,6,7,0,5,5,6,0,1,3,6,0,4,8,3,9,5,8,6,4,4,6,7,0,6,3,2,4,4,1,5,7,2,2,1,5,5,3,9,7,5,3,6,9,7,8,1,7,9,7,7,8,4,6,1,7,4,0,6,4,9,5,5,1,4,9,2,9,0,8,6,2,5,6,9,3,2,1,9,7,8,4,6,8,6,2,2,4,8,2,8,3,9,7,2,2,4,1,3,7,5,6,5,7,0,5,6,0,5,7,4,9,0,2,6,1,4,0,7,9,7,2,9,6,8,6,5,2,4,1,4,5,3,5,1,0,0,4,7,4,8,2,1,6,6,3,7,0,4,8,4,4,0,3,1,9,9,8,9,0,0,0,8,8,9,5,2,4,3,4,5,0,6,5,8,5,4,1,2,2,7,5,8,8,6,6,6,8,8,1,1,6,4,2,7,1,7,1,4,7,9,9,2,4,4,4,2,9,2,8,2,3,0,8,6,3,4,6,5,6,7,4,8,1,3,9,1,9,1,2,3,1,6,2,8,2,4,5,8,6,1,7,8,6,6,4,5,8,3,5,9,1,2,4,5,6,6,5,2,9,4,7,6,5,4,5,6,8,2,8,4,8,9,1,2,8,8,3,1,4,2,6,0,7,6,9,0,0,4,2,2,4,2,1,9,0,2,2,6,7,1,0,5,5,6,2,6,3,2,1,1,1,1,1,0,9,3,7,0,5,4,4,2,1,7,5,0,6,9,4,1,6,5,8,9,6,0,4,0,8,0,7,1,9,8,4,0,3,8,5,0,9,6,2,4,5,5,4,4,4,3,6,2,9,8,1,2,3,0,9,8,7,8,7,9,9,2,7,2,4,4,2,8,4,9,0,9,1,8,8,8,4,5,8,0,1,5,6,1,6,6,0,9,7,9,1,9,1,3,3,8,7,5,4,9,9,2,0,0,5,2,4,0,6,3,6,8,9,9,1,2,5,6,0,7,1,7,6,0,6,0,5,8,8,6,1,1,6,4,6,7,1,0,9,4,0,5,0,7,7,5,4,1,0,0,2,2,5,6,9,8,3,1,5,5,2,0,0,0,5,5,9,3,5,7,2,9,7,2,5,7,1,6,3,6,2,6,9,5,6,1,8,8,2,6,7,0,4,2,8,2,5,2,4,8,3,6,0,0,8,2,3,2,5,7,5,3,0,4,2,0,7,5,2,9,6,3,4,5,0]

	greatest_product = 0
	for i in range(0, len(long_number) - (n - 1)):
			list_segment = long_number[i:(i+n)]

			list_segment_product = listProduct(list_segment)

			if list_segment_product > greatest_product:
				greatest_product = list_segment_product

	return greatest_product

# Problem 9
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-9-special-pythagorean-triplet
def specialPythagoreanTriplet(n) -> int:
	"""
	Returns the product of a*b*c where a+b+c = n and a,b,c are a pythagorean triplet.
	A pythagorean triplet is a set of three integers where a < b < c and a^2 + b^2 = c^2
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	a = 1
	b = a + 1
	c = n - b - a

	while a < b and b < c:
		while b < c:
			if a**2 + b**2 == c**2:
				return a*b*c
			else:
				b += 1
				c = n - b - a
		a += 1
		b = a + 1
		c = n - b - a

# Problem 10
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-10-summation-of-primes
def primeSummation(n) -> int:
	"""
	Returns the sum of all primes below n.
	"""
	if type(n) is not type(int()):
		raise ValueError("Input must be of type int.")

	if n < 1:
		raise ValueError("Input must be positive.")

	from common_functions import isPrime

	return sum(filter(isPrime, range(n)))
