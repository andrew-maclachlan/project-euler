"""Problem 31: Coin sums
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can n pence be made using any number of coins?
"""

import numpy as np
from itertools import combinations

def coinSums(price: int, coins: tuple = (1, 2, 5, 10, 20, 50, 100, 200)) -> int:
    """Calculate the number of ways that a price can be made using a set of coin sizes.

    Args:
        price (int): Price in pence to calculate.
        coins (tuple, optional): Different size of coins available. Defaults to English coins, (1, 2, 5, 10, 20, 50, 100, 200).
    
    Returns:
        int: Number of ways the price can be made
    """
    # Smallest representation of the price
    smallest_represention =  _smallest_representation(price, coins)

    # All combinations of coins starting with the smallest
    price_combinations = [smallest_represention]

    # Iterate up through more coins until all the smallest coins are used
    latest_representation = smallest_represention

    while len(latest_representation) < price:
        # Get the furthest right non-1 number in the tuple
        right_number = 1
        i = 1

        while right_number == 1:
            right_number = latest_representation[-i]
            rest_of_number = latest_representation[:-i]
            i += 1

        # Take the coin subset smallest than then righmost non-1 number
        smaller_coins = tuple(coin for coin in coins if coin < right_number)

        # Get the next biggest coin smaller than the righmost non-1 number
        largest_coin = max(smaller_coins)

        # Next in the seqence is...
        # everything to left of rightmost non-1
        # + largest coin smaller than rightmost non-1
        # + smallest representation using coins smaller than rightmost non-1
        latest_representation = rest_of_number + (largest_coin,) + _smallest_representation(price - sum(rest_of_number) - largest_coin, smaller_coins)

        # Add the next in sequence to the list
        price_combinations.append(latest_representation)
    
    # Return the list that contains all combinations
    return len(price_combinations)

def _smallest_representation(price, coins):
    # Smallest representation of a price
    smallest_represention = ()

    sub_price = price

    while sub_price >= min(coins):
        # Largest coin that is smaller than or equal to the sub_price
        largest_coin = max(coin for coin in coins if coin <= sub_price)

        # Add the largest available coin to the total and subtract from sub_price
        smallest_represention += (largest_coin,)
        sub_price -= largest_coin
    
    return smallest_represention