import time, itertools, hashlib, re
from math import log

########################
guides="(((())))()((((((((())()(()))(()((((()(()(((()((()((()(()()()()()))(((()(()((((((((((())(()()((())()(((())))()(()(()((()(()))(()()()()((()((()(((()()(((((((()()())()((((()()(((((()(())()(())((())()()))()(((((((())(()())(()(((())(()))((())))(()((()())))()())((((())))(()(((((()(())(((()()((()((()((((((((((())(()())))))()))())()()((((()()()()()()((((((())())(((()())()((()()(((()()()))(((((()))(((()(()()()(()(()(((())()))(()(((()((())()(()())())))((()()()(()()(((()))(((()((((()(((((()()(()())((()())())(()((((((()(()()))((((()))))())((())()()((()(()))))((((((((()))(()()(((())())(())()((()()()()((()((()((()()(((())))(()((())()((((((((()((()(()()(((())())())))(())())))()((((()))))))())))()()))()())((()())()((()()()))(()()(((()(())((((())())((((((((()()()()())))()()()((((()()))))))()((((()(((()))(()()())))((()()(((()))()()())())(((())((()()(())()()()(((())))))()())((()))()))((())()()())()())()()(()))())))())()))(())((()(())))(()(())(()))))(()(())())(()(())(()(()))))((()())()))()((((()()))))())))()()())((())()((()()()))()(((()(()))))(())()()))(((()())))))))))(((())))()))())()))))()()(((())))))))()(()()(()))((()))))((())))((()((())))())))()()(()))())()(()((()())(()(()()())())(()()))()))))(()())()()))()()()()))(()(()(()))))))()(()))()))()()(()((())(()(())))()(((())(())())))))()(()(()))))()))(()()()(())()(()(())))()))))()()(((((())))))())()())())())()())()))))()))))))))())()()()()()()())))()))((())()))())))()((())()))))()))())))))))())()()()))()()(()((((()(((((((()(())((()())((()()))()))))(())))()()()(())((())()())))(())))(())))(((()()))()(())(((()(()))((())))())()))((((()))())()))))))))()(())())))(()))()(()()))())()()(())())))())()()(()())))()((()())(()(())(())))))))))))))(()))))()))))))()()())(()(((((()(()())))())()))(()))()))(()()))()())(()))())()(())((()()))))))())))())()(((())))(()(()))()()))()(()))))))((()())(()))))))()())))()()))))))))((((((((()()()(()))))))()())))())))()()((())()))((())(())))())())))()()()((()((()(())))())()(())))))))))()())))()()()()()()))()))((())())(()(()))))))(()()))()))(())))()))))))))))))(()))))))))()))))()))()())()))()()))))))()))))((()))))(()))())()(())))(()())((((()())))()))))(()))()(()()(())))))())))))()))))))())))())))))())))())())))())(()))))(())()(())))())()))((()()))))))())))((())))))))())))(())))))()()())))))())))))()))))))()))()()()(()(((()())())())(()))())))))((()(())(()))))))))(())))()()()())())(()))))()()()))()))())())())()(())))()(((()((((())))))))()))))))))))))))))))))((())()())(()))))()()))))))(()()(())())))())))((())))((())))))))))))))()))))()(()))))))())))))()))(()()())(()())))))))))()))))))(())))))()()))()())(((())))()))(()))))))))(())())))())))())())())()()))((())()(())()())()))()())(())(()))))()())))(()(((()))))))()(()())()()()))()))))))))()()()(())()())()(((((()))()())())(()))))()()()(())))())))()((()())))(()))())()(()())())(()))()()))((()()))((()()()()())))(())()))(()(())))((()()))))))))())))))))())()()))))))))))))))))(())()(())(())()())())()))()(()))))())())))))()())()(()))()()(())))(())())))))(()))))))))))))))())())(())(())))(((()))()))))())((())(()))())))))))())))))())))()))()))))))))))))())()))))()))))((()))(())))()(())))(())()))()))())))())))))))()(()())())))()()())))(())))))(()))))))))))))(()))()))()))())))(((()()()(())((()())))()())(((()))(())()))((()()()())))())(())(()))))()(((((())))(()))())())))))))((((()()()))())())()(()(()())))))))))()())())))(())))()())(((()(())())()()))())())))))))((()())((()()(()))(()(())))()))()))(()))(()))()()(()(((())((((()))()(()))((())()(()(()())()(()))()())))))(()))()))())()())))())))(())))((())(()())))))()))(())(()))()())()(()()((()(()))))))()(())(()())(())()))(((())()))(()()(()()()))))(()(())))()))))())))))())(()()()()()()(((())))(()()))()((())(((((()()())))(()))(()))()()))(((())())()(((()()()()))))(()))(())())))()())(()()())())))))))()))))((())))()())(()))(()(()))())))))())(())))))()()())())()))()()(())))(()))(())((((((())(()))(()))())()))(()()(())))()))(()()))()))()(())))(())))((()(()))(())()()())())))(((()()())(())()))))))()(((()(((((()()(((())(())))())()((()))))((()())()(())(((())))(((()((()(()(()))(()()))())(()))(())(())))()))))))((((()))()((((()(()))()))()()))))()(()(()))()(()((()(((()(()()(((()))))()(((()(()(()(((()(()())())()()(()(()())())(()((((())(()))()))(((((()()())(())()((()()())))()()(((()()))()((((((((()(())))())((()))))(())))(()))))((()((((()()(())(((((()))(((((((((((((()())))((((()(((()((())())()))((()))()(()()((()()()()(()()(()(()(((())()(()((((((()((()()((())()((((()((()()(()()())((()()()((()((())()(()(((()((())((((())(()))((()(()))(()())()((((((((()(((((((((((()))(()(((()(()()()((((())((())()())()))(())((())(()))(((()((()(())))(()))))((()()))))((((()(()(()())(()(())((((((((()((((()((()(((((()))())()(()))(()()((()(())(((((()(())()(((((()()))))))()(((())()(()()((((())()((())((()(((())(((()))((()()((((()(())))))((()((((()((()((()(((())((()))(((((((()(((()((((((((())()))((((())(((((()((((((((()(((()((()(((()()(((()((((((()()(()((((((((()()(()(()(())((((()())()))))(((()))((((())((((()())((()(())()((()((((((()((((((()(())))()())(((())())())()(())()(()())((()()((((())((((((())(()(((((()((((())()((((()(()(())(()())(((())()((())((((()))()((((((())(()(((()(((()((((((()(((()))(()()())())((()((()())()((((())(((()(()(((((((((())(())))()((()()()()(())((()))(((((((()(((((((((()(()))))(()((((((((()((((()((()()((((((()()(((((((()(()(())()(())((()()()((()(((((()())()(((((()())()()((()(()())(()()()(((()()(((((()((((((()()((()(()()()((((((((((((()((((((((()()(((()())))()(((()()(())())((((()((((()((((()()()(())(())((()(()(((((((((((((((()(())(())))))()()))((()(((()(())((()(((()(()()((((()()(((()(((()(((((()()((()(()(((()))((((((()((((((((()((()((())(((((()(((())(())())((()()))((((())()()((()(((()(((((()()(((()))(((()(()(((((((((((((()))((((((((()(((()))))())((((((((((((())((())((()())(((())((())(()((((((((((()(((())((()()(()((())(((((((((((()))((((((((((((()(()())((()((()((()(()(((()((((((((()()(()((()(()(((()))((()))(((((((((((((()(())((((((())(((()(())(()(()(()((()()))((((()((((()((((())))())((((()((((()))((((((()((((((()((()(((())))((())(()))(()((()((((()((()(((()()))((((()()()(((((((())(((())(()))())((((()())(((()(((((((((((()(()(()((()(((((((((((((((()()((((()((((((((()(((()()((()((((()))(((()(())((((((()((((())()((((()((()))(())()(()(((()((())())((((((()(()(())())(((())(()(()())(((((()((()((())()())(())))(((()(())))))))(((()(((()))()((()(((()()((()())()()))())))(((()))(()(((()(((((((((()(()(((((()()(((()())()()))))()(((()))(((()(()(()(()(()))()(())()))(()(((())))(()))))))))))(())((()((())((()(())()(())((()()((((()()((()()))((())(((()((()(())(())))()(()(((((()((()))())()(((((()()(((()(()((((((())(()))(())()))((()(()()))(())())()))(((())))(()((()(((())(())())))((()()((((((((((((((()((()(()()(()(((()))())()()((()()()(())(()))(()())(((())((())()(())()()(()()(())))((()(((()))))(((()()(()()))())((()((())()))((((()()()())((())))(((()(())(((((()(((((()((()(()((((()()(((()()()(((()())(((()()((((())(()))(((()))(())())((()))(((()((()))(((()()((())((()(((((()((((()()())((()))()((((()((()(()()()("

