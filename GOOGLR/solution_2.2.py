def tni(i, b):
    last = i % b
    rest = int(i/b)
    if rest == 0:
        return str(last)
    return tni(rest, b) + str(last)


def next_ID(ID, b):
    x = "".join(sorted(ID, reverse=True))
    y = "".join(sorted(ID))
    z = tni(int(x, b)-int(y, b), b)
    return z.zfill(len(ID))


def solution_minion(ID, b):
    counter = 0
    seen = []

    while ID not in seen:
        seen.append(ID)
        ID = next_ID(ID, b)
        counter += 1
    return counter - seen.index(ID)

#=============================================================================

"""For example, given the list l as ["1.1.2", "1.0",
"1.3.3", "1.0.12", "1.0.2"], the
function solution(l) would return the list ["1.0",
"1.0.2", "1.0.12", "1.1.2",
"1.3.3"]. If two or more versions are equivalent but one
version contains more numbers than the others, then these versions
must be sorted ascending based on how many numbers they have, e.g
["1", "1.0", "1.0.0"]. The number of
elements in the list l will be at least 1 and will not exceed 100.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown
here.

-- Python cases --
Input:
solution.solution(["1.11", "2.0.0",
"1.2", "2", "0.1", "1.2.1",
"1.1.1", "2.0"])
Output:
    0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0

Input:
solution.solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
Output:
    1.0,1.0.2,1.0.12,1.1.2,1.3.3"""


def major(version):
    v = version.split(".")
    return int(v[0])


def minor(version):
    v = version.split(".")
    return int(v[1]) if len(v) > 1 else -1


def revision(version):
    v = version.split(".")
    return int(v[2]) if len(v) > 2 else -1


def solution(l):
    l.sort(key=revision)
    l.sort(key=minor)
    l.sort(key=major)
    return(l)


solution(
    ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
