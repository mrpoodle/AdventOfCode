### for day 11

from itertools import combinations


def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    ## Do whatever with the lines

    return lines

def expand(lines):
    # duplicate empty lines
    new_lines = []
    for i, line in enumerate(lines):
        if set(line) == {"."}:
            new_lines.append(line)
        new_lines.append(line)

    # turn lines
    turned_lines = ["" for x in new_lines[0]]
    for i, line in enumerate(new_lines):
        for j, char in enumerate(line):
            turned_lines[j] += char

    # duplicate empty lines and turn
    expanded_lines =  ["" for x in turned_lines[0]]
    for i, line in enumerate(turned_lines):
        if set(line) == {"."}:
            for j, char in enumerate(line):
                expanded_lines[j] += char*2
        else:
            for j, char in enumerate(line):
                expanded_lines[j] += char
    return expanded_lines

def part_1(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    lines = expand(lines)

    galaxies = []
    for i, line in enumerate(lines):
        for char in line:
            if char == "#":
                galaxies.append((i, line.index(char)))
    dist = 0
    paths = 0
    for pair in combinations(galaxies, 2):
        paths += 1
        dist += abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1])
    print(paths)
    return dist

def part_2(input_file):
    # read data
    data = read_input(input_file)

    out = "Not implemented yet"
    # process and compute out
    return out
