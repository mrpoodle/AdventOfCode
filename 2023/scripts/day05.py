### for day 05

def read_input(input_file):
    chunks = "\n".join([line.strip("\n") for line in open(input_file)])
    maps = []
    for chunk in chunks.split("\n\n"):
        if chunk.startswith("seeds:"):
            seeds = [int(seed) for seed in chunk.removeprefix("seeds: ").split(" ")]
            continue
        my_map = chunk.split("\n")
        maps.append([[int(num) for num in string.split()] for string in my_map[1:]])
    return seeds, maps


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


def part_1(input_file):
    seeds, maps = read_input(input_file)

    out = None
    for seed in seeds:
        seed=find_location(seed, maps)
        if out == None or seed < out:
            out = seed
    return out

def part_2(input_file):
    numbers, maps = read_input(input_file)
    maximum = 0
    length = 0
    seeds=[]
    for first, second in zip(numbers[::2], numbers[1::2]):
        seeds.append(range(first, first+second))
        if first+second>maximum:
            maximum=first+second
        length+=second

    out = None
    counter = 0

    for seed_range in seeds:
        for seed in seed_range:
            seed=find_location(seed, maps)
            if out == None or seed < out:
                out = seed
            counter += 1
            print(counter/length*100, "%    ", out, " "*30, end="\r")

    print()
    ## TODO: implement chunks of ranges
    return out
