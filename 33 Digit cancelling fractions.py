'''

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''


def solution():
    numerator = denominator = 1
    for a in range(11, 100):
        for b in range(a+1, 100):
            for char in str(a):
                if char in str(b):
                    fraction = a / b

                    if str(a).replace(char, '') == '':
                        a1 = int(str(a)[0])
                    else:
                        a1 = int(str(a).replace(char, ''))

                    if str(b).replace(char, '') == '':
                        b1 = int(str(b)[0])
                    else:
                        b1 = int(str(b).replace(char, ''))

                    if b % 10 == 0:
                        continue
                    fraction_to_compare = a1 / b1

                    if fraction == fraction_to_compare:
                        print(f'{a}/{b}')
                        numerator *= a1
                        denominator *= b1
    print(denominator/numerator)


solution()
