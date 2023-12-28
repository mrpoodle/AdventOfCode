### for day 09

def read_input(input_file):
    lines = [[int(value) for value in line.strip("\n").split()] for line in open(input_file)]
    def find_next(values):
        new_values = [0 for x in range(len(values)-1)]
        prev = values[0]
        value = 0
        for i, value in enumerate(values[1:]):
            new_values[i] = value-prev
            prev = value
            if i == len(values)-2:
                if set(new_values) == {0}:
                    return values[0], values[-1]
                else:
                    front, end = find_next(new_values)
                    return values[0]-front, end+values[-1]
    out = [0, 0]
    for line in lines:
        front, end = find_next(line)
        out[0] += front
        out[1] += end
    return out

def part_1(input_file):
    return read_input(input_file)[1]

def part_2(input_file):
    return read_input(input_file)[0]