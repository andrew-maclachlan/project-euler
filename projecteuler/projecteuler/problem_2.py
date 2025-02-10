"""Problem 2: Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting
with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the
even-valued terms.
"""


def fibo_even_sum(n: int) -> int:
    """Return the sum of all even numbers in the fibonacci sequence of length n.

    Args:
        n (int):

    Returns:
        int
    """
    # Generate a fibonacci sequence of length n
    fibo_seq = [1, 2]
    while fibo_seq[-1] < n:
        fibo_seq.append(sum(fibo_seq[-2:]))

    # Return the sum of all even numbers in the sequence
    return sum(i for i in fibo_seq if i % 2 == 0)
