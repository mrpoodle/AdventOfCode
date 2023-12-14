### for day 00

balls_1 = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

balls_2 = {
    "red": 0,
    "green": 0,
    "blue": 0,
}


def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    games = []
    for line in lines:
        id, turns = line.removeprefix("Game ").split(":")
        games.append((id, turns))

    return games


def test_game(turns, part=1):
    if part == 1:
        balls = balls_1
    elif part == 2:
        balls = balls_2.copy()

    for turn in turns.split(";"):
        ball_set = {
            pair.strip().split(" ")[1]:int(pair.strip().split(" ")[0])
            for pair in turn.strip(" ").split(",")
        }
        for color in ball_set:
            if ball_set[color] > balls[color]:
                if part == 1:
                    return False
                balls[color] = ball_set[color]
    return balls["red"]*balls["green"]*balls["blue"]

def part_1(input_file):
    games = read_input(input_file)

    out = 0
    for id, turns in games:
        out += int(id) if test_game(turns) else 0
    return out


def part_2(input_file):
    games = read_input(input_file)

    out = 0
    for id, turns in games:
        out += test_game(turns, part=2)
    return out