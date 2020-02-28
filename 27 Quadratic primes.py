'''Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41

is clearly divisible by 41.

The incredible formula n2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.'''


def solution():
    def check_prime(x):
        for i in range(2, abs(x)):
            if x % i == 0:
                return False

        return True

    max_number_of_primes = 0

    for a in range(-999, 1000, 1):
        for b in range(-1000, 1001, 1):
            n = 0
            while True:
                if check_prime((n*n) + (a*n) + b):
                    n += 1
                    print(f'a={a}, b={b}, n={n}')
                else:
                    break

            if max_number_of_primes < n:
                max_number_of_primes = n
                coef_a = a
                coef_b = b

    print(f'max_number_of_primes = {max_number_of_primes}, a = {coef_a}, b = {coef_b}, a*b = {coef_a*coef_b}')


print(solution())