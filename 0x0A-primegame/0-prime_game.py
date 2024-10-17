#!/usr/bin/python3
def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    def count_prime_moves(n):
        is_removed = [False] * (n + 1)
        move_count = 0

        for prime in primes:
            if prime > n:
                break
            if not is_removed[prime]:
                move_count += 1
                for multiple in range(prime, n + 1, prime):
                    is_removed[multiple] = True

        return move_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_moves = count_prime_moves(n)
        if prime_moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
