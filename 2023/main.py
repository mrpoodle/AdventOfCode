from itertools import cycle, combinations
import math
import click

def day01_1(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    out = 0
    for l in lines:
        first = None
        last = None
        for x in l:
            if x.isdigit():
                last = x
                if first:
                    continue
                first=x
        out += int(first+last)
    return out

def day01_2(input_file):
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
    lines = [line.strip("\n") for line in open(input_file)]
    out = 0
    for l in lines:
        first = None
        last = None
        for x in numbers:
            l = l.replace(x, numbers[x])
        for x in l:
            if x.isdigit():
                last = x
                if first:
                    continue
                first=x
        out += int(first+last)
    return out

def day02_1(input_file):
    balls = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    def test_game(turns):
        for turn in turns.split(";"):
            ball_set = {
                pair.strip().split(" ")[1]:int(pair.strip().split(" ")[0])
                for pair in turn.strip(" ").split(",")
            }
            for color in ball_set:
                if ball_set[color] > balls[color]:
                    return False
        return True

    out = 0
    lines = [line.strip("\n") for line in open(input_file)]
    for line in lines:
        id, turns = line.removeprefix("Game ").split(":")
        out += int(id) if test_game(turns) else 0
    return out


def day02_2(input_file):

    def test_game(turns):
        balls = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for turn in turns.split(";"):
            ball_set = {
                pair.strip().split(" ")[1]:int(pair.strip().split(" ")[0])
                for pair in turn.strip(" ").split(",")
            }
            for color in ball_set:
                if ball_set[color] > balls[color]:
                    balls[color] = ball_set[color]
        return balls["red"]*balls["green"]*balls["blue"]

    out = 0
    lines = [line.strip("\n") for line in open(input_file)]
    for line in lines:
        id, turns = line.removeprefix("Game ").split(":")
        out += test_game(turns)
    return out


def day03_1(input_file):
    """every number adjacent to a symbol in the matrix should be added to the sum"""
    lines = [line.strip("\n") for line in open(input_file)]

    def check_sourrounding(x, y):
        length = 1
        while lines[x][y+length].isdigit(): #(y+length>len(lines[x])-1) and
            length += 1
            if y+length>len(lines[x])-1:
                break
        number = int(lines[x][y:y+length])
        for i in range(-1, 2):
            for j in range(-1, 1+length):
                if y+j<0 or y+j>len(lines[x])-1 or x+i<0 or x+i>len(lines)-1:
                    continue
                if lines[x+i][y+j] not in "1234567890.":
                    return(True, length, number)

        return(False, length, number)

    length = 1
    out = 0
    for x, l in enumerate(lines):
        for y,char in enumerate(l):
            if length > 1:
                length -= 1
                continue
            if char.isdigit():
                check,length, number = check_sourrounding(x, y)
                if check:
                    print(number)
                    out += number
    return out


def day03_2(input_file):
    """only two numbers ajacent to a * should be multiplied and added to the sum"""
    lines = [line.strip("\n") for line in open(input_file)]
    out = 0

    def find_number(x, y):
        visited = [(x, y)]
        left = 0
        right = 0

        while lines[x][y+left-1].isdigit():
            left -= 1
            visited.append((x, y+left))
        while lines[x][y+right+1].isdigit():
            right += 1
            visited.append((x, y+right))
        number = int(lines[x][y+left:y+right+1])
        return number, visited

    def check_sourrounding(x, y):
        visited = []
        numbers = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i,j) in visited:
                    continue
                if j<0 or j>len(lines[x])-1 or i<0 or i>len(lines)-1:
                    continue
                if lines[i][j].isdigit():
                    number, just_visited = find_number(i, j)
                    visited += just_visited
                    numbers.append(number)
        # print(numbers)
        if len(numbers) == 2:
            print(x, y)
            print(numbers[0], "*", numbers[1])
            return(numbers[0]*numbers[1])
        return(0)

    for x, l in enumerate(lines):
        for y,char in enumerate(l):
            if char=="*":
                check = check_sourrounding(x, y)
                # print(check)
                out += check

    return out

def day04_1(input_file):
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

def day04_2(input_file):
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

### for day 5
def find_location(seed, maps):
    for step in maps:
        seed = find_next(seed, step)
    return seed

def find_next(seed, step):
    for my_map in step:
        if seed >= my_map[1] and seed < my_map[1]+my_map[2]:
            seed = my_map[0] + (seed - my_map[1])
            return seed
    return seed

def day05_1(input_file):
    chunks = "\n".join([line.strip("\n") for line in open(input_file)])
    maps = []
    minimum = []
    maximum = []
    for chunk in chunks.split("\n\n"):
        if chunk.startswith("seeds:"):
            seeds = [int(seed) for seed in chunk.removeprefix("seeds: ").split(" ")]
            continue
        my_map = chunk.split("\n")
        maps.append([[int(num) for num in string.split()] for string in my_map[1:]])

    out = None
    for seed in seeds:
        seed=find_location(seed, maps)
        if out == None or seed < out:
            out = seed
    return out

def day05_2(input_file):
    chunks = "\n".join([line.strip("\n") for line in open(input_file)])
    maps = []
    length = 0
    maximum = 0
    for chunk in chunks.split("\n\n"):
        if chunk.startswith("seeds:"):
            seeds=[]
            numbers = [int(x) for x in chunk.removeprefix("seeds: ").split(" ")]
            for first, second in zip(numbers[::2], numbers[1::2]):
                seeds.append(range(first, first+second))
                if first+second>maximum:
                    maximum=first+second
                length+=second
            continue
        my_map = chunk.split("\n")
        maps.append([[int(num) for num in string.split()] for string in my_map[1:]])

    out = None
    counter = 0

    for seed_range in seeds:
        for seed in seed_range:
            seed=find_location(seed, maps)
            if out == None or seed < out:
                out = seed
            counter += 1
            print(counter/length*100, "%    ", out, " "*30, end="\r")

    ## TODO: implement chunks of ranges

    print()
    return out

