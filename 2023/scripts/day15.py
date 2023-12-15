### for day 00

def read_input(input_file):
    data = [line.strip("\n") for line in open(input_file)][0]

    strings = data.split(",")

    return strings

def holiday_hasher(string):
    current_value = 0
    for char in string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

def part_1(input_file):
    # read data
    strings = read_input(input_file)

    out = 0
    for string in strings:
        out += holiday_hasher(string)
    return out


def add_lense(string, lense_boxes):
    operator = "="
    box_id = 0
    label, focal = string.split(operator)
    box_id = holiday_hasher(label)
    for i, lense in enumerate(lense_boxes[box_id]):
        if lense[0] == label:
            lense_boxes[box_id][i][1] = int(focal)
            return lense_boxes
    lense_boxes[holiday_hasher(label)].append([label, int(focal)])
    return lense_boxes


def remove_lense(string, lense_boxes):
    operator = "-"
    label = string.strip(operator)
    box_id = holiday_hasher(label)
    lense_boxes[box_id] = list(filter(lambda x: x[0] != label, lense_boxes[box_id]))
    return lense_boxes

def focal_power(lense_boxes):
    power = 0
    for i, box in enumerate(lense_boxes):
        if len(box) == 0:
            continue
        for j, lense in enumerate(box):
            power += (i+1) * (j+1) * lense[1]
    return power

def part_2(input_file):
    # read data
    strings = read_input(input_file)

    lense_boxes = [[] for _ in range(256)]
    for string in strings:
        if "-" in string:
            lense_boxes = remove_lense(string, lense_boxes)
        elif "=" in string:
            lense_boxes = add_lense(string, lense_boxes)
    return focal_power(lense_boxes)
