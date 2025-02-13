"""Problem 17: Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numberLetterCounts(limit: int) -> int:
	"""Returns the number of letters required to write all of the numbers from 1 up to limit in English.

	Args:
		limit (int): Maximum number to count up to.
	
	Returns:
		int: Sum of the letters
	"""
	# All English representations up to the the limit
	english_strs = [int_to_str(num) for num in range(1, limit+1)]

	# Calculate the number of chars in the strings
	letter_sums = [len(num_str.replace(" ", "")) for num_str in english_strs]

	# Sum all the char sums
	return sum(letter_sums)


def int_to_str(number: int) -> str:
	"""Convert an integer into its English string.
	
	Args:
		number (int): Number to convert.
	
	Returns:
		str: English language string
	"""
	cent_list = [
		'thousand',
		'million',
		'billion',
		'trillion'
	]

	# Convert the int to a str
	number_str = str(number)

	# Split the string into chunks of 3
	number_list = []
	while number_str:
		number_list.append(int(number_str[-3:]))
		number_str = number_str[:-3]

	# Reverse the list
	number_list.reverse()

	# Blank list to start
	number_list_str = []

	for i, hundred in enumerate(number_list):
		sub_list = [_hundred_int_to_str(hundred)]

		if i != 0:
			sub_list.append(cent_list[i-1])
		
		number_list_str[:0] = sub_list
	
	return " ".join(number_list_str)


def _hundred_int_to_str(num):
	num_dict = {
		'1': 'one',
		'2': 'two',
		'3': 'three',
		'4': 'four',
		'5': 'five',
		'6': 'six',
		'7': 'seven',
		'8': 'eight',
		'9': 'nine',
		'10': 'ten',
		'11': 'eleven',
		'12': 'twelve',
		'13': 'thirteen',
		'14': 'fourteen',
		'15': 'fifteen',
		'16': 'sixteen',
		'17': 'seventeen',
		'18': 'eighteen',
		'19': 'nineteen'
	}

	dec_dict = {
		'2': 'twenty',
		'3': 'thirty',
		'4': 'forty', 
		'5': 'fifty',
		'6': 'sixty',
		'7': 'seventy',
		'8': 'eighty',
		'9': 'ninety'
	}

	# Add 0s to the start to make the string 3 long
	num_str = ('00' + str(num))[-3:]

	# Blank list to begin
	number_list_str = []

	# If the first digit is not a 0
	if num_str[0] != '0':
		# Insert X hundred
		number_list_str.append(num_dict[num_str[0]])
		number_list_str.append('hundred')

		# If the end digits are not 00
		if num_str[1:] != '00':
			# Add an and
			number_list_str.append('and')
	
	# If final 2 digits with are in num_dic then add
	if sub_str := num_dict.get(num_str[1:]):
		number_list_str.append(sub_str)

	# If 2nd digit is in dec_dict then add
	elif sub_str := dec_dict.get(num_str[1]):
		number_list_str.append(sub_str)

		# Try to add the final digit as well
		number_list_str.append(num_dict.get(num_str[2]))
	
	# Try getting the final digit
	else:
		number_list_str.append(num_dict.get(num_str[2]))
	
	# Remove any blanks from the list
	number_list_str_clean = [i for i in number_list_str if i]

	# Return the list as a string
	return " ".join(number_list_str_clean)
