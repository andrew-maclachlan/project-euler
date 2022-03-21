# Problem 1
# https://www.freecodecamp.org/learn/coding-interview-prep/project-euler/problem-1-multiples-of-3-and-5
def multiplesOf3and5(n) -> int:
    """
    Returns the sum of all the multiples of 3 or 5 below n.
    """
    if type(n) is not type(int()):
        raise ValueError("Input must be of type int.")
    
    # Create lists of the multiples of 3 and 5 up to the provided integer
    multiples_of_3 = {*range(3, n, 3)}
    multiples_of_5 = {*range(5, n, 5)}

    # Sum the unique values in both lists
    return sum(multiples_of_3.union(multiples_of_5))
