import os
from ast import literal_eval as parse

DAY = 18
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


def flat(some_list):
    depths = []
    for item in some_list:
        if isinstance(item, list):
            depths.append(flat(item))
    if len(depths) > 0:
        return 1 + max(depths)
    return 1


def split(number):
    if number < 10:
        return number
    return [int(number/2), int((number+1)/2)]


def combine(number, second_part):
    if isinstance(second_part, int):
        try:
            return split(number + second_part)
        except:
            print(number, second_part)

    if isinstance(second_part, list):
        return [combine(number, second_part[0]), second_part[1]]


def validate(number, level=1):
    if level > 4:
        if isinstance(number, list):
            return (
                validate(number, level=0)
            )
        return (
            0,
            split(number),
            0
        )
    if isinstance(number, list):
        n_1 = validate(number[0], level=level+1)
        n_2 = validate(number[1], level=level+1)
        print(n_1, n_2)
        return (
            n_1[0],
            [combine(n_2[0], n_1[1]), combine(n_1[2], n_2[1])],
            n_2[2]
        )
    return (
        0,
        split(number),
        0
    )


def addition(number):
    a, number, e = validate(number)
    print(number)
    if flat(number) > 4:
        return addition(number)
    return number


def main_1(input):
    sum = []
    with open(input) as file:
        for line in file:
            line = parse(line.strip())
            if sum == []:
                sum = line
                continue
            print(flat([sum, line]))
            print([sum, line])
            sum = addition([sum, line])
    print(sum)
    return 0


def main_2(input):
    # TODO
    with open(input) as file:
        for line in file:
            pass  # TODO
    return 0


print(main_1(TESTING))
