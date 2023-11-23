#!/usr/bin/python3

"""Create a Function"""


def makeChange(coins, total):
    """Func that determines the fewest number of coins
    needed to meet a given amount
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)

    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        if coin > total:
            continue
        for i in range(coin, total + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return -1 if minCoins[total] == float('inf') else minCoins[total]
