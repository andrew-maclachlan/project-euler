"""Problem 32: Pandigital products
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through n pandigital.
"""
from itertools import permutations, combinations

def pandigitalProducts(n: int) -> int:
    """Calculate the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through n pandigital.

    Args:
        n (int): Number of digits to use
    
    Returns:
        int: Sum of all pandigital products
    """
    # All pandigital products as a set to remove duplicates
    pandigital_products = set()

    # For each order of all digits up to n
    for number_order in permutations(range(1, n+1)):

        # For all possible positions of the x and = in the order of numbers
        for op_pos in combinations(range(1, n), 2):
            
            # Split the ordered numbers based on each combination of x and = position
            multiplicand = int("".join(str(i) for i in number_order[:op_pos[0]]))
            multiplier = int("".join(str(i) for i in number_order[op_pos[0]:op_pos[1]]))
            product = int("".join(str(i) for i in number_order[op_pos[1]:]))

            # If the sum is correct then and the product to the set
            if multiplicand * multiplier == product:
                pandigital_products.add(product)

    return sum(pandigital_products)
