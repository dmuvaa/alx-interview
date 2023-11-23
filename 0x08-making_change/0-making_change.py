#!/usr/bin/python3

"""Create a Function"""


def makeChange(coins, total):
    """Func that determines the fewest number of coins
    needed to meet a given amount
    """
    if total <= 0:
        return 0

    minCoins = [total + 1] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return -1 if minCoins[total] > total else minCoins[total]
