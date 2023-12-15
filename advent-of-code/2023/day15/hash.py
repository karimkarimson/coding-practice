import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample2"
# path = base + "/input"
data = open(path).read().strip()
data = data.split(",")
sum1 = 0
boxes = []
for i in range(len(data)):
    data[i] = list(data[i])
    val = 0
    for c in data[i]:
        val += ord(c)
        val *= 17
        val %= 256
    sum1 += val

    # Part 2
    box = 0
    for ii in range(len(data[i])):
        if data[i][ii] == "=" or data[i][ii] == "-": break
        box += ord(data[i][ii])
        box *= 17
        box %= 256

    try:
        d = data[i].index("=")
        boxNotInStack = True
        for b in boxes:
            if b[0][0] == box: 
                boxNotInStack = False
                # box exists, now check if same lensgroup exists
                for bb in range(1, len(b)):
                    isSame = True
                    if len(b[bb]) == len(data[i]):
                        for ii in range(len(b[bb]) - 2):
                            if b[bb][ii] != data[i][ii]:
                                isSame = False
                                break
                        if isSame: boxes[boxes.index(b)][b.index(b[bb])] = data[i]
                    if not isSame: boxes[boxes.index(b)].append(data[i])
        if boxNotInStack: 
            boxes.append([[box], data[i]])

    except:
        for b in boxes: 
            if b[0][0] == box: 
                for bb in b:
                    if len(bb) - 1 == len(data[i]):
                        isSame = True
                        for ii in range(len(bb) - 2):
                            if bb[ii] != data[i][ii]:
                                isSame = False
                                break
                        if isSame: b.pop(b.index(bb))
print(str(sum1))