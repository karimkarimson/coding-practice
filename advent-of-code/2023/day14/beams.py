import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")
map = []
for d in data: map.append(list(d))
# rot = list(zip(*map[::-1]))

def roll(column):
    try:
        start = column.index("O")
        try:
            cube = column.index("#")
            if cube < len(column) - 1:
                # split column and retry roll behind #
                splitted = column[cube + 1::]
                t = roll(splitted)
                column = column[:cube + 1:]
                column += t
                # column += roll(column[:cube:])
        except:
            # print("No # in row")
            cube = len(column)
    except:
        # print("No O in column")
        return column

    iO = []
    for i in range(cube):
        if column[i] == "O":
            placed = False
            for ii in range(cube - i):
                if placed: continue
                else:
                    if column[cube - ii - 1] == ".":
                        placed = True
                        column[cube - ii - 1] = "O"
                        iO.append(i)
                        column[i] == "t"
    for n in iO: column[n] = "."
    True
    return column

# sum1 = 0
rotations = 4 * 1000000
for l in range(rotations):
    rot = list(zip(*map[::-1]))
    # print(rot)
    for i, r in enumerate(rot):
        # print("*" * 80)
        # print(r)
        rolled = roll(list(r))
        rot[i] = rolled
        # print(rolled)
        # print("*" * 80)
    # if l == rotations - 1:
    sum1 = 0
    for rr in rot:
        # print(rr)
        for i, r in enumerate(rr):
            # print(rr)
            if r =="O": sum1 += i + 1
    # if l > 38 and (l + 1) % 10 == 0: 
    if (l) % 400000 == 0: 
        print("*" * 88)
        print("Rotation: " + str(l + 1))
        print(sum1)
    # for rr in rot:
    #     print(rr)
    # print("*" * 88)
    map = rot
# print(sum1)