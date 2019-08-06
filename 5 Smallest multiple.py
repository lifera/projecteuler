'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def solution():
    a = 2520
    b = 1
    list_to_divide = [16, 18, 14, 11, 20, 12, 13, 15, 17, 19]
    # lst_sum = 2*2*2*2*2*3*3*2*7*11*2*2*5*2*2*3*13*3*5*17*19
    while a >= 0:
        a += 1
        print(a)
        for i in list_to_divide:
            if a % i == 0:
                continue
            else:
                break
        else:
            break
    # for i in list_to_divide:
    #     b *= i
    # print(b)
    # print(lst_sum)
    # a =
    print(a)


solution()
