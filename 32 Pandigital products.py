'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''


def solution():
    from itertools import permutations

    list_of_numbers = [x for x in range(1, 10)]
    products = set()
    for i in permutations(list_of_numbers):
        # 00*000=0000
        if (i[0]*10 + i[1]) * (i[2]*100 + i[3]*10 + i[4]) == (i[5]*1000 + i[6]*100 + i[7]*10 + i[8]):
            print(i)
            products.add(i[5] * 1000 + i[6] * 100 + i[7] * 10 + i[8])
        # 0*0000=0000
        if (i[0]) * (i[1] * 1000 + i[2] * 100 + i[3]*10 + i[4]) == (i[5] * 1000 + i[6] * 100 + i[7] * 10 + i[8]):
            print(i)
            products.add(i[5] * 1000 + i[6] * 100 + i[7] * 10 + i[8])

    print(sum(products))

solution()

