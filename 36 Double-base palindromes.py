'''

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def solution(n):
    answers = []
    for i in range(1, n):
        if str(i)[-1::-1] == str(i):
            binary_str = str(bin(i))[2:]
            if binary_str[-1::-1] == binary_str:
                answers.append(i)
    print(answers)
    print(sum(answers))

if __name__ == '__main__':
    solution(1000000)
