def multiples_of_3_and_5(n: int) -> int:
    """Sum the multiples of 3 or 5 below n.

    Args:
        n (int):

    Returns:
        int:

    Raises:
        ValueError: If arg is not of type int
    """
    if type(n) is not type(int):
        raise ValueError("Input must be of type int.")
    
    # Create lists of the multiples of 3 and 5 up to the provided integer and convert to sets
    multiples_of_3 = {*range(3, n, 3)}
    multiples_of_5 = {*range(5, n, 5)}

    # Sum the unique values in both lists
    return sum(multiples_of_3.union(multiples_of_5))

# Test 4
