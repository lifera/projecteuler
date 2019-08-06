'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def solution(n):
    i = 0
    candidate = 0
    primes = []
    while i * i <= n:
        i += 1
        if n % i == 0:
            candidate = i
            a = 1
            while a * a < candidate:
                a += 1
                if candidate % a == 0:
                    break
            else:
                primes.append(candidate)
    print(max(primes))

solution(600851475143)
solution(13195)
