'''

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?

'''


def eratosthenes_sieve(n: int) -> list:
    # Not gonna need this
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    primes = []
    for index in range(2, n + 1):
        if sieve[index]:
            primes.append(index)
            for i in range(index * index, n + 1, index):
                sieve[i] = False

    return primes


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def solution():
    primes = []
    for numb in range(3, 10000, 2):
        conjecture_true = False
        if is_prime(numb):
            primes.append(numb)
        else:
            for prime in primes:
                for square in range(1, int(numb**0.5)):
                    if 2*square*square + prime == numb:
                        conjecture_true = True
                    if conjecture_true:
                        break
                if conjecture_true:
                    break
            if not conjecture_true:
                print(numb)


if __name__ == '__main__':
    solution()
