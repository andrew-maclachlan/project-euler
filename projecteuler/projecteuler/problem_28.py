"""Problem 28: Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in an n by n spiral formed in the same way?
"""

def spiralDiagonals(size: int) -> int:
    """Calculate the sum of numbers on the diagonals of a spiral of size n by n.

    Args:
        size (int): Size of sides of the diagonal.
    
    Return:
        int: Sum of the diagonal numbers.
    """
    # Sum starts with the centre
    spiral_numbers = [1]

    # Number of rings in spiral
    ring_cnt = int((size + 1) / 2)

    # Loop through each ring
    for i in range(1, ring_cnt):
        # 4 sides of the spiral
        for _ in range(1, 5):
            next_number = spiral_numbers[-1] + (i * 2)
            spiral_numbers.append(next_number)
    
    return sum(spiral_numbers)
