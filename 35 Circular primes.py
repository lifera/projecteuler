'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''


def circulate(n: int) -> list:
    # 179 -> [179, 917, 791]
    str_n = str(n)
    circulated_numbs = []
    len_n = len(str_n)
    for index, numb in enumerate(str_n):
        if index == 0:
            circ_number = n
        elif index == len_n:
            circ_number = int(numb + str_n[0:index])
        else:
            circ_number = int(numb + str_n[index + 1:] + str_n[0:index])
        circulated_numbs.append(circ_number)

    return circulated_numbs

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    for q in range(3, int(n**.5)+1, 2):
        if n % q == 0:
            return False
    return True

def solution():

    answer = set()
    answer.add(2)
    for i in range(3, 1000000, 2):
        if is_prime(i):
            if i < 10:
                answer.add(i)
            else:
                prime = True
                for numb in circulate(i):
                    if not is_prime(numb):
                        prime = False
                if prime:
                    answer.add(i)
    print(answer)
    print(len(answer))


if __name__=='__main__':
    solution()


