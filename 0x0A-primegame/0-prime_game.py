#!/usr/bin/python3

"""Method that determines the winner of a Prime Game"""


def isWinner(x, nums):
    def generate_primes(n):
        """Prime Game Method"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(2, n + 1) if sieve[i]]

    def simulate_game(n):
        """Simulate a game with set size n and return the winner."""
        primes = generate_primes(n)
        return 'Ben' if len(primes) % 2 == 0 else 'Maria'

    maria_wins = ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
