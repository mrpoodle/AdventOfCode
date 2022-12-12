import os

DAY = 20
PATH = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(PATH, "input.txt")
TESTING = os.path.join(PATH, "test.txt")


enhancement =(
    "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"
    "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###"
    ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#."
    ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....."
    ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.."
    "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....."
    "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
)



def pad_image(image):
    length = len(image[0])+2
    new_image = ["."*length]
    new_image.extend(["."+line+"." for line in image])
    new_image.append("."*length)
    return new_image


def filter(image):
    for line in range(1,len(image)-2):
        print(image[line])

def main_1(input):
    image = [
        "#..#.",
        "#....",
        "##..#",
        "..#..",
        "..###"
    ]
    image = pad_image(image)
    filter(image)
    return 0


def main_2(input):
    # TODO
    with open(input) as file:
        for line in file:
            pass  # TODO
    return 0


main_1(TESTING)