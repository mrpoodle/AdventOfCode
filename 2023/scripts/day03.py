### for day 03

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    ## Do whatever with the lines

    return lines

def part_1(input_file):
    """every number adjacent to a symbol in the matrix should be added to the sum"""
    lines = [line.strip("\n") for line in open(input_file)]

    def check_sourrounding(x, y):
        length = 1
        while lines[x][y+length].isdigit(): #(y+length>len(lines[x])-1) and
            length += 1
            if y+length>len(lines[x])-1:
                break
        number = int(lines[x][y:y+length])
        for i in range(-1, 2):
            for j in range(-1, 1+length):
                if y+j<0 or y+j>len(lines[x])-1 or x+i<0 or x+i>len(lines)-1:
                    continue
                if lines[x+i][y+j] not in "1234567890.":
                    return(True, length, number)

        return(False, length, number)

    length = 1
    out = 0
    for x, l in enumerate(lines):
        for y,char in enumerate(l):
            if length > 1:
                length -= 1
                continue
            if char.isdigit():
                check,length, number = check_sourrounding(x, y)
                if check:
                    # print(number)
                    out += number
    return out


def part_2(input_file):
    """only two numbers ajacent to a * should be multiplied and added to the sum"""
    lines = [line.strip("\n") for line in open(input_file)]
    out = 0

    def find_number(x, y):
        visited = [(x, y)]
        left = 0
        right = 0

        while lines[x][y+left-1].isdigit():
            left -= 1
            visited.append((x, y+left))
        while lines[x][y+right+1].isdigit():
            right += 1
            visited.append((x, y+right))
        number = int(lines[x][y+left:y+right+1])
        return number, visited

    def check_sourrounding(x, y):
        visited = []
        numbers = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i,j) in visited:
                    continue
                if j<0 or j>len(lines[x])-1 or i<0 or i>len(lines)-1:
                    continue
                if lines[i][j].isdigit():
                    number, just_visited = find_number(i, j)
                    visited += just_visited
                    numbers.append(number)
        # print(numbers)
        if len(numbers) == 2:
            # print(x, y)
            # print(numbers[0], "*", numbers[1])
            return(numbers[0]*numbers[1])
        return(0)

    for x, l in enumerate(lines):
        for y,char in enumerate(l):
            if char=="*":
                check = check_sourrounding(x, y)
                # print(check)
                out += check

    return out