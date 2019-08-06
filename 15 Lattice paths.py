'''

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''


def solution(n):
    # Using binomial coefficient
    last = 1
    for i in range(1, n+1):
        last *= (2*n - i + 1) / i
    return last


def official_solution(n):
    # Using binomial coefficient
    last = 1
    for i in range(1, n+1):
        last *= (n + i) / i
    return last


print(solution(20))
print(official_solution(20))
