def to_lists(file):
    reports = []

    for line in open(file):
        reports.append(list(int(a) for a in line.split()))

    return reports

def compare(a, b, direction):
    if abs(a-b) > 3:
        return (direction, False)
    if direction == ">":
        return (">", a > b)
    else:
        return ("<", a < b)

def tester(report):
    current = report[0]
    direction = ">" if current > report[1] else "<"
    for i in range(len(report)):
        if i == 0:
            continue
        direction, status = compare(current, report[i], direction)
        if not status:
            return 0
        current = report[i]
    return 1

def tester_with_dampener(report):
    if tester(report):
        return 1
    for i in range(len(report)):
        new_report = report.copy()
        new_report.pop(i)
        if tester(new_report):
            return 1
    return 0

def test():
    reports = to_lists("day02.tst")
    result = sum(
        tester(report) for report in reports
    )
    print("Test 1: ", result, " Expected: 2")
    result = sum(
        tester_with_dampener(report) for report in reports
    )
    print("Test 2: ", result, " Expected: 4")

def run1():
    reports = to_lists("day02.txt")
    result = sum(
        tester(report) for report in reports
    )
    print("Part 1: ", result)

def run2():
    reports = to_lists("day02.txt")
    result = sum(
        tester_with_dampener(report) for report in reports
    )
    print("Part 2: ", result)

test()
run1()
run2()