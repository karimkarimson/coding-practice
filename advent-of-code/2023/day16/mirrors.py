import os
base = os.environ["AOC_BASE"]
# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

# CREATE AND LOAD GRAPH
class Graph:
    def __init__(self, value, x, y):
        self.v = value
        self.x = x
        self.y = y
        self.u, self.d, self.l, self.r, self.energized = None, None, None, None, False
        self.touched = { "r": False, "l": False, "u": False, "d": False }
graphs = []
for i, line in enumerate(data):
    for ii, char in enumerate(line):
        graphs.append(Graph(char, ii, i))
        if ii > 0: 
            graphs[-1].l = graphs[-2] 
            graphs[-2].r = graphs[-1]
        if i > 0: 
            graphs[-1].u = graphs[0 - (len(line) + 1)]
            graphs[0 - (len(line) + 1)].d = graphs[-1]

# Beam that travels will yield new Node(s)
def beam(node, direction):
    node.touched[direction] = True
    node.energized = True
    # possible Situations and their results
    signs = { 
        ".": {
            "r": [node.r, "r"],
            "l": [node.l, "l"],
            "u": [node.u, "u"],
            "d": [node.d, "d"]
        },
        "/": { 
            "r": [node.u, "u"],
            "l": [node.d, "d"],
            "u": [node.r, "r"],
            "d": [node.l, "l"]
            }, 
        "\\": { 
            "r": [node.d, "d"], 
            "l": [node.u, "u"],
            "u": [node.l, "l"],
            "d": [node.r, "r"],
            }, 
        "-": {
            "r": [node.r, "r"],
            "l": [node.l, "l"],
            "u": [[node.r, "r"], [node.l, "l"]],
            "d": [[node.r, "r"], [node.l, "l"]]
            },
        "|": {
            "r": [[node.u, "u"], [node.d, "d"]],
            "l": [[node.u, "u"], [node.d, "d"]],
            "u": [node.u, "u"],
            "d": [node.d, "d"]
            }
    }

    nextNode = signs[node.v][direction]
    def isValid(n, d):
        if n is None: return [None, "s"]
        if n.touched[d]: return [None, "s"]
        else: return [n, d]

    if type(nextNode[0]) == list:
        for n in range(len(nextNode)):
            nextNode[n] = isValid(*nextNode[n])
    else: nextNode = isValid(*nextNode)

    return nextNode

# Part 2
def findBest(g, gg):
    # Clean up Graph
    for ggg in graphs:
        ggg.energized, ggg.touched["r"], ggg.touched["u"], ggg.touched["d"], ggg.touched["l"] = False, False, False, False, False

    # Let the Beam travel
    stack = [[g, gg]]
    while True:
        newStack = []
        for n in stack:
            nn = beam(*n)
            if type(nn[0]) == list:
                for nnn in nn:
                    if nnn[0] is not None: newStack.append(nnn)
            elif nn[0] is not None: newStack.append(nn)
        if newStack == []: break
        else: stack = newStack
    count = 0
    for ggg in graphs:
        if ggg.energized: count += 1
    return count

# start Beam from every Edge-Node/Leaf
values = []
node = graphs[0]
direction = "d"
while True:
    values.append(findBest(node, direction))
    directions = {"d": node.r, "l": node.d, "u": node.l, "r": node.u}
    if directions[direction] == graphs[0]: break
    elif directions[direction]: node = directions[direction]
    else: direction = {"d":"l", "l": "u", "u": "r"}[direction]
print(str(max(values)))


# Clean Up Graph for Part 1
for ggg in graphs:
        ggg.energized, ggg.touched["r"], ggg.touched["u"], ggg.touched["d"], ggg.touched["l"] = False, False, False, False, False

stack = [[graphs[0], "r"]]
while True:
    newStack = []
    for n in stack:
        nn = beam(*n)
        if type(nn[0]) == list:
            for nnn in nn:
                if nnn[0] is not None: newStack.append(nnn)
        elif nn[0] is not None: newStack.append(nn)
    if newStack == []: break
    else: stack = newStack

sum1 = 0
for g in graphs:
    if g.energized: sum1 += 1
print(sum1)