'''

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


def solution():
    from itertools import permutations
    digits = '0123456789'
    for index, a in enumerate(permutations(digits)):
        if index+1 == 10**6:
            print(a)


def lexicographic_order(n):
    import math
    start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    order = []
    for i in range(9, -1, -1):
        shifts = int(n / math.factorial(i))
        n = n - shifts * math.factorial(i)
        order.append(start.pop(shifts))

    return int(''.join([str(i) for i in order]))

solution()

print(lexicographic_order(10**6-1))
