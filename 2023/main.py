import click


from scripts import day as day

@click.command()
@click.argument('day_number', type=int)
@click.argument('part', type=click.Choice(["0", "1", "2"]), default="0", required=False)
@click.argument('input_type', required=False, default='input', type=click.Choice(['input', 'test']))
@click.option('--manual_input', '-i', type=click.Path(exists=True) , required=False, default=None)
def main(day_number, part, input_type, manual_input):
    day_number = f"{day_number:02d}"
    if day_number not in day:
        print(f"Day {day_number} not found")
        return

    if part == "0":
        parts = ["1", "2"]
    else:
        parts = [part]

    for p in parts:
        if p in day[day_number]:
            input_file = f"inputs/day{day_number}.tst" if input_type=="test" else f"inputs/day{day_number}.txt"
            if manual_input:
                input_file = manual_input
            print(f"\nRunning day{day_number} part {p} with input file: {input_file}")
            print("Output:", day[f"{day_number}"][p](input_file))
        else:
            print(f"Function for day{day_number} part {p} not found")


if __name__ == '__main__':
    main()