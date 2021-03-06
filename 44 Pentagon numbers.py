'''

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which
their sum and difference are pentagonal and D = |Pk − Pj| is minimised;
what is the value of D?

'''


def solution():
    def gen_pentagonal_numbers(n: int) -> list:
        pent_number = 1
        pentagonal_numbers = []
        i = 1
        while pent_number < n:
            i += 1
            pentagonal_numbers.append(pent_number)
            pent_number = i * (3 * i - 1) // 2
        return pentagonal_numbers

    pentagonal_numbers = gen_pentagonal_numbers(10000000)
    print(pentagonal_numbers)
    min_diff = 100000000
    for k in pentagonal_numbers:
        for j in pentagonal_numbers:
            if k + j in pentagonal_numbers and int(abs(k - j)) in pentagonal_numbers:
                min_diff = min(min_diff, abs(k - j))
    print(min_diff)


if __name__ == '__main__':
    solution()