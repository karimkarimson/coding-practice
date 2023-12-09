import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
# path = base + "/sample2"
# path = base + "/sample3"
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")

directions = list(data[0].strip())

nodes = []
references = []
for i in range(2, len(data)):
    node, refs = data[i].split("=")
    refs = refs.split(",")
    for ii, ref in enumerate(refs):
        ref = filter(lambda c: c.isalpha(), list(ref.strip()))
        ref = "".join(ref)
        refs[ii] = ref

    nodes.append(node.strip())
    references.append(refs)

# tries = 12737
tries = 1
snodes = list(filter(lambda s: s[-1] == "A", nodes))
pathlengths = []
diffs = []
for i, node in enumerate(snodes):
    steps = 0
    noEnd = True
    pathlengths.append([])
    while noEnd:
        for d in directions:
            inode = nodes.index(snodes[i])
            refs = references[inode]
            if d == 'L': snodes[i] = refs[0]
            if d == 'R': snodes[i] = refs[1]
            steps += 1
            if snodes[i].endswith("Z"):
                pathlengths[i].append(steps)
                if len(pathlengths[i]) > tries:
                    noEnd = False
                    break
    for n in range(len(pathlengths[i]) - 1):
        diffs.append(pathlengths[i][n + 1] - pathlengths[i][n])

noEnd = True
div = 2
divs = []
while noEnd:
    didDivide = False
    for i, node in enumerate(diffs):
        if node % div == 0: 
            diffs[i] = int(node/div)
            didDivide = True
    if didDivide: divs.append(div)

    goOn = False
    for d in range(len(diffs) - 1):
        if diffs[d] != 1:
            goOn = True
    if goOn:
        div += 1 
    else:
        noEnd = False

lcm = 1
for i in range(len(divs)):
    lcm = lcm * divs[i]

print(lcm)