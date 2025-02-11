"""Problem 16: Power digit sum
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2exponent?
"""

def powerDigitSum(n: int)->int:
	"""Return the sum of the digits of the number 2**n

	ArgsL
		n (int): number to perform calculation on
	
	Returns:
		int:
	"""
	# Calculate the power and store as a sting
	power_str = str(2 ** n)

	# Iterate through the digits and sum
	digit_sum = sum(int(digit) for digit in power_str)

	return digit_sum
