# Problem 17
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-17-number-letter-counts
def numberLetterCounts(limit):
	"""
	Returns the number of letters required to write all of the numbers from 1 up to limit in English.
	"""
	num_dict = {
		'1': 'one', '2': 'two',	'3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',	'9': 'nine',
		'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'
	}

	dec_dict = {
		'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'
	}

	cent_list = [
		'hundred',
		'thousand',
		'million',
		'billion',
		'trillion'
	]

	def _englishNumber(number):
		if len(str(number)) % 3 == 0:
			number_str = str(number)
		else:
			number_str = (3 - len(str(number)) % 3)  * '0' + str(number)

		number_list = [number_str[i:i+3] for i in range(0, len(number_str), 3)]
		number_list_len = len(number_list) - 1

		number_list_str = []
		for i, num in enumerate(number_list):
			if num[0] in num_dict:
				number_list_str.append(num_dict[num[0]])
				number_list_str.append(cent_list[0])
				if int(num[1:]) > 0:
					number_list_str.append('and')
				elif i == number_list_len and number_list_len > 0:
					number_list_str.insert(-2, 'and')
			elif i == number_list_len and number_list_len > 0:
				number_list_str.append('and')

			if str(int(num[1:])) in num_dict:
				number_list_str.append(num_dict[str(int(num[1:]))])
			elif num[1] in dec_dict:
				number_list_str.append(dec_dict[num[1]])
				if num[2] in num_dict:
					number_list_str.append(num_dict[num[2]])

			if i != number_list_len and int(num) != 0:
				number_list_str.append(cent_list[number_list_len - i])

			if number_list_str[-1] == 'and':
				number_list_str = number_list_str[:-1]

		return number_list_str

	letter_sum = 0
	for num in range(1, limit + 1):
		letter_sum += sum([len(i) for i in _englishNumber(num)])

	return letter_sum
