import click

from scripts.days import (
    day01_1, day01_2,
    day02_1, day02_2,
    day03_1, day03_2,
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
from scripts.day13 import part_1 as day13_1, part_2 as day13_2

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
        input_file = f"inputs/day{day_number:02d}.tst" if input_type=="test" else f"day{day_number:02d}.txt"
        print(f"Running day{day_number:02d}_{part} with input file: {input_file}")
        print("Output:", function(input_file))
    else:
        print(f"Function {function_name} not found")


if __name__ == '__main__':
    main()