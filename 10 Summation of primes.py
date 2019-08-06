'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def solution(n):

    def is_prime(a):
        i = 1
        if a == 2 or a == 3:
            return True
        if a % 2 == 0:
            return False

        while i * i <= a:
            i += 2
            if a % i == 0:
                return False
            else:
                continue
        return True

    list_of_primes = []
    prime = 0
    i = 1
    while i < n:
        i += 1
        if is_prime(i):
            prime = i
            list_of_primes.append(prime)
    print(list_of_primes)

    print(sum(list_of_primes))


solution(2000000)
