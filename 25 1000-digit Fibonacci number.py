'''

The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''


def fibonacci_digits(n):
    fib_numbers = dict()

    def fib(x):
        if x == 1 or x == 2:
            return 1
        if fib_numbers.get(x):
            return fib_numbers.get(x)
        fib_numbers[x] = fib(x-1) + fib(x-2)
        return fib_numbers[x]
    a = 1
    while len(str(fib(a))) < n:
        a += 1
    print(a)


fibonacci_digits(1000)