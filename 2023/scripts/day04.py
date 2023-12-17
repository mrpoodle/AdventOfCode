### for day 00

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    ## Do whatever with the lines

    return lines

def part_1(input_file):
    lines = [[set([int(number)
            for number in numbers.split()])
                for numbers in line.strip("\n").split(":")[1].strip(" ").split(" | ")]
                    for line in open(input_file)]
    out = 0
    for line in lines:
        points = 2**(len(line[0] & line[1])-1)
        if points >= 1:
            out += points
    return out

def part_2(input_file):
    lines = [[set([int(number)
            for number in numbers.split()])
                for numbers in line.strip("\n").split(":")[1].strip(" ").split(" | ")]
                    for line in open(input_file)]

    cards = [1 for x in lines]
    print(cards)
    for i, line in enumerate(lines):
        points = len(line[0] & line[1])
        for x in range(points):
            try:
                cards[i+x+1] += cards[i]
            except IndexError:
                pass
    print(cards)
    out = sum(cards)
    return out
