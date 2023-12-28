### for day 10

def read_input(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    ## Do whatever with the lines

    return lines

pipes = {
    #     top right bottom left
    "L": ["t", "r"],
    "J": ["t", "l"],
    "7": ["b", "l"],
    "F": ["r", "b"],
    "-": ["l", "r"],
    "|": ["t", "b"],
    ".": []
}

def find_next(current, dist, lines):
    x, y, connections = current
    lines[y][x]=dist
    try:
        if "t" in connections:
            new_connections = pipes[lines[y-1][x]].copy()
            new_connections.remove("b")
            return (x, y-1, new_connections), False
        elif "r" in connections:
            new_connections = pipes[lines[y][x+1]].copy()
            new_connections.remove("l")
            return (x+1, y, new_connections), False
        elif "b" in connections:
            new_connections = pipes[lines[y+1][x]].copy()
            new_connections.remove("t")
            return (x, y+1, new_connections), False
        elif "l" in connections:
            new_connections = pipes[lines[y][x-1]].copy()
            new_connections.remove("r")
            return (x-1, y, new_connections), False
    except KeyError:
        return None, True

def find_path(x, y, lines):
    lines[y][x]=0
    next=[]
    dist = 1
    for i in [-1, 1]:
        if x+i>=0 and x+i<len(lines[0]):
            connections = pipes[lines[y][x+i]].copy()
            if i == -1 and "r" in connections:
                # current left connected to right
                connections.remove("r")
                next.append((x+i, y, connections))
            elif i == 1 and "l" in connections:
                # current right connected to left
                connections.remove("l")
                next.append((x+i, y, connections))
        if y+i>=0 and y+i<len(lines):
            connections = pipes[lines[y+i][x]].copy()
            if i == -1 and "b" in connections:
                # current top connected to bottom
                connections.remove("b")
                next.append((x, y+i, connections))
            elif i == 1 and "t" in connections:
                # current botttom connected to top
                connections.remove("t")
                next.append((x, y+i, connections))
    while True:
        path_1, end_1 = find_next(next[0], dist, lines)
        path_2, end_2 = find_next(next[1], dist, lines)
        if end_1 == True or end_2 == True:
            return dist
        else:
            dist += 1
            next = [path_1, path_2]

def visualize(lines):
    visual = []
    for line in lines:
        v_line = ""
        for char in line:
            if isinstance(char, int):
                v_line += "#"
            else:
                v_line += " "
        visual.append(v_line)
    return visual

def flood_zeros(x, y, lines, changed=0):
    visiting = []
    if y > 1:
        visiting.append((x, y-1))
    if y < len(lines)-1:
        visiting.append((x, y+1))
    if x > 1:
        visiting.append((x-1, y))
    if x < len(lines[0])-1:
        visiting.append((x+1, y))
    for x, y in visiting:
        if lines[y][x] == " ":
            lines[y] = lines[y][:x]+"O"+lines[y][x+1:]
            changed += 1 #flood_zeros(x, y, lines, changed+1)
    return changed, lines

def blow_up(lines):
    new_lines = []
    for line in lines:
        if "S" in line:
            s_line_index = lines.index(line)
            s_line = list("-".join(line))
            s_index = s_line.index("S")
            # print(len(line))
            # print(s_index)
            if s_line[s_index+2] in "LF|.":
                s_line[s_index+1]="."
            if s_line[s_index-2] in "J7|.":
                s_line[s_index-1]="."
            new_lines.append(s_line)
        else:
            new_lines.append(list("-".join(line)))
        new_lines.append(list(".".join("|" for x in line)))
    # print(s_index)
    if s_line_index > 1:
        # print(s_index)
        if new_lines[s_line_index-2][s_index] in "JL-.":
            new_lines[s_line_index-1][s_index]="."
    if s_line_index < len(new_lines)-2:
        if new_lines[s_line_index+2][s_index] in "F7-.":
            new_lines[s_line_index+1][s_index]="."
    return new_lines

def blow_down(lines):
    new_lines = []
    for i, line in enumerate(lines):
        new_line = ""
        if i%2 == 0:
            for j, char in enumerate(line):
                if j%2 == 0:
                    new_line += char
            new_lines.append(new_line)
    return new_lines


def part_1(input_file):
    lines = read_input(input_file)
    for row,line in enumerate(lines):
        if "S" in line:
            start_y = row
            start_x = line.index("S")
            out = find_path(start_x, start_y, lines)
            return out

def part_2(input_file):
    lines = read_input(input_file)
    lines = blow_up(lines)
    for row,line in enumerate(lines):
        if "S" in line:
            start_y = row
            start_x = line.index("S")
            find_path(start_x, start_y, lines)
            break
    new_lines = visualize(lines)
    new_lines[0] = new_lines[0].replace(" ", "O")
    new_lines[-1] = new_lines[-1].replace(" ", "O")
    for i, line in enumerate(new_lines):
        if line.startswith(" "):
            line = "O"+line[1:]
        if line.endswith(" "):
            line = line[:-1]+"O"
        new_lines[i] = line
    while True:
        changed = 0
        for x in range(len(new_lines[0])):
            for y in range(len(new_lines)):
                if new_lines[y][x] == "O":
                    c, new_lines = flood_zeros(x, y, new_lines)
                    changed += c
        if changed == 0:
            break
        else:
            changed = 0
    new_lines=blow_down(new_lines)
    return "".join(new_lines).count(" ")
