def read_in(file):
    # read 4 lines at a time
    lines = []
    machines = []
    for line in open(file):
        if line == "\n":
            machines.append(to_values(lines))
            lines = []
            continue
        lines.append([a for a in line.split()])
    machines.append(to_values(lines))
    return machines

def to_values(lines):
        X = int(lines[2][1][2:-1])
        Y = int(lines[2][2][2:])
        xA = int(lines[0][2][2:-1])
        yA = int(lines[0][3][2:])
        xB = int(lines[1][2][2:-1])
        yB = int(lines[1][3][2:])
        return([X, Y, xA, yA, xB, yB])


def simple_test():
    """
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    """

    X=8400
    Y=5400
    xA=94
    yA=34
    xB=22
    yB=67

    B = (Y*xA - X*yA)/(yB*xA - xB*yA)
    A = (X - B*xB)/xA

    print("Test 0: ", A, B)

def solve(X,Y,xA,yA,xB,yB):
    B = (Y*xA - X*yA)/(yB*xA - xB*yA)
    A = (X - B*xB)/xA

    if A == int(A) and B == int(B):
        return int(A), int(B)
    return False, False

def test1():
    machines = read_in("day13.tst")
    cost = 0
    for machine in machines:
        A, B = solve(*machine)
        # print(A, B)
        if A:
            cost += A*3+B
    print("Test 1: ", cost, "expected: ", 480)


def run2():
    machines = read_in("day13.txt")
    cost = 0
    for machine in machines:
        machine[0] += 10000000000000
        machine[1] += 10000000000000
        A, B = solve(*machine)
        # print(A, B)
        if A:
            cost += A*3+B
    print(cost)

def run1():
    machines = read_in("day13.txt")
    cost = 0
    for machine in machines:
        A, B = solve(*machine)
        # print(A, B)
        if A:
            cost += A*3+B
    print(cost)

# simple_test()
test1()
run1()
run2()