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

    print(f"day 03, part 1: {counter_1}")
    print(f"day 03, part 2: {counter_2}")


# day01("2022/day01.txt")
# day02("2022/day02.txt")
# day03("2022/day03.txt")
day04("2022/day04.txt")
