'''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''


def solution():
    with open('p022_names.txt') as f:
        names = f.read()
    names = names.replace('"', '').split(',')
    letter_number = dict()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    for i, a in enumerate(alphabet):
        letter_number[a] = i+1
    names.sort()
    print(names)
    print(letter_number)
    total_name_scores= 0
    for index, name in enumerate(names):
        name_score = 0
        for i in name:
            name_score += letter_number[i]
        total_name_scores += name_score * (index + 1)
    print(total_name_scores)

solution()
