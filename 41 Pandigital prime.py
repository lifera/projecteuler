'''


We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True


def pandigital_prime():
    from itertools import permutations
    numbers = [x for x in range(1, 10)]
    max_prime = 0
    for number_len in range(9, 1, -1):
        for permutation in permutations(numbers[0:number_len]):
            int_to_check = ''
            for number in permutation:
                int_to_check = int(str(int_to_check) + (str(number)))
            if is_prime(int_to_check):
                max_prime = max(max_prime, int_to_check)
    print(max_prime)


if __name__ == '__main__':
    pandigital_prime()