def day01(filename):
    def solution(max_elves):
        maxima = [0] * max_elves

        def check_max(counter):
            for x in range(max_elves):
                if counter > maxima[x]:
                    maxima.insert(x, counter)
                    maxima.pop()
                    break

        with open(filename) as f:
            counter = 0
            for line in f:
                if line == "\n":
                    check_max(counter)
                    counter = 0
                    continue
                counter += int(line)
        check_max(counter)
        return sum(maxima)

    print(f"day 01, part 1: {solution(1)}")
    print(f"day 01, part 2: {solution(3)}")


def day02(filename):

    values_1 = {
        #          rock        paper       scissors   opponent
        "A": {"X": 3 + 1, "Y": 6 + 2, "Z": 0 + 3},  # rock - 1
        "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},  # paper - 2
        "C": {"X": 6 + 1, "Y": 0 + 2, "Z": 3 + 3}   # scissors - 3
    }

    values_2 = {
        #          loose       draw        win        opponent
        "A": {"X": 0 + 3, "Y": 3 + 1, "Z": 6 + 2},  # rock - 1
        "B": {"X": 0 + 1, "Y": 3 + 2, "Z": 6 + 3},  # paper - 2
        "C": {"X": 0 + 2, "Y": 3 + 3, "Z": 6 + 1}   # scissors - 3
    }

    def solution(values):
        score = 0
        with open(filename) as f:
            for line in f:
                line = line.strip("\n")
                score += values[line[0]][line[-1]]
        return score

    print(f"day 02, part 1: {solution(values_1)}")
    print(f"day 02, part 2: {solution(values_2)}")


def day03(filename):

    def map2number(letter):
        if letter.isupper():
            return ord(letter) - 38
        else:
            return ord(letter) - 96

    def get_priority_1(line):
        first_half = line[:int(len(line)/2)]
        second_half = line[int(len(line)/2):]
        common = list(set(first_half).intersection(second_half))
        return map2number(common[0])

    def get_priority_2(lines):
        common = list(set(lines[0]).intersection(lines[1]))
        common = list(set(common).intersection(lines[2]))
        return map2number(common[0])

    def solution_1():
        counter = 0
        with open(filename) as f:
            for line in f:
                line = line.strip("\n")
                counter += get_priority_1(line)
        return counter

    def solution_2():
        counter = 0
        index = 0
        lines = ["", "", ""]
        with open(filename) as f:
            for line in f:
                lines[index] = line.strip("\n")
                if index == 2:
                    index = 0
                    counter += get_priority_2(lines)
                    continue
                index += 1
        return counter

    print(f"day 03, part 1: {solution_1()}")
    print(f"day 03, part 1: {solution_2()}")


def day04(filename):
    def make_set(range_string):
        start, end = range_string.split("-")
        range_set = set(range(int(start), int(end) + 1))
        return range_set

    counter_1 = 0
    counter_2 = 0
    with open(filename) as f:
        for line in f:
            a, b = line.strip("\n").split(",")
            a_range = make_set(a)
            b_range = make_set(b)
            if a_range.issubset(b_range) or b_range.issubset(a_range):
                counter_1 += 1
                counter_2 += 1
            elif a_range.intersection(b_range):
                counter_2 += 1

    print(f"day 04, part 1: {counter_1}")
    print(f"day 04, part 2: {counter_2}")


def day05(filename):
    def process(part):
        stacks = {}
        with open(filename) as f:
            for line in f:
                line = line.strip("\n")
                if line == "":
                    break
                for i, column in enumerate(range(1, len(line), 4)):
                    if not line[column].isupper():
                        continue
                    if i+1 in stacks:
                        stacks[i+1].insert(0, line[column])
                    else:
                        stacks[i+1] = [line[column]]
            # print(stacks)

            for line in f:
                words = line.strip("\n").split(" ")
                if words[0] != "move":
                    continue
                _n_ = int(words[1])
                _from_ = int(words[3])
                _to_ = int(words[5])
                if part == 1:
                    for _ in range(_n_):
                        stacks[_to_].append(stacks[_from_].pop())
                if part == 2:
                    stacks[_to_] += stacks[_from_][-_n_:]
                    del stacks[_from_][-_n_:]
            # print(stacks)

            return "".join([stacks[i+1][-1] for i in range(len(stacks))])

    print(f"day 05, part 1: {process(1)}")
    print(f"day 05, part 2: {process(2)}")


def day06(filename):
    with open(filename) as f:
        for line in f:
            window_1 = " " * 4
            window_2 = " " * 14
            for i, character in enumerate(line):
                window_1 = window_1[-3:] + character
                if " " not in window_1 and len(set(window_1)) == 4:
                    solution_1 = i+1
                    break
            for i, character in enumerate(line):
                window_2 = window_2[-13:] + character
                if " " not in window_2 and len(set(window_2)) == 14:
                    solution_2 = i+1
                    break

    print(f"day 06, part 1: {solution_1}")
    print(f"day 06, part 2: {solution_2}")


def day07(filename):
    from os import path
    from collections import defaultdict
    solution_1 = 0
    solution_2 = 0
    current_path = "/"
    dirs = defaultdict(list)
    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            if line[0] == "$":
                if line[2:4] == "cd":
                    if line[5:] == "..":
                        current_path = path.dirname(current_path)
                    else:
                        current_path = path.join(current_path, line[5:])
                if line[2:4] == "ls":
                    continue
            elif line[:3] == "dir":
                directory = path.join(current_path, line[4:])
                dirs[current_path].append(directory)
                dirs[directory]
            else:
                size, _ = line.split(" ")
                dirs[current_path].append(int(size))

    def get_size(key, dir_dict):
        sum = 0
        for value in dir_dict[key]:
            if isinstance(value, int):
                sum += value
            else:
                sum += get_size(value, dir_dict)
        return sum

    for key in dirs:
        dirs[key] = get_size(key, dirs)

    for key in dirs:
        if dirs[key] < 100000:
            solution_1 += dirs[key]

    # dirs_space = dirs["/"]
    # disk_space = 70000000
    # update_space = 30000000
    # free_space = disk_space - dirs_space
    # needed_space = update_space - free_space
    needed_space = 30000000 - (70000000 - dirs["/"])
    solution_2 = dirs["/"]
    for key in dirs:
        if dirs[key] > needed_space and dirs[key] < solution_2:
            solution_2 = dirs[key]

    print(f"day 07, part 1: {solution_1}")
    print(f"day 07, part 2: {solution_2}")


def day08(filename):
    def check_visibility(grid, x, y):
        line = grid[y]
        column = [grid[i][x] for i in range(0, len(grid))]
        value = grid[y][x]
        left = max(line[:x])
        right = max(line[x+1:])
        top = max(column[:y])
        bottom = max(column[y+1:])
        if min([left, right, top, bottom]) < value:
            return 1
        return 0

    def find_score(grid, x, y):
        line = grid[y]
        column = [grid[i][x] for i in range(0, len(grid))]
        value = grid[y][x]
        left, right = line[:x], line[x+1:]
        left.reverse()
        top, bottom = column[:y], column[y+1:]
        top.reverse()
        score = (
            get_sight(left, value) * get_sight(right, value) *
            get_sight(top, value) * get_sight(bottom, value)
            )
        return score

    def get_sight(trees, value):
        # sight = trees
        for i, v in enumerate(trees):
            if v >= value:
                return i+1

    solution_2 = 0
    treegrid = []
    with open(filename) as f:
        for line in f:
            treegrid.append(list(line.strip("\n")))

    width = len(treegrid[0])
    height = len(treegrid)
    solution_1 = 2*width + 2*height - 4  # remove corners, counted twice

    for x in range(1, width-1):
        for y in range(1, height-1):
            solution_1 += check_visibility(treegrid, x, y)

    for x in range(1, width-1):
        for y in range(1, height-1):
            score = find_score(treegrid, x, y)
            if score > solution_2:
                solution_2 = score

    print(f"day 08, part 1: {solution_1}")
    print(f"day 08, part 2: {solution_2}")


