"""Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two n-digit numbers.
"""


def largest_palindrome_product(num_digits: int) -> int:
    """Return the largest palindrome made from the product of two numbers with the number of digits
    num_digits.
    """
    # Generate the highest and lowest integers with number of digits num_digits
    num_min = int('1' + '0' * (num_digits - 1))
    num_max = int('9' * num_digits)

    # Generate a list of all palindromes between the largest and smallest possible products
    palindrome_list = [i for i in range(num_min ** 2, num_max ** 2) if str(i) == str(i)[::-1]]

    # Check the palidrome list for all factors between num_max and num_min
    return max([palindrome for i in range(num_min, num_max)
                if palindrome % i == 0 and palindrome / i <= num_max]
               for palindrome in palindrome_list)[0]
