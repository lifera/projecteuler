'''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work
from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


def eratosthenes_sieve(n: int) -> list:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for index in range(2, n + 1):
        if sieve[index]:
            primes.append(index)
            for a in range(index * index, n + 1, index):
                sieve[a] = False

    return primes


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for q in range(2, int(n ** .5) + 1):
        if n % q == 0:
            return False
    return True


def solution():

    primes = eratosthenes_sieve(1000000)
    answer = []

    for prime in primes:
        good = True
        s = str(prime)
        for i in range(len(s)):
            print(s)
            if not is_prime(int(s[i:])):
                good = False
                break
            if not is_prime(int(s[:len(s)-i])):
                good = False
                break

        if prime in (2, 3, 5, 7):
            good = False
        if good:
            answer.append(prime)

    print(answer)
    print(f'answer sum = {sum(answer)} len = {len(answer)}')


def is_truncatable_prime(n: int) -> bool:
    s = str(n)
    if not is_prime(n):
        return False
    for i in range(len(s)):
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:len(s) - i])):
            return False
    return True


def solution2():
    def rec_check_next_prime(n: int):
        for next_candidate in numbs_to_check:
            check_number = int(str(n) + str(next_candidate))
            if is_prime(check_number):
                if is_truncatable_prime(check_number):
                    truncatable_primes.add(check_number)
                rec_check_next_prime(check_number)

    truncatable_primes = set()
    numbs_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in numbs_to_check:
        if is_prime(i):
            rec_check_next_prime(i)

    print(truncatable_primes)
    print(f'truncatable_primes sum = {sum(truncatable_primes)} len = {len(truncatable_primes)}')


if __name__ == '__main__':
    solution2()
