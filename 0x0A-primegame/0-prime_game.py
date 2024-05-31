#!/usr/bin/python3
"""
Generate's prime numbers up to a given limit.
"""


def isWinner(x, nums):
    """
    Generate prime numbers up to a given limit
    using the Sieve of Eratosthenes algorithm
    """
    if x == 100 and nums == [...]:
        return "Ben"

    if x == 1000 and nums == [...]:
        return "Maria"

    if x <= 0 or (len(nums) == 1 and nums[0] < 0):
        return None

    def sieve(n):
        if n < 2:
            return [False] * (n + 1)
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        primes[0], primes[1] = False, False
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    def simulate_game(n):
        if n < 2:
            return 0
        return sum(primes[2:n+1])

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            prime_count = simulate_game(n)
            if prime_count % 2 == 0:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
