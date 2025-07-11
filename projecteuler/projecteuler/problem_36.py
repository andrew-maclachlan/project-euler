"""Problem 36: Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1000000, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def doubleBasePalindromes(n):
    """Return the sum of all numbers below n that are palindromic in both base 10 and base 2.
    
    Args:
        n (int): The upper limit for the search.
    
    Returns:
        int: The sum of all qualifying numbers.
    """
    total = 0
    for i in range(1, n):
        if _is_palindrome(str(i)) and _is_palindrome(bin(i)[2:]):
            total += i

    return total


def _is_palindrome(s):
        return s == s[::-1]
