### for day 18


def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    data = []
    for line in lines:
        direction, length, hex_code = line.split(" ")
        length = int(length)
        hex_code = hex_code.strip("()")
        data.append([direction, length, hex_code])
    ## Do whatever with the lines

    return data

def find_corners_1(data):
    corners = [(0,0)]
    for instruction in data:
        direction, length, _ = instruction
        if direction == "R":
            corners.append((corners[-1][0]+length, corners[-1][1]))
        elif direction == "L":
            corners.append((corners[-1][0]-length, corners[-1][1]))
        elif direction == "U":
            corners.append((corners[-1][0], corners[-1][1]+length))
        elif direction == "D":
            corners.append((corners[-1][0], corners[-1][1]-length))
    return corners

def find_corners_2(data):
    corners = [(0,0)]
    new_data = []
    for instruction in data:
        hex_code = instruction[2]
        length = int(hex_code[1:-1], 16)
        direction = int(hex_code[-1])
        if direction == 0:
            # direction = "R"
            corners.append((corners[-1][0]+length, corners[-1][1]))
        elif direction == 2:
            # direction = "L"
            corners.append((corners[-1][0]-length, corners[-1][1]))
        elif direction == 3:
            # direction = "U"
            corners.append((corners[-1][0], corners[-1][1]+length))
        elif direction == 1:
            # direction = "D"
            corners.append((corners[-1][0], corners[-1][1]-length))
        new_data.append([direction, length, ""])
    return corners, new_data

def calculate_pool(data, corners):
    # TO USE: 1/2 SIGMA(x_i*(y_i+1 - y_i-1)
    out = 0
    for i, corner in enumerate(corners):
        # sum(x_i*(y_i+1 - y_i-1)
        out += corner[1]*(corners[(i+1)%len(corners)][0]-corners[i-1][0])

    out = abs(out)/2  # according to the formula: 1/2 sum(x_i*(y_i+1 - y_i-1)
    out += sum([x[1] for x in data])/2  # outer half of the path
    out += 1  # four outer corners of outer half
    return int(out)

def part_1(input_file):
    data = read_input(input_file)

    corners = find_corners_1(data)
    if not corners[-1] == corners[0]:
        raise Exception("The path doesn't end where it started")
    corners.pop()

    return calculate_pool(data, corners)

def part_2(input_file):
    data = read_input(input_file)

    corners, new_data = find_corners_2(data)
    if not corners[-1] == corners[0]:
        raise Exception("The path doesn't end where it started")
    corners.pop()

    return calculate_pool(new_data, corners)

