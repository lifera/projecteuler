'''

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word
a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''


def gen_triangle_numbers(max_number: int) -> list:
    triangle_numbers = []
    i = 0
    triangle_number = 1
    while triangle_number < max_number:
        i += 1
        triangle_numbers.append(triangle_number)
        triangle_number = (i * (i + 1)) // 2

    return triangle_numbers


def solution():
    def get_word_number(s: str) -> int:
        number = 0
        for a in s:
            number += ord(a) - 64
        return number

    answer = 0
    with open('p042_words.txt') as f:
        words = f.read()

    words = words.split(',')
    max_len_of_word = max([len(x) for x in words]) - 2
    max_triangle_word_number = max_len_of_word*26

    triangle_numbers = gen_triangle_numbers(max_triangle_word_number)
    for word in words:
        if get_word_number(word[1:-1]) in triangle_numbers:
            answer += 1

    print(answer)


    # print(words)

if __name__ == '__main__':
    solution()