'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def solution(n):
    i = 0
    prime_numbers = []
    while True:
        i += 1
        a = 1
        while a * a <= i:
            a += 1
            if i % a != 0:
                continue
            else:
                break
        else:
            prime_numbers.append(i)

        print(len(prime_numbers))
        if len(prime_numbers) >= n+1:
            print(prime_numbers[n])
            break

print(solution(10001))