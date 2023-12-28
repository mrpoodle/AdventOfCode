### for day 06

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]
    time = lines[0].split()[1:]
    dist = lines[1].split()[1:]

    return time, dist

def part_1(input_file):
    time, dist = read_input(input_file)
    time_dist = zip(
        [int(number) for number in time],
        [int(number) for number in dist]
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

def part_2(input_file):
    time, dist = read_input(input_file)

    time = int("".join(time))
    dist = int("".join(dist))

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

    # print()
    # print(lower, upper)
    out = upper-(lower-1)
    return out