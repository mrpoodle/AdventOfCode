### for day 13

def find_mirrow_over_rows(pattern, old_mirrors=None):
        for i, line in enumerate(pattern):
            if old_mirrors and old_mirrors == i:
                continue
            candidate = None
            if i == 0:
                continue
            if line == pattern[i-1]:
                candidate = i
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
            sum += rows*100
        else:
            _, cols = find_mirrow_over_rows(list(zip(*pattern)))
            sum += cols
    return sum

def part_2(input_file):
    patterns = read_input_13(input_file)

    # find if pattern is mirrored over rows
    sum = 0
    for pattern in patterns:
        old_mirrors = None
        mirrors = []
        row_mirrored, rows = find_mirrow_over_rows(pattern)
        if row_mirrored:
            old_mirror = (rows, "row")
        else:
            col_mirrored, cols = find_mirrow_over_rows(list(zip(*pattern)))
            if col_mirrored:
                old_mirror = (cols, "col")
        for i, line in enumerate(pattern):
            for j, char in enumerate(line):
                new_line = line
                new_pattern = pattern.copy()
                if char == ".":
                    new_line = line[:j]+"#"+line[j+1:]
                else:
                    new_line = line[:j]+"."+line[j+1:]
                new_pattern[i] = new_line
                row_mirrored, rows = find_mirrow_over_rows(new_pattern, old_mirror[0] if old_mirror[1] == "row" else None)
                if row_mirrored:
                    mirrors.append((rows, "row"))
                col_mirrored, cols = find_mirrow_over_rows(list(zip(*new_pattern)), old_mirror[0] if old_mirror[1] == "col" else None)
                if col_mirrored:
                    mirrors.append((cols, "col"))
        if len(mirrors) == 0:
            for line in pattern:
                print(line)
            print()
            continue
        first = min(mirrors, key=lambda x: x[0])
        if first[1] == "row":
            sum += first[0]*100
        else:
            sum += first[0]
    return sum

