from itertools import product
from .utils import get_file


def load_data():
    lines = get_file("inputs/day4.txt")
    data = []
    for line in lines:
        data.append(line.strip())
    return data

def xmas_search():
    lines = load_data()
    for y, line in enumerate(lines):
        for x, letter in enumerate(line):
            if letter == 'X':
                for direction in [x for x in product((0, 3, -3), repeat=2)]:
                    print(letter)
            continue
    return lines