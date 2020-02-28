'''

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

'''


def solution():
    from itertools import permutations
    numbers_with_property = []
    for i in permutations([0,1,2,3,4,5,6,7,8,9]):
        numb = ''
        for numb_temp in i:
            numb += str(numb_temp)

        cond234 = int(numb[1] + numb[2] + numb[3])
        cond345 = int(numb[2] + numb[3] + numb[4])
        cond456 = int(numb[3] + numb[4] + numb[5])
        cond567 = int(numb[4] + numb[5] + numb[6])
        cond678 = int(numb[5] + numb[6] + numb[7])
        cond789 = int(numb[6] + numb[7] + numb[8])
        cond8910 = int(numb[7] + numb[8] + numb[9])

        if cond234 % 2 == 0 \
            and cond345 % 3 == 0 and cond456 % 5 == 0\
            and cond567 % 7 == 0 and cond678 % 11 == 0 and cond789 % 13 == 0\
            and cond8910 % 17 == 0:
            numbers_with_property.append(numb)
    print(sum(map(int, numbers_with_property)))


if __name__ == '__main__':
    solution()

