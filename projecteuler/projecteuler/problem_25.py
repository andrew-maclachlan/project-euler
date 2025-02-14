"""Problem 25: 1000-digit Fibonacci number
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain n digits?
"""

def digitFibonacci(n: int) -> int:
    """Get the index of the first term in the fibonacci sequence that contains n digits.

    Args:
        n (int): Number of digits
    
    Returns:
        int: First term with n digits
    """
    previous_term = 1
    latest_term = 1
    term_cnt = 2

    # While the latest term in the fibonacci sequence is less than the require length
    while len(str(latest_term)) < n:
        # Generate the next term and demote latest_term to previous_term
        previous_term, latest_term = latest_term, previous_term + latest_term

        # Increment the term counter that starts at 2 since the first terms 1, 1 were hardcorded
        term_cnt += 1
    
    return term_cnt
