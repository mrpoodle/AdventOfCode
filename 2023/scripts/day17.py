### for day 00
from copy import deepcopy

def read_input(input_file):
    lines = [[int(char) for char in line.strip("\n")] for line in open(input_file)]

    ## Do whatever with the lines

    return lines

def find_out_1(data, start, dir, visited):
    if start in visited[0] or start[0] >= len(data) or start[1] >= len(data[0]) or start[0] < 0 or start[1] < 0:
        return
    visited[0].append(start)
    visited[1].append(data[start[0]][start[1]])
    if start==[len(data)-1, len(data[0])-1]:
        if path == None or sum(visited[1]) < path:
            path = sum(visited[1])
        return
    if dir[2]<3:
        find_out(data, [start[0], start[1]+dir[1]], [0, dir[1], dir[2]+1], deepcopy(visited))
    find_out(data, [start[0]+dir[1], start[1]+dir[0]], [ dir[1],  dir[0], 1], deepcopy(visited))
    find_out(data, [start[0]-dir[1], start[1]-dir[0]], [-dir[1], -dir[0], 1], deepcopy(visited))

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if [i,j] in visited[0]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
    return

path = None
def find_out(data, start, dir, visited):
    global path
    # print(data, start, dir, visited)
    if start in visited[0] or start[0] >= len(data) or start[1] >= len(data[0]) or start[0] < 0 or start[1] < 0:
        return []
    visited[0].append(start)
    visited[1].append(data[start[0]][start[1]])
    if start==[len(data)-1, len(data[0])-1]:
        if path == None or sum(visited[1]) < path:
            path = sum(visited[1])
        return
    if not path==None:
        if sum(visited[1]) > path:
            return
    print(path)
    options = [
        [[start[0]+dir[0], start[1]+dir[1]],    [      0,  dir[1], dir[2]+1]],
        [[start[0]+dir[1], start[1]+dir[0]],    [ dir[1],  dir[0],        1]],
        [[start[0]-dir[1], start[1]-dir[0]],    [-dir[1], -dir[0],        1]]
    ]
    if options[0][1][2] == 3:
        options.pop(0)
    #options = sorted(options, lambda: data[x[0][0]][x[0][1]] 
    #    find_out(data, option[0], option[1], deepcopy(visited))

def part_1(input_file):
    global path
    data = read_input(input_file)
    start = [0, 0]

    find_out(data, start, [0, 1, 1], [[],[]]) #+ find_out(data, start, [1, 0, 1], [[],[]])

    out = path
    # process and compute out
    return out

def part_2(input_file):
    # read data
    data = read_input(input_file)

    out = "Not implemented yet"
    # process and compute out
    return out