def day1(guides):
    floor = 0
    for i,b in enumerate(guides,start=1):
        if b == "(":
            floor+=1
        if b == ")":
            floor-=1
        if floor == -1:
            print(i)
            break

########################

def paper_calculator(l, w, h):
    sides=[l*h, l*w, w*h]
    return sum(sides)*2 + min(sides)

def ribbon_calculator(l, w, h):
    sides=[l, w, h]
    return ( sum(sides) - max(sides) )*2 + ( l * w * h )

def day2():
    paper=0
    ribbon=0
    for line in open("input_2.txt"):
        l,w,h = line.strip("\n").split("x")
        paper += paper_calculator(int(l),int(w),int(h))
        ribbon += ribbon_calculator(int(l),int(w),int(h))

    print(ribbon_calculator(2,3,4))
    print("paper:\t{}".format(paper))
    print("ribbon:\t{}".format(ribbon))

########################

def find_locations(list):
    x=0
    y=0
    locations=[]
    locations.append("0_0")
    for d in list:
        if d == "<":
            x-=1
        elif d == ">":
            x+=1
        elif d == "v":
            y-=1
        elif d == "^":
            y+=1
        else:
            raise EnvironmentError
        locations.append("{}_{}".format(x,y))
    return locations

def day3_2():
    for line in open("input_3.txt"):
        s = line[::2]
        r = line[1::2]
        sList = find_locations(s)
        rList = find_locations(r)
        mylist = sList+rList
        houses=[(i,mylist.count(i)) for i in set(mylist)]
        print(len(houses))

def day3_1():
    for line in open("input_3.txt"):
        mylist=find_locations(line)
        houses=[(i,mylist.count(i)) for i in set(mylist)]
        print(len(houses))

########################

def day4():
    str2hash = "yzbqklnj"
  
    for i in itertools.count(start=1, step=1):
        string = str2hash+str(i)
        result = hashlib.md5(string.encode())
        if result.hexdigest()[:6] == "000000":
            print(string)
            return

#########################

def vowels(string):
    v = re.findall(r"[aeiou]", string)
    if len(v) >=3:
        return True
    return False

def double(string):
    v = re.findall(r"(\w)\1{1}",string)
    if len(v) >=1:
        return True
    return False

def forbidden(string):
    for x in ["ab", "cd", "pq", "xy"]:
        v = re.findall(x,string)
        if len(v) >=1:
            return True
    return False

def double_pair(string):
    v = re.findall(r"(\w).\1{1}",string)
    if len(v) >=1:
        return True
    return False

def spaced_double(string):
    v = re.findall(r"(\w\w).*\1{1}",string)
    if len(v) >=1:
        return True
    return False

def nice_1(string):
    if vowels(string) and double(string):
        if forbidden(string):
            return False
        return True
    return False

def nice_2(string):
    if spaced_double(string) and double_pair(string):
        return True
    return False

def day5():
    count = 0
    print(nice_2("qjhvhtzxzqqjkmpb")) #nice
    print(nice_2("xxyxx")) #nice
    print(nice_2("uurcxstgmygtbstg")) #naughty
    print(nice_2("ieodomkazucvgmuy")) #naughty

    for line in open("input_5.txt"):
        if nice_2(line):
            count+=1
    print(count)
    return




##################################

def division_check(base, divider):
    if base%divider == 0:
        return True
    return False

def day20(number, two):
    house=[0]*(number+1)
    
    for elve in range(1,number):
        count=0
        for visiting in range(elve, number, elve):
            house[visiting] += 10*elve if not two else 11*elve
            count+=1
            if count >=50 and two: break

    for i,m in enumerate(house,start=0):
        if m >= number:
            print("House {} got {} presents.".format(i,m))
            return

    ## OLD ATTEMPT
    # elve_counter=0
    # elves=set()
    # print("goal:    {}".format(number))
    # biggest=0
    # while elve_counter < number:
    #     elve_counter+=1
    #     elves.add(elve_counter)
    #     visiting_elves = list(filter(lambda e: division_check(elve_counter, e), elves))

    #     gifts = sum(list(map(lambda n: n*10,visiting_elves)))
    #     biggest = gifts if gifts > biggest else biggest
    #     sys.stdout.write("current: {}{}".format(" "*(len(str(number))-len(str(biggest))),
    #                                             biggest))
    #     sys.stdout.flush()
    #     if gifts >= number:
    #         sys.stdout.write('\b'*(1+int(log(gifts))))
    #         print("House {} got {} presents.".format(elve_counter,gifts))
    #         break
    #     sys.stdout.write('\b'*(10+len(str(number))))


##########################################

class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    def print(self):
        print(self.x,self.y,self.value)

def generate(n):
    return (n*252533)%33554393

def day24():

    x = 1
    y = 1
    code = 20151125
    table=[]
    tic = time.perf_counter()
    while True:
        table.append(Point(x,y,code))
        code=generate(code)
        y+=1
        x-=1
        if x == 0:
            x=y
            y=1
        if x >= 6100:
            break

    x=0
    y=0
    toc = time.perf_counter()
    print(toc-tic)
    list = [[0 for j in range(1,3100)] for i in range(1,3100)]
    for point in table:
        if point.x == 2978 and point.y == 3083:
            print(point.value)

    toc = time.perf_counter()
    print(toc-tic)


if __name__ == '__main__':
    #day1(guides)
    #day2()
    #day3_1()
    #day3_2()
    #day4()
    #day5()

    #day20(29000000, False)
    #day20(290, True)
    
    #day24()