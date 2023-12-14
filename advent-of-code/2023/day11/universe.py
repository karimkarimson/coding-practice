import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

class Graph:
    def __init__(self, value):
        self.v = value
        self.x, self.y, self.u, self.d, self.l, self.r = None, None, None, None, None, None

# Part 1 d2factor = 1
d2factor = 1
# Load data into List of Graphs
graphs, galaxies = [],[]
for index_line, line in enumerate(data):
    allSpace = True
    for index_char, char in enumerate(list(line)):
        if char == ".": graphs.append(Graph(1))
        if char == "#": 
            graphs.append(Graph("G"))
            galaxies.append(len(graphs) - 1)
            allSpace = False

        # First add only left neighboor and upper neighboors
        if index_char > 0: graphs[-1].l = graphs[-2] 
        if index_line > 0: graphs[-1].u = graphs[0 - (len(line) + 1)]
    
    if allSpace:
        for d in range(d2factor):
            for index_c, c in enumerate(list(line)): 
                graphs.append(Graph(1))
                if index_c > 0: graphs[-1].l = graphs[-2] 
                graphs[-1].u = graphs[0 - (len(line) + 1)]

for graph in graphs:
    # now add right and down neighboors
    if graph.l: graph.l.r = graph
    if graph.u: graph.u.d = graph

def doubleRowVertical(node):
    allSpaces = True
    if node.v == "G": return False
    else: 
        if node.d is not None:
            allSpaces = doubleRowVertical(node.d)
        return allSpaces

n = graphs[0]
while n is not None:
    allSpace = doubleRowVertical(n)
    if allSpace:
        for d in range(d2factor):
            s = n
            while s is not None:
                graphs.append(Graph(1))
                graphs[-1].l = s
                graphs[-1].r = s.r
                s.r.l = graphs[-1]
                s.r = graphs[-1]
                if s.u:
                    graphs[-1].u = s.u.l
                s = s.d

            while s is not None:
                node = s.r
                node.d = s.d.r
                s = s.d
            n = n.r
    n = n.r

def markX(node, count):
    node.x = count
    if node.r is not None:
        markX(node.r, count + 1)
def markY(node, count):
    node.y = count
    if node.d is not None:
        markY(node.d, count + 1)

n = graphs[0]
while n is not None:
    markY(n, 0)
    n = n.r
n = graphs[0]
while n is not None:
    markX(n, 0)
    n = n.d
x, y = 0, 0

sum1 = 0
for i, g in enumerate(galaxies):
    if i == len(galaxies) - 1: break
    startN = graphs[g]
    count = 0
    for p in range(i + 1, len(galaxies)):
        endN = graphs[galaxies[p]]
        diffX = endN.x - startN.x
        diffY = endN.y - startN.y
        steps = abs(diffX) + abs(diffY)
        sum1 += steps
        inG = galaxies.index(graphs.index(endN))
        # if ((i + 1 == 5) and (inG + 1 == 9)) or ((i + 1 == 1) and (inG + 1 == 7)) or ((i + 1 == 3) and (inG + 1 == 6)) or ((i + 1 == 8) and (inG + 1 == 9)):
        #     print("This Galaxy: " + str(i + 1) + " with Y: " + str(graphs[g].y) + " X: " + str(graphs[g].x) + " is " + str(steps) + " away from Galaxy " + str(inG + 1))
        count += 1
    # print("Y: " + str(graphs[g].y) + " X: " + str(graphs[g].x) + " has " + str(count) + " pairs")
        # sum1 += findWay(startN, endN)
print(sum1)

sum2 = 0