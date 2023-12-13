### for day 13

def find_mirrow_over_rows(pattern):
        for i, line in enumerate(pattern):
            candidate = False
            if i == 0:
                continue
            if line == pattern[i-1]:
                candidate = (i-1, i)
                for j in range(1, i):
                    if i-1-j < 0 or i+j > len(pattern)-1:
                        break
                    if pattern[i-1-j] != pattern[i+j]:
                        candidate = None
                        break
                if candidate:
                    return True, candidate
        return False, None

def read_input_13(input_file):
    lines = [line.strip("\n") for line in open(input_file)]

    # split lines at empty line
    patterns = []
    pattern = []
    for line in lines:
        if line == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)
    return patterns

def part_1(input_file):
    patterns = read_input_13(input_file)

    # find if pattern is mirrored over rows
    sum = 0
    for pattern in patterns:
        row_mirrored, rows = find_mirrow_over_rows(pattern)
        if row_mirrored:
            sum += rows[1]*100
        else:
            _, cols = find_mirrow_over_rows(list(zip(*pattern)))
            sum += cols[1]
    return sum

def part_2(input_file):
    patterns = read_input_13(input_file)

    # find if pattern is mirrored over rows
    sum = 0
    for pattern in patterns:
        mirrors = []
        row_mirrored, rows = find_mirrow_over_rows(pattern)
        if row_mirrored:
            mirrors.append((rows[1], "row"))
        else:
            col_mirrored, cols = find_mirrow_over_rows(list(zip(*pattern)))
            if col_mirrored:
                mirrors.append((cols[1], "col"))
        for i, line in enumerate(pattern):
            for j, char in enumerate(line):
                new_line = line
                new_pattern = pattern.copy()
                if char == ".":
                    new_line = line[:j]+"#"+line[j+1:]
                else:
                    new_line = line[:j]+"."+line[j+1:]
                new_pattern[i] = new_line
                row_mirrored, rows = find_mirrow_over_rows(new_pattern)
                if row_mirrored:
                    mirrors.append((rows[1], "row"))
                col_mirrored, cols = find_mirrow_over_rows(list(zip(*new_pattern)))
                if col_mirrored:
                    mirrors.append((cols[1], "col"))
        first = min(mirrors, key=lambda x: x[0])
        if first[1] == "row":
            sum += first[0]*100
        else:
            sum += first[0]
    return sum

