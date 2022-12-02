def day01(filename):
    def solution(filename, max_elves):
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

    print(f"day 01, part 1: {solution(filename, 1)}")
    print(f"day 01, part 2: {solution(filename, 3)}")


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

    print(f"day 01, part 1: {solution(values_1)}")
    print(f"day 01, part 2: {solution(values_2)}")


day01("2022/day01.txt")
day02("2022/day02.txt")
