'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''


from math import sqrt


def find_sides(p:int) ->list:
    sides = []
    for a in range(p//2):
        for b in range(a, p//2):
            c = sqrt(a*a + b*b)
            if c.is_integer() and a+b+c == p:
                sides.append((a, b, int(c)))
    return sides


def main():
    sides_with_max_solutions = []
    max_solutions = 0
    for p in range(1001):
        solutions = find_sides(p)

        if len(solutions) > max_solutions:
            max_solutions = len(solutions)
            sides_with_max_solutions = solutions
            answer = p

    print(f'While p = {answer}: '
          f'Solutions : {sides_with_max_solutions} , len = {max_solutions}')


if __name__ == '__main__':
    main()