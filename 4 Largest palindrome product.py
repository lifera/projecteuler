''''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def solution():
    l = []
    for i in range(100, 999):
        for a in range(100, 999):
            p = a * i
            p = str(p)
            if p[0] == p[-1] and p[1] == p[-2] and p[2] == p[-3]:
                l.append(int(p))
    print(max(l))

def reverse(n):
    reversed = 0
    while n > 1:
        reversed = 10*reversed + n % 10
        n = n//10
        print(n, reversed)
    return reversed

solution()
print(reverse(49616518))