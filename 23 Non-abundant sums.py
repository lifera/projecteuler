'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


def solution():
    def get_sum_of_divisors(n):
        i = 1
        result = 0

        while i * i < n:
            if n % i == 0:
                result += i + n // i
            i += 1

        if i*i == n:
            result += i

        return result - n

    # abundant numbers
    abundant_numbers = []
    for a in range(1, 28124):
        if a < get_sum_of_divisors(a):
            abundant_numbers.append(a)

    sums = set()
    for a in abundant_numbers:
        for b in abundant_numbers:
            sums.add(a+b)

    all_numbers = set(range(1, 28124))
    result = all_numbers.difference(sums)
    print('all_numbers.difference(sums)', result)
    print('result', sum(result))


solution()
