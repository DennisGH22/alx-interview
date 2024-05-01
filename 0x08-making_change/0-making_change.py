#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in your possession.
        total (int): The amount total to be met.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If total is 0 or less, return 0.
             If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    min_coins_needed = [float('inf')] * (total + 1)
    min_coins_needed[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins_needed[amount] = min(
                min_coins_needed[amount], min_coins_needed[amount - coin] + 1)

    return min_coins_needed[total] if (
        min_coins_needed[total] != float('inf')) else -1
