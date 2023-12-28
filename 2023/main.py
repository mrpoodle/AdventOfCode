import click


from scripts import day as day

@click.command()
@click.argument('day_number', type=int)
@click.argument('part', type=click.Choice(["0", "1", "2"]), default="0", required=False)
@click.argument('input_type', required=False, default='input', type=click.Choice(['input', 'test']))
@click.option('--manual_input', '-i', type=click.Path(exists=True) , required=False, default=None)
def main(day_number, part, input_type, manual_input):
    day_number = f"{day_number:02d}"
    input_file = f"inputs/day{day_number}.tst" if input_type=="test" else f"inputs/day{day_number}.txt"

    if day_number == "00":
        for i in range(1,26):
            i = f"{i:02d}"
            input_file = f"inputs/day{i}.tst" if input_type=="test" else f"inputs/day{i}.txt"
            run_part(i, "1", input_file)
            if i == "05" or i == "12":
                print("\nSkipping day{i} part 2, because it takes fart too long to run")
            else:
                run_part(i, "2", input_file)
        return

    if manual_input:
            input_file = manual_input

    if part == "0":
        parts = ["1", "2"]
    else:
        parts = [part]

    for p in parts:
        run_part(day_number, p, input_file)

def run_part(day_number, part, input_file):
    if day_number not in day:
        print(f"Day {day_number} not found")
        return

    if part in day[day_number]:
        print(f"\nRunning day{day_number} part {part} with input file: {input_file}")
        print("Output:", day[f"{day_number}"][part](input_file))
    else:
        print(f"Function for day{day_number} part {part} not found")


if __name__ == '__main__':
    main()