"""
For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state,
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4,
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14

So, putting that together, and making a common denominator, gives an answer in
the form of [s2.numerator, s3.numerator, s4.numerator, s5.numerator,
denominator] which is [0, 3, 2, 9, 14].


-- Python cases --
Input:
solution.solution([
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])
Output:
    [7, 6, 8, 21]

Input:
solution.solution([
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]])
Output:
    [0, 3, 2, 9, 14]
"""


def traverse(m, state=0, taken=[], prob=(1, 1)):
    print([taken + ["s{}".format(state)] + [reduce(prob)]])
    if sum(m[state]) == 0:
        return [taken + ["s{}".format(state)] + [prob]]
    list = []
    for i, route in enumerate(m[state]):
        if route != 0:
            list += traverse(
                m, i,
                taken + ["s{}".format(state)],
                (prob[0]*route, prob[1]*sum(m[state]))
            )
    return list


def last(elem):
    return elem[-2]


def gcd(fraction):
    n, d = fraction
    while d != 0:
        t = d
        d = n % d
        n = t
    return n


def reduce(fraction):
    n, d = fraction
    greatest = gcd(fraction)
    n /= greatest
    d /= greatest
    return int(n), int(d)


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def solution(m):
    routes = traverse(m)
    routes.sort(key=last)
    probs = [x[-1] for x in routes]
    probs = list(map(reduce, probs))
    maximum = max(p[1] for p in probs)
    return [int(p[0]*maximum/p[1]) for p in probs] + [maximum]


m = [
  [0, 1, 0, 0, 0, 1],  # s0, initial, goes to s1 and s5 with equal probability
  [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4 (probabilities)
  [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable
  [0, 0, 0, 0, 0, 0],  # s3 is terminal
  [0, 0, 0, 0, 0, 0],  # s4 is terminal
  [0, 0, 0, 0, 0, 0],  # s5 is terminal
]
m = [
  [0, 1, 0, 0, 0, 1],  # s0, initial, goes to s1 and s5 with equal probability
  [0, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4 (probabilities)
  [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable
  [0, 0, 0, 0, 0, 0],  # s3 is terminal
  [0, 0, 0, 0, 0, 0],  # s4 is terminal
  [0, 0, 0, 0, 0, 0],  # s5 is terminal
]
m1 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
m2 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
a = solution(m2)
print(a)
