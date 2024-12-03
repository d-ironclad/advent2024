import re

from .utils import NUMBERS_PATTERN, get_file

def load_data():
    lines = get_file("inputs/day3.txt")
    data = []
    for line in lines:
        data.append(line)
    return data

def mull_it(no_fix=True):
    pattern = r"mul\((\d+),(\d+)\)" if no_fix else r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))"
    data = load_data()
    result = 0
    do = True
    for line in data:
        if no_fix:
            for match in re.findall(pattern, line):
                print(match)
                result += int(match[0]) * int(match[1])
        else:
            for match in re.finditer(pattern, line):
                print(match)
                if match.group(3):
                    do = False
                elif match.group(4):
                    do = True
                elif match.group(1) and match.group(2) and do:
                    result += (int(match.group(1)) * int(match.group(2)))
    return result