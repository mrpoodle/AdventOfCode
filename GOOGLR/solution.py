def solution(n, b):
    y = sorted(str(n))  # remove, you do the same later

    def cleanx(x):
        x = sorted(str(n), reverse=True)
        x = int("".join(x), b)
        x = str(x)
        x = list(x)  # strings also have len() so you don't need this
        while len(x) <= len(str(n)):
            x.append('0')

        return int("".join(x))  # if you dont convert to list, no need to join

    if b == 10:  # why only for 10? it can happen for all
        x = cleanx(n)
    else:
        x = sorted(str(n), reverse=True)
        x = int("".join(x), b)
    print(x, "x")
    nID = 0
    # ynum = 0
    # zmod = 0
    # trsy = []
    # sq = []
    # stlist = 0
    # index = 0
    idlist = []
    y = sorted(str(n))
    y = int("".join(y), b)
    z = x-y
    # zc = z
    print(x, y, z)

    def translate(z):
        zc = z  # you could just work with z
        ztra = []
        print(zc)
        while zc > 0:
            zmod = zc % b
            zc = int(zc/b)  # YOU NEED TO ROUND DOWN HERE. INT DOES THAT
            ztra.insert(0, str(zmod))  # CONVERT TO STRING HERE, THEN JOIN
        ztra = "".join(ztra)  # AS PROPOSED BEFORE
        return ztra

    # loop... what to do... Take translated ID, make x,y, make new ID log the
    # ID into the list.
    # while Id in list.... so I need to renew the ID every time to check.
    # while nID not in idlist:
    for fd in range(5):
        nID = (translate(z))
        print(int(nID), "translated")
        if len(nID) == len(str(n)):
            x = sorted(str(nID), reverse=True)
            x = (int("".join(x), b))
        else:
            x = cleanx(x)

        print(x)
        y = sorted(str(nID))
        y = int("".join(y), b)
        z = x-y
        idlist.append(translate(z))
        print(x, y, translate(z), "last line", idlist)

# sort and translate to 10 (V)
# translate to b


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


# print(solution_minion("210022", 3))
# solution(210022, 3)
