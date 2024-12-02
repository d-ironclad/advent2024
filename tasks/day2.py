import re
from itertools import pairwise
from .utils import NUMBERS_PATTERN, get_file

def load_data():
    lines = get_file("inputs/day2.txt")
    data = []
    for line in lines:
        data.append([int(x) for x in re.findall(NUMBERS_PATTERN, line)])
    return data

def safe_reports(with_dampener=False):
    data = load_data()
    safe = 0

    for report in data:
        asc = False
        desc = False
        for pair in pairwise(report):
            diff = pair[0] - pair[1]
            if not (3 >= abs(diff) >= 1):
                asc = desc = True
                break

            if diff > 0:
                desc = True
            elif diff < 0:
                asc = True
            else:
                asc = desc = True
        if asc != desc:
            safe +=1 
    return safe