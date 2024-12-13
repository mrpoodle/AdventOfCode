def to_lists(file):
    list1 = []
    list2 = []

    for line in open(file):
        l1, l2 = line.split()
        list1.append(int(l1))
        list2.append(int(l2))

    list1.sort()
    list2.sort()

    return list1, list2

def list_dist(list1, list2):
    return sum(
        abs(list1[i]-list2[i]) for i in range(len(list1))
    )

def count_sum(list1, list2):
    return sum(
        list2.count(list1[i])*list1[i] for i in range(len(list1))
    )

def test():
    list1, list2 = to_lists("day01.tst")
    print("Test 1: ", list_dist(list1, list2), " Expected: 11")
    print("Test 2: ", count_sum(list1, list2), " Expected: 31")


def run1():
    list1, list2 = to_lists("day01.txt")
    print("Part 1: ", list_dist(list1, list2))

def run2():
    list1, list2 = to_lists("day01.txt")
    print("Part 1: ", count_sum(list1, list2))

test()
run1()
run2()