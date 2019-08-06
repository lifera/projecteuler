'''

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''


def solution():
    answer = 0
    a = str(2**1000)
    print(a)
    for b in a:
        answer += int(b)
    print(answer)

solution()
print(map(int,str(2**1000)))