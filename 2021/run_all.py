from argparse import ArgumentParser
import timeit


def run(number, timer, parts):
    try:
        day = getattr(
            __import__(f"day{number}", fromlist=["script"]), "script")
    except ModuleNotFoundError as e:
        print(f"Day {number} in not yet available\nError: {e}\n")
        return
    print("Day {}".format(day.DAY))
    for part in parts:
        outcome = day.main_1(day.INPUT) if part == 1 else day.main_2(day.INPUT)
        print(f"{day.DAY}.{part}:    {outcome}")

        if timer:
            time = timeit.timeit(
                stmt=f'day.main_{part}(day.TESTING)',
                setup=f'from day{number} import script as day',
                number=10000)
            print(f"\tTIME: {time}")
    print()


if __name__ == '__main__':
    parser = ArgumentParser(description='run advent of code for specific days')
    parser.add_argument(
        '--days', '-d', type=int, nargs='+', help='list of days to run')
    parser.add_argument(
        '--timer', '-t', action='store_true', help='run timer for each day')
    parser.add_argument(
        '--parts', '-p', type=int, nargs='+',
        help='run timer for each day', default=[1, 2])

    args = parser.parse_args()
    for part in args.parts:
        if part not in [1, 2]:
            print(f"only part 1 and/or 2 are available, not {part}")
            exit()

    if args.days:
        for day in args.days:
            run(f"{day:02}", args.timer, args.parts)
    else:
        for day in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17]:
            run(f"{day:02}", args.timer, args.parts)
