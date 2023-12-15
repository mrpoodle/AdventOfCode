### for day 14
import re, sys
from tqdm import tqdm

def read_input(input_file):
    # . operational
    # # damaged
    # ? unknown
    lines = [line.strip("\n") for line in open(input_file)]
    springs = []
    for line in lines:
        status, groups = line.split(" ")
        springs.append([status, [int(i) for i in groups.split(",")]])

    return springs

def check_status(new_status, status, groups):
    possible_groups = [len(group) for group in re.split("\.+", new_status) if group != ""]
    # print(status, groups, possible_groups)
    if len(possible_groups) > len(groups):
        return False
    for i, group in enumerate(possible_groups):
        if i == len(possible_groups)-1:
            if group < groups[i] and new_status[-1] == "#":
                continue
            elif group == groups[i]:
                continue
            else:
                return False
        if group != groups[i]:
            return False
    rest = groups[len(possible_groups):]
    length_rest = sum(rest) + len(rest)-1
    if length_rest + len(new_status) > len(status):
        return False
    return True

def test_groups(status, groups):
    possible_status = [""]
    for char in tqdm(status, desc=" char", position=1, leave=False):
        sys.stderr.flush()
        if char == "." or char == "#":
            possible_status = [s+char for s in possible_status if check_status(s+char, status, groups)]
        elif char == "?":
            possible_status = [s+"." for s in possible_status if check_status(s+".", status, groups)] + [s+"#" for s in possible_status if check_status(s+"#", status, groups)]
    counter = 0
    for s in tqdm(possible_status, desc=" chek", position=1, leave=False):
        possible_groups = [len(group) for group in re.split("\.+", s) if group != ""]
        if possible_groups == groups:
            counter += 1
    return counter


def part_1(input_file):
    # read data
    springs = read_input(input_file)

    out = 0
    for status, groups in springs:  # tqdm(springs):
        out+= test_groups(status, groups)
    return out

def part_2(input_file):
    # read data
    springs = read_input(input_file)

    out = 0
    for status, groups in tqdm(springs, desc=" line", position=0):
        status = (status+"?")*5
        out+= test_groups(status[:-1], groups*5)
    print(" "*40)
    return out

