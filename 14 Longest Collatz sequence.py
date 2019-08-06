'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def brute_force_solution(n):
    max_steps = 1
    for i in range(2, n):
        a = i
        print(a)
        steps = 1
        while a > 1:
            if a % 2 == 0:
                a = a/2
            else:
                a = 3*a + 1
            steps += 1
        if steps > max_steps:
            max_steps = steps
            result = i

    return result, max_steps


def good_solution(n):

    def count_steps(q):

        if steps_for_number.get(q) is not None:
            return steps_for_number.get(q)
        if q == 1: return 1
        if q % 2 == 0:
            steps_for_number[q] = count_steps(q // 2) + 1
        else:
            steps_for_number[q] = count_steps((3 * q + 1) / 2) + 2

        return steps_for_number[q]

    max_i = 1
    max_steps = 1
    steps_for_number = dict()

    for i in range(n // 2, n):
        steps = count_steps(i)
        if steps > max_steps:
            max_steps = steps
            max_i = i
    return max_i, max_steps


print(good_solution(10**6))