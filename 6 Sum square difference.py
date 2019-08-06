'''

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def solution(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n+1):

        sum_of_squares += i * i

        square_of_sum += i

    square_of_sum = square_of_sum * square_of_sum
    print(f'square_of_sum = {square_of_sum}, sum_of_squares = {sum_of_squares}')
    print(f'square_of_sum - sum_of_squares = {square_of_sum - sum_of_squares}')

solution(100)