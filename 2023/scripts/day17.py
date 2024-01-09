### for day 00
from copy import deepcopy
from typing import Any

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


def find_out_2(data, start, dir, visited):
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


class Heatloss_Map (list):
    """A class to store the heatloss map

    the size will be identical to the data given in the constructor. in the
    initial state all values are None.
    """
    def __init__(self, data):
        self.data = [[None for x in range(len(data))] for y in range(len(data[0]))]


def find_path(data, start, aim, dir, visited):
    return

def dist(current, aim):
    return (aim[0]-current[0]) + (aim[1]-current[1])

direcs = [
    ("l",(0, -1)),
    ("r", (0, 1)),
    ("u", (-1, 0)),
    ("d", (1, 0))
]

def find_neighbours(data, current, path_so_far):
    neighbours = []
    current_pos = current[1]
    for dir in direcs:
        # "lrlrlll" -> "lll"
        if path_so_far[-3:] == dir[0]*3:
            continue
        print(path_so_far[-1:]+dir[0])
        if path_so_far[-1:]+dir[0] in ["lr", "rl", "ud", "du"]:
             continue
        if (current_pos[0]+dir[1][0] >= 0 and
                current_pos[0]+dir[1][0] < len(data) and
                current_pos[1]+dir[1][1] >= 0 and
                current_pos[1]+dir[1][1] < len(data[0])):
            neighbours.append((dir[0], (current_pos[0]+dir[1][0], current_pos[1]+dir[1][1]), current_pos))
    return neighbours


def guesstimate_heatloss(neighbors, aim, heatloss_map, data):
    current_pos = neighbors[2]
    next_pos = neighbors[1]
    return (
        dist(current_pos, aim) +
        heatloss_map.data[current_pos[0]][current_pos[1]] +
        data[next_pos[0]][next_pos[1]]
    )


def dijkstra(data, start, aim, heatloss_map):
    current = ("r", start, None)
    heatloss_map.data[start[0]][start[1]] = (
        dist(start, aim) +
        data[start[0]][start[1]]
    )

    last_dirs = ""
    next_neighbors = []
    while heatloss_map.data[aim[0]][aim[1]] == None:
        print("find neighbors")
        next_neighbors = find_neighbours(data, current, last_dirs) + next_neighbors
        print(next_neighbors)
        print("sort")
        next_neighbors = sorted(next_neighbors, key=lambda x: guesstimate_heatloss(x, aim, heatloss_map, data))
        print(next_neighbors)
        print("next")
        current = next_neighbors.pop(0)
        last_dirs += current[0]
        current = next_neighbors.pop(0)
    return heatloss_map.data[aim[0]][aim[1]]

def find_best_path(data):
    global heatloss_map
    heatloss_map = Heatloss_Map(data)

    start = (0, 0)
    aim = [len(data)-1, len(data[0])-1]
    print(list(heatloss_map))

    return dijkstra(data, start, aim, heatloss_map)


def part_1(input_file):
    global path
    data = read_input(input_file)

    return find_best_path(data)

def part_2(input_file):
    # read data
    data = read_input(input_file)

    out = "Not implemented yet"
    # process and compute out
    return out

