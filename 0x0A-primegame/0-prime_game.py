#!/usr/bin/python3
def isWinner(x, nums):
    """
    Generate prime numbers up to a given limit
    using the Sieve of Eratosthenes algorithm
    """
    def sieve(n):
        primes = [True] * (n+1)
        primes[0], primes[1] = False, False
        p = 2
        while p*p <= n:
            if primes[p]:
                for i in range(p*p, n+1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(2, n+1) if primes[i]]

    def simulate_game(n):
        primes = sieve(n)
        remaining_primes = len(primes)
        return remaining_primes % 2 == 0

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if simulate_game(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
