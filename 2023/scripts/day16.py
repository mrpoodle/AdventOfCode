### for day 00
from sys import setrecursionlimit
setrecursionlimit(10000)
from copy import deepcopy

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    grid = []
    for line in lines:
        grid.append([])
        for char in line:
            grid[-1].append([char, 0, []])

    ## Do whatever with the lines

    return grid


def find_out(grid, beam):
    if beam[0] >= len(grid) or beam[1] >= len(grid[0]) or beam[0] < 0 or beam[1] < 0:
        return
    if beam[2] in grid[beam[0]][beam[1]][2]:
        return
    else:
        grid[beam[0]][beam[1]][2].append(beam[2])
    grid[beam[0]][beam[1]][1] = 1
    if grid[beam[0]][beam[1]][0] == "/":
        # 0,1 -> -1,0
        # 1,0 -> 0,-1
        # -1,0 -> 0,1
        # 0,-1 -> 1,0
        new_dir = [beam[2][1]*-1, beam[2][0]*-1]
    elif grid[beam[0]][beam[1]][0] == "\\":
        # 0,1 -> 1,0
        # 1,0 -> 0,1
        # -1,0 -> 0,-1
        # 0,-1 -> -1,0
        new_dir = [beam[2][1], beam[2][0]]
    elif grid[beam[0]][beam[1]][0] == "|":
        # 0,1 or 0,-1 -> 1,0 & -1,0
        find_out(grid, [beam[0]+1, beam[1], [1, 0]])
        new_dir = [-1, 0]
    elif grid[beam[0]][beam[1]][0] == "-":
        # 1,0 or -1,0 -> 0,1 & 0,-1
        find_out(grid, [beam[0], beam[1]+1, [0, 1]])
        new_dir = [0, -1]
    else:
        new_dir = beam[2]
    find_out(grid, [beam[0]+new_dir[0], beam[1]+new_dir[1], new_dir])




def part_1(input_file):
    beam = [0, 0, [0, 1]]  # [x, y, [speed_x, speed_y]]
    grid = read_input(input_file)

    find_out(grid, beam)

    out = 0
    for line in grid:
        out += sum([field[1] for field in line])
    return out


def part_2(input_file):
    # speeds: 1=up, 2=right, 3=down, 4=left
    grid = read_input(input_file)
    beams = [[0, 0, [0, 1]], [0, 0, [1, 0]], [0, len(grid[0])-1, [0, -1]], [len(grid[0])-1, 0, [-1, 0]]]
    out = 0

    for i in range(1, len(grid[0])):
        beams[0][0] = i
        beams[1][1] = i
        beams[2][0] = i
        beams[3][1] = i
        for beam in beams:
            light = 0
            current_grid = deepcopy(grid)
            find_out(current_grid, beam)
            for line in current_grid:
                light += sum([field[1] for field in line])
            if light > out:
                out = light
    return out

