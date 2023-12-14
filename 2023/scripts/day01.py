### for day 00

numbers = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}


def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    ## Do whatever with the lines

    return lines


def process_line(l):
    first = None
    last = None
    for x in l:
        if x.isdigit():
            last = x
            if first:
                continue
            first=x
    return int(first+last)


def part_1(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    out = 0
    for line in lines:
        out += process_line(line)
    return out


def part_2(input_file):
    lines = read_input(input_file)
    out = 0
    for l in lines:
        for x in numbers:
            l = l.replace(x, numbers[x])
        out += process_line(l)
    return out