def day06_1(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    time_dist = zip(
        [int(number) for number in lines[0].split()[1:]],
        [int(number) for number in lines[1].split()[1:]]
    )
    score = 1
    for round in time_dist:
        wins = 0
        for i in range(round[0]):
            travelled = i*(round[0]-i)
            if travelled > round[1]:
                wins += 1
        score *= wins
    out = score
    return out

def day06_2(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    time = int("".join([number for number in lines[0].split()[1:]]))
    dist = int("".join([number for number in lines[1].split()[1:]]))

    step = time/2
    pointer = step

    while True:
        travelled = pointer*(time-pointer)
        if travelled > dist:
            if step < 1:
                lower=int(pointer+1)
                break
            pointer -= step/2
        else:
            pointer += step/2
        step /= 2

    step = time/2
    pointer = step
    while True:
        travelled = pointer*(time-pointer)
        if travelled < dist:
            if step < 1:
                upper=int(pointer)
                break
            pointer -= step/2
        else:
            pointer += step/2
        step /= 2

    print()
    print(lower, upper)
    out = upper-(lower-1)
    return out

def day07_1(input_file):
    lines = [line.strip("\n").split(" ") for line in open(input_file)]
    def get_hand_value(hand):
        """returns the value of a hand"""
        # 5	of	a	Kind
        if len(set(hand)) == 1:
            value='G'
        # four of a kind
        elif len(set(hand)) == 2:
            if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
                value='F'
            # full house
            else:
                value='E'
        # 3 of a kind
        elif len(set(hand)) == 3:
            if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
                value='D'
            # 2 pairs
            else:
                value='C'
        # 1 pair
        elif len(set(hand)) == 4:
            value='B'
        # high card
        else:
            value='A'

        # values for cards in order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
        card_values = {
            '2': 'a',
            '3': 'b',
            '4': 'c',
            '5': 'd',
            '6': 'e',
            '7': 'f',
            '8': 'g',
            '9': 'h',
            'T': 'i',
            'J': 'j',
            'Q': 'k',
            'K': 'l',
            'A': 'm'
        }
        for card in hand:
            value += card_values[card]

        return value

    lines = sorted(lines, key=lambda x: get_hand_value(x[0]))

    out = 0
    multiplyer = 1
    for line in lines:
        #print(multiplyer, "*", int(line[1]))
        out += multiplyer * int(line[1])
        multiplyer += 1
    return out

def day07_2(input_file):
    lines = [line.strip("\n").split(" ") for line in open(input_file)]
    def get_hand_value(hand):
        """returns the value of a hand"""
        # 5	of	a	Kind
        if len(set(hand)) == 1 or (len(set(hand)) == 2 and "J" in hand):
            value='G'
        # four of a kind
        elif len(set(hand)) == 2 or (len(set(hand)) == 3 and "J" in hand):
            sub_set = list(set(filter(lambda a: a != "J", hand)))
            jokers = hand.count("J")

            if hand.count(sub_set[0])+jokers == 4 or hand.count(sub_set[1])+jokers == 4:
                value='F'
            # full house
            else:
                value='E'
        # 3 of a kind
        elif len(set(hand)) == 3 or (len(set(hand)) == 4 and "J" in hand):
            sub_set = list(set(filter(lambda a: a != "J", hand)))
            jokers = hand.count("J")

            if hand.count(sub_set[0])+jokers == 3 or hand.count(sub_set[1])+jokers == 3 or hand.count(sub_set[2])+jokers == 3:
                value='D'
            # 2 pairs
            else:
                value='C'
        # 1 pair
        elif len(set(hand)) == 4 or (len(set(hand)) == 5 and "J" in hand):
            value='B'
        # high card
        else:
            value='A'

        # values for cards in order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
        card_values = {
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            'T': 'j',
            'J': 'a',
            'Q': 'k',
            'K': 'l',
            'A': 'm'
        }
        for card in hand:
            value += card_values[card]
        return value

    lines = sorted(lines, key=lambda x: get_hand_value(x[0]))

    out = 0
    multiplyer = 1
    for line in lines:
        #print(multiplyer, "*", int(line[1]))
        out += multiplyer * int(line[1])
        multiplyer += 1
    return out

def day08_1(input_file):
    lines = [[element.strip(")(,") for element in line.strip("\n").split(" ")] for line in open(input_file)]
    lines = filter(lambda x: x[0].startswith("#") == False , lines)
    instructions = None
    map = {}
    for line in lines:
        if not instructions:
            instructions = line[0]
            continue
        if line[0] == "":
            continue
        map[line[0]] = (line[2], line[3])

    current = "AAA"
    steps = 0
    for i in cycle(instructions):
        if current == "ZZZ":
            break
        steps += 1
        if i == "L":
            current = map[current][0]
        elif i == "R":
            current = map[current][1]
    return steps


def day08_2(input_file):
    lines = [[element.strip(")(,") for element in line.strip("\n").split(" ")] for line in open(input_file)]
    lines = filter(lambda x: x[0].startswith("#") == False , lines)
    instructions = None
    map = {}
    for line in lines:
        if not instructions:
            instructions = line[0]
            continue
        if line[0] == "":
            continue
        map[line[0]] = (line[2], line[3])

    current = [key for key in map.keys() if key[-1] == "A"]
    all_loops = []
    for c in current:
        loops = []
        steps = 0
        last= 0
        for i in cycle(instructions):
            if c.endswith("Z"):
                if steps-last in loops:
                    break
                loops.append(steps-last)
                last = steps
            steps += 1
            if i == "L":
                c = map[c][0]
            elif i == "R":
                c = map[c][1]
        all_loops += list(set(loops))
    return math.lcm(*all_loops)

def day09_common(input_file):
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

def day09_1(input_file):
    out = day09_common(input_file)[1]
    return out

def day09_2(input_file):
    out = day09_common(input_file)[0]
    return out

### for day 10

pipes = {
    #     top right bottom left
    "L": ["t", "r"],
    "J": ["t", "l"],
    "7": ["b", "l"],
    "F": ["r", "b"],
    "-": ["l", "r"],
    "|": ["t", "b"],
    ".": []
}

def find_next(current, dist, lines):
    x, y, connections = current
    lines[y][x]=dist
    try:
        if "t" in connections:
            new_connections = pipes[lines[y-1][x]].copy()
            new_connections.remove("b")
            return (x, y-1, new_connections), False
        elif "r" in connections:
            new_connections = pipes[lines[y][x+1]].copy()
            new_connections.remove("l")
            return (x+1, y, new_connections), False
        elif "b" in connections:
            new_connections = pipes[lines[y+1][x]].copy()
            new_connections.remove("t")
            return (x, y+1, new_connections), False
        elif "l" in connections:
            new_connections = pipes[lines[y][x-1]].copy()
            new_connections.remove("r")
            return (x-1, y, new_connections), False
    except KeyError:
        return None, True

def find_path(x, y, lines):
    lines[y][x]=0
    next=[]
    dist = 1
    for i in [-1, 1]:
        if x+i>=0 and x+i<len(lines[0]):
            connections = pipes[lines[y][x+i]].copy()
            if i == -1 and "r" in connections:
                # current left connected to right
                connections.remove("r")
                next.append((x+i, y, connections))
            elif i == 1 and "l" in connections:
                # current right connected to left
                connections.remove("l")
                next.append((x+i, y, connections))
        if y+i>=0 and y+i<len(lines):
            connections = pipes[lines[y+i][x]].copy()
            if i == -1 and "b" in connections:
                # current top connected to bottom
                connections.remove("b")
                next.append((x, y+i, connections))
            elif i == 1 and "t" in connections:
                # current botttom connected to top
                connections.remove("t")
                next.append((x, y+i, connections))
    while True:
        path_1, end_1 = find_next(next[0], dist, lines)
        path_2, end_2 = find_next(next[1], dist, lines)
        if end_1 == True or end_2 == True:
            return dist
        else:
            dist += 1
            next = [path_1, path_2]

def visualize(lines):
    visual = []
    for line in lines:
        v_line = ""
        for char in line:
            if isinstance(char, int):
                v_line += "#"
            else:
                v_line += " "
        visual.append(v_line)
    return visual

def day10_1(input_file):
    lines = [list(line.strip("\n")) for line in open(input_file)]
    for row,line in enumerate(lines):
        if "S" in line:
            start_y = row
            start_x = line.index("S")
            out = find_path(start_x, start_y, lines)
            return out
        visual.append(v_line)

def flood_zeros(x, y, lines, changed=0):
    visiting = []
    if y > 1:
        visiting.append((x, y-1))
    if y < len(lines)-1:
        visiting.append((x, y+1))
    if x > 1:
        visiting.append((x-1, y))
    if x < len(lines[0])-1:
        visiting.append((x+1, y))
    for x, y in visiting:
        if lines[y][x] == " ":
            lines[y] = lines[y][:x]+"O"+lines[y][x+1:]
            changed += 1 #flood_zeros(x, y, lines, changed+1)
    return changed, lines

def blow_up(lines):
    new_lines = []
    for line in lines:
        if "S" in line:
            s_line_index = lines.index(line)
            s_line = list("-".join(line))
            s_index = s_line.index("S")
            print(len(line))
            print(s_index)
            if s_line[s_index+2] in "LF|.":
                s_line[s_index+1]="."
            if s_line[s_index-2] in "J7|.":
                s_line[s_index-1]="."
            new_lines.append(s_line)
        else:
            new_lines.append(list("-".join(line)))
        new_lines.append(list(".".join("|" for x in line)))
    print(s_index)
    if s_line_index > 1:
        print(s_index)
        if new_lines[s_line_index-2][s_index] in "JL-.":
            new_lines[s_line_index-1][s_index]="."
    if s_line_index < len(new_lines)-2:
        if new_lines[s_line_index+2][s_index] in "F7-.":
            new_lines[s_line_index+1][s_index]="."
    return new_lines

def blow_down(lines):
    new_lines = []
    for i, line in enumerate(lines):
        new_line = ""
        if i%2 == 0:
            for j, char in enumerate(line):
                if j%2 == 0:
                    new_line += char
            new_lines.append(new_line)
    return new_lines

def day10_2(input_file):
    lines = [list(line.strip("\n")) for line in open(input_file) if not line.startswith("#")]
    #print("\n".join(["".join(line) for line in lines]))
    lines = blow_up(lines)
    print("\n".join(["".join(line) for line in lines]))
    for row,line in enumerate(lines):
        if "S" in line:
            start_y = row
            start_x = line.index("S")
            find_path(start_x, start_y, lines)
            break
    new_lines = visualize(lines)
    new_lines[0] = new_lines[0].replace(" ", "O")
    new_lines[-1] = new_lines[-1].replace(" ", "O")
    for i, line in enumerate(new_lines):
        if line.startswith(" "):
            line = "O"+line[1:]
        if line.endswith(" "):
            line = line[:-1]+"O"
        new_lines[i] = line
    while True:
        changed = 0
        for x in range(len(new_lines[0])):
            for y in range(len(new_lines)):
                if new_lines[y][x] == "O":
                    c, new_lines = flood_zeros(x, y, new_lines)
                    changed += c
        if changed == 0:
            break
        else:
            changed = 0
    #print("\n".join(new_lines))
    new_lines=blow_down(new_lines)
    #print("\n".join(new_lines))
    return "".join(new_lines).count(" ")

def expand(lines):
    # duplicate empty lines
    new_lines = []
    for i, line in enumerate(lines):
        if set(line) == {"."}:
            new_lines.append(line)
        new_lines.append(line)

    # turn lines
    turned_lines = ["" for x in new_lines[0]]
    for i, line in enumerate(new_lines):
        for j, char in enumerate(line):
            turned_lines[j] += char

    # duplicate empty lines and turn
    expanded_lines =  ["" for x in turned_lines[0]]
    for i, line in enumerate(turned_lines):
        if set(line) == {"."}:
            for j, char in enumerate(line):
                expanded_lines[j] += char*2
        else:
            for j, char in enumerate(line):
                expanded_lines[j] += char
    return expanded_lines

def day11_1(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    lines = expand(lines)

    galaxies = []
    for i, line in enumerate(lines):
        for char in line:
            if char == "#":
                galaxies.append((i, line.index(char)))
    dist = 0
    paths = 0
    for pair in combinations(galaxies, 2):
        paths += 1
        dist += abs(pair[0][0]-pair[1][0])+abs(pair[0][1]-pair[1][1])
    print(paths)
    return dist

def get_function_name(day_number, part):
    return f"day{day_number:02d}_{part}"

@click.command()
@click.argument('day_number', type=int)
@click.argument('part', type=int)
@click.argument('input_type', required=False, default='input', type=click.Choice(['input', 'test']))
def main(day_number, part, input_type):
    function_name = get_function_name(day_number, part)
    function = globals().get(function_name)
    if function:
        input_file = f"day{day_number:02d}.tst" if input_type=="test" else f"day{day_number:02d}.txt"
        print(f"Running day{day_number:02d}_{part} with input file: {input_file}")
        print("Output:", function(input_file))
    else:
        print(f"Function {function_name} not found")


if __name__ == '__main__':
    main()

