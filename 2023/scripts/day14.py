### for day 14
from tqdm import tqdm

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    data = reversed([list(i) for i in zip(*lines)])
    return list(data)


def rearrange(data):
    for d in data:
        d = "".join(d)
        spaces = d.split("#")
        spaces = ["".join(sorted(space, reverse=True)) for space in spaces]
        arranged = "#".join(spaces)
        yield arranged

def part_1(input_file):
    # read data
    data = read_input(input_file)
    # data[0][0] is NE

    out = 0
    for arranged in rearrange(data):
        for i, field in enumerate(arranged):
            if field == "O":
                out += len(arranged)-i
    return out

def rotate_90_clockwise(data):
    return [list(reversed(i)) for i in zip(*data)]

def print_north(data):
    print_west(rotate_90_clockwise(data))

def print_east(data):
    print_north(rotate_90_clockwise(data))

def print_south(data):
    print_east(rotate_90_clockwise(data))

def print_west(data):
    for line in data:
        print("".join(line))
    print()

def print_north_up(data, dir):
    if dir == "A":
        print_north(data)
    elif dir == "<":
        print_west(data)
    elif dir == "V":
        print_south(data)
    elif dir == ">":
        print_east(data)

def rearrangment_cycle(data):
    #print(". initial")
    #print_north(data)
    for dir in ["A", "<", "V", ">"]:
        data = list(rearrange(data))
        #print(dir)
        #print_north_up(data, dir)
        data = rotate_90_clockwise(data)
    return data


def part_2(input_file):
    # read data
    data = read_input(input_file)
    # data[0][0] is NE

    previous = []
    out = 0
    loads = []
    cycles = 1000000000
    for i in range(cycles):
        if data in previous:
            # print(f"cycle found at {i-1} from {previous.index(data)}")
            # print(loop)
            # print(cycles-1-(previous.index(data)))
            # print((cycles-1-previous.index(data))%len(loop)+1)
            # print(loop[(cycles-1-previous.index(data))%(len(loop)+1)])
            loop = loads[previous.index(data):-1]
            # A B C D E F "G" H I J "G" H I ....
            out = loop[(cycles-1-previous.index(data))%(len(loop)+1)]
            break
        previous.append(data)
        data = list(rearrangment_cycle(data))

        load = 0
        for d in data:
            for j, field in enumerate(d):
                if field == "O":
                    load += len(d)-j
        loads.append(load)
    return out

