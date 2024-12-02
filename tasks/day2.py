import re
from copy import copy
from itertools import pairwise
from .utils import NUMBERS_PATTERN, get_file

def load_data():
    lines = get_file("inputs/day2.txt")
    data = []
    for line in lines:
        data.append([int(x) for x in re.findall(NUMBERS_PATTERN, line)])
    return data

def is_safe(report) -> bool:
    asc = False
    desc = False
    for pair in pairwise(report):
        diff = pair[0] - pair[1]
        if not (3 >= abs(diff) >= 1):
            asc = desc = True
            return False
        if diff > 0:
            desc = True
        elif diff < 0:
            asc = True
        else:
            asc = desc = True
    if asc == desc:
        return False
    return True 

def safe_reports(with_dampener=False):
    data = load_data()
    safe = 0

    for report in data:
        if is_safe(report=report):
            safe += 1
        elif with_dampener:
            for idx, _ in enumerate(report):
                dampened = copy(report)
                del(dampened[idx])
                if is_safe(dampened):
                    safe += 1
                    break
    return safe