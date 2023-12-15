import click

from scripts.days import (
    day04_1, day04_2,
    day05_1, day05_2,
    day06_1, day06_2,
    day07_1, day07_2,
    day08_1, day08_2,
    day09_1, day09_2,
    day10_1, day10_2,
    # day11_1, day11_2,
    # day12_1, day12_2,
)
from scripts.day01 import part_1 as day01_1, part_2 as day01_2
from scripts.day02 import part_1 as day02_1, part_2 as day02_2
from scripts.day03 import part_1 as day03_1, part_2 as day03_2
from scripts.day13 import part_1 as day13_1, part_2 as day13_2
from scripts.day14 import part_1 as day14_1, part_2 as day14_2
from scripts.day15 import part_1 as day15_1, part_2 as day15_2

def get_function_name(day_number, part):
    if part == "0":
        return [f"day{day_number:02d}_1", f"day{day_number:02d}_2"]
    return [f"day{day_number:02d}_{part}"]

@click.command()
@click.argument('day_number', type=int)
@click.argument('part', type=click.Choice(["0", "1", "2"]), default="0", required=False)
@click.argument('input_type', required=False, default='input', type=click.Choice(['input', 'test']))
def main(day_number, part, input_type):
    function_names = get_function_name(day_number, part)
    for function_name in function_names:
        function = globals().get(function_name)
        if function:
            input_file = f"inputs/day{day_number:02d}.tst" if input_type=="test" else f"inputs/day{day_number:02d}.txt"
            print(f"\nRunning {function_name} with input file: {input_file}")
            print("Output:", function(input_file))
        else:
            print(f"Function {function_name} not found")


if __name__ == '__main__':
    main()