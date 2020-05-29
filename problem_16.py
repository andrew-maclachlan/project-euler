def powerDigitSum(n)->int:
	""" Returns the sum of the digits of the number 2**n
	"""

	power = str(2 ** n)

	digit_sum = 0
	for i in power:
		digit_sum += int(i)

	return digit_sum
