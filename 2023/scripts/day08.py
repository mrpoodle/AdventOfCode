### for day 08

from itertools import cycle
import math


def read_input(input_file):
    lines = [[element.strip(")(,") for element in line.strip("\n").split(" ")] for line in open(input_file)]
    lines = filter(lambda x: x[0].startswith("#") == False , lines)
    instructions = None
    map = {}
    for line in lines:
        if not instructions:
            instructions = line[0]
            continue
        if line[0] == "":
            continue
        map[line[0]] = (line[2], line[3])

    return map, instructions

def part_1(input_file):
    map, instructions = read_input(input_file)

    current = "AAA"
    steps = 0
    for i in cycle(instructions):
        if current == "ZZZ":
            break
        steps += 1
        if i == "L":
            current = map[current][0]
        elif i == "R":
            current = map[current][1]
    return steps

def part_2(input_file):
    map, instructions = read_input(input_file)

    current = [key for key in map.keys() if key[-1] == "A"]
    all_loops = []
    for c in current:
        loops = []
        steps = 0
        last= 0
        for i in cycle(instructions):
            if c.endswith("Z"):
                if steps-last in loops:
                    break
                loops.append(steps-last)
                last = steps
            steps += 1
            if i == "L":
                c = map[c][0]
            elif i == "R":
                c = map[c][1]
        all_loops += list(set(loops))
    return math.lcm(*all_loops)
