import re

from .utils import NUMBERS_PATTERN, get_file

def load_data():
    lines = get_file("inputs/day3.txt")
    data = []
    for line in lines:
        data.append(line)
    return data

def mull_it():
    data = load_data()
    result = 0
    for line in data:
        for match in re.findall(r"mul\((\d+),(\d+)\)", line):
            print(match)
            result += int(match[0]) * int(match[1])
    return result