'''

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''


def solution():
    from math import factorial
    result = 0
    factorials = {q: factorial(q) for q in range(10)}
    print(factorials)
    for i in range(3, 10**6):
        sum_of_factorials = 0
        for a in str(i):
            sum_of_factorials += factorials[int(a)]
        if sum_of_factorials == i:
            print(i)
            result += i
    print(result)


solution()
