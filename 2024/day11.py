from functools import lru_cache

def blinker(stones, limit):
    return sum(
        counter(stone, 0, limit)
        for stone in stones
    )


@lru_cache(maxsize=None)
def counter(stone, blinks, limit):
    blinks += 1
    if blinks > limit:
        return 1
    elif stone == 0:
        return counter(1, blinks, limit)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        return counter(int(stone_str[:int(len(stone_str)/2)]), blinks, limit) + counter(int(stone_str[int(len(stone_str)/2):]), blinks, limit)
    else:
        return counter(stone * 2024, blinks, limit)

def test():
    stones = [125, 17]
    print("Test: ", blinker(stones, 25), " Expected: 55312")


def run1():
    stones = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]
    print("Part 1: ", blinker(stones, 25))

def run2():
    stones = [2701, 64945, 0, 9959979, 93, 781524, 620, 1]
    print("Part 2: ", blinker(stones, 75))

test()
run1()
run2()