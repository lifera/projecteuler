'''

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def solution():
    def is_pandigital(s:str)->bool:
        q = set(s)
        if len(q) == 9 and '0' not in q:
            return True

        return False
    answer = 0
    for number in range(2, 100000):
        concatenated_product = ''
        for i in range(1, 10):
            concatenated_product = concatenated_product + str(i*number)
            if len(concatenated_product) < 9:
                continue
            elif len(concatenated_product) == 9:

                if is_pandigital(concatenated_product):
                    answer = max(answer, int(concatenated_product))
            else:
                break
    print(f'Max pandigital = {answer}')

solution()