def day09(filename):
    solution_2 = 0
    loc_H = {"x": 0, "y": 0}
    loc_T = {"x": 0, "y": 0}
    location_bag = set([str(loc_H)])

    def move(loc, dir, stp):
        #         U +y
        #         ∧
        # L -x <- s -> R +x
        #         v
        #         D -y
        instructions = {
            "L": ["x", -1],
            "R": ["x", 1],
            "U": ["y", -1],
            "D": ["y", 1]
        }
        axis, factor = instructions[dir]
        loc[axis] += stp*factor
        return loc

    def adjust(loc_T, loc_H, adding):
        x_dist = loc_H["x"] - loc_T["x"]
        y_dist = loc_H["y"] - loc_T["y"]

        if abs(x_dist) < 2 and abs(y_dist) < 2:
            if adding:
                location_bag.add(str(loc_T))
            return loc_T

        if x_dist > 1 or x_dist > 0 and abs(y_dist) > 1:
            loc_T["x"] += 1
        elif x_dist < -1 or x_dist < 0 and abs(y_dist) > 1:
            loc_T["x"] -= 1

        if y_dist > 1 or y_dist > 0 and abs(x_dist) > 1:
            loc_T["y"] += 1
        elif y_dist < -1 or y_dist < 0 and abs(x_dist) > 1:
            loc_T["y"] -= 1

        if adding:
            location_bag.add(str(loc_T))
        return adjust(loc_T, loc_H, adding)

    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            direction, steps = line.split(" ")
            loc_H = move(loc_H, direction, int(steps))
            loc_T = adjust(loc_T, loc_H, True)

    solution_1 = len(location_bag)

    loc_H = {"x": 0, "y": 0}
    location_bag = set([str(loc_H)])
    tails = {i: {"x": 0, "y": 0} for i in range(10)}
    print(tails)
    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            direction, steps = line.split(" ")
            for _ in range(int(steps)):
                loc_H = move(loc_H, direction, 1)
                prev = loc_H
                for tail in tails:
                    adding = True if tail == 8 else False
                    tails[tail] = adjust(tails[tail], prev, adding)
                    prev = tails[tail]

    solution_2 = len(location_bag)

    print(f"day 09, part 1: {solution_1}")
    print(f"day 09, part 2: {solution_2}")


def day10(filename):
    solution_1 = 0
    cycle = 0
    value = 1

    def cycle_1(cycle, solution):
        cycle += 1
        if cycle in range(20, 221, 40):
            solution += cycle*value
        return cycle, solution

    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            cycle, solution_1 = cycle_1(cycle, solution_1)
            
            if line != "noop":
                _, number = line.split(" ")
                cycle, solution_1 = cycle_1(cycle, solution_1)
                value += int(number)

    print(f"day 10, part 1: {solution_1}")
    print("day 10, part 2:")

    def cycle_2(cycle):
        cycle += 1
        if cycle in range(0, 241, 40):
            if 39 in [offset, offset + 1, offset + 2]:
                print("#")
            else:
                print(" ")
        elif cycle%40 in [offset, offset + 1, offset + 2]:
            print("#", end="")
        else:
            print(" ", end="")

        return cycle

    cycle = 0
    offset = 1
    with open(filename) as f:
        for line in f:
            line = line.strip("\n")
            cycle = cycle_2(cycle)

            if line != "noop":
                _, number = line.split(" ")
                cycle = cycle_2(cycle)
                offset += int(number)


def day11(filename):
    solution_1 = 0
    solution_2 = 0
    with open(filename) as f:
        for line in f:
            continue

    print(f"day 11, part 1: {solution_1}")
    print(f"day 11, part 2: {solution_2}")


# day01("2022/day01.txt")
# day02("2022/day02.txt")
# day03("2022/day03.txt")
# day04("2022/day04.txt")
# day05("2022/day05.txt")
# day06("2022/day06.txt")
# day07("2022/day07.txt")
# day08("2022/day08.txt")
# day09("2022/day09.txt")
# day10("2022/day10.txt")
day11("2022/day11.txt")


def dayXX(filename):
    solution_1 = 0
    solution_2 = 0
    with open(filename) as f:
        for line in f:
            continue

    print(f"day XX, part 1: {solution_1}")
    print(f"day XX, part 2: {solution_2}")
