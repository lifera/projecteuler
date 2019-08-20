'''

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

# 1 way to make 1
# 2 ways to make 2
# 4 ways to make 5
# 10  5 5  2 2 2 2 2   1 1 1 1 1 1 1 1 1 1    2 2 2 2 1 1   2221111   22111111  211111111 5221 52111 511111
# 8  11111111 2222  22211 221111 2111111 521 5111
#
#
#
def solution():
    coins = [100, 50, 20, 10, 5, 2, 1]
    different_ways = 0

    rest = 200
    for a1 in range(0, rest+1, 200):
        rest = 200 - a1
        for a2 in range(0, rest+1, 100):
            rest = 200 - a1 - a2
            for a3 in range(0, rest+1, 50):
                rest = 200 - a1 - a2 - a3
                for a4 in range(0, rest+1, 20):
                    rest = 200 - a1 - a2 - a3 - a4
                    for a5 in range(0, rest+1, 10):
                        rest = 200 - a1 - a2 - a3 - a4 - a5
                        for a6 in range(0, rest+1, 5):
                            rest = 200 - a1 - a2 - a3 - a4 - a5 - a6
                            for a7 in range(0, rest+1, 2):
                                a = 200 - a1 - a2 - a3 - a4 - a5 - a6 - a7
                                print(a)
                                if a >= 0:
                                    different_ways += 1


    print(different_ways)


solution()
