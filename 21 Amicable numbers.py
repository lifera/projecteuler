'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''


def solution():
    a = 1
    amicable_numbers = []
    while a < 10000:
        a += 1
        list_of_a_divisors = []
        for b in range(1, a):
            if a % b == 0:
                list_of_a_divisors.append(b)
        sum_of_a_divisors = sum(list_of_a_divisors)

        list_of_b_divisors = []
        for b in range(1, sum_of_a_divisors):
            if sum_of_a_divisors % b == 0:
                list_of_b_divisors.append(b)
        sum_of_b_divisors = sum(list_of_b_divisors)
        if sum_of_b_divisors == a and sum_of_a_divisors != sum_of_b_divisors:
            amicable_numbers.append([sum_of_a_divisors, sum_of_b_divisors])
    print(amicable_numbers)
    print(sum([z[0] for z in amicable_numbers]))


solution()
