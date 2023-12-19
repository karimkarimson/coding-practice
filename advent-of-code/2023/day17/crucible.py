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
        self.u, self.d, self.l, self.r = None, None, None, None
graphs = []
for i, line in enumerate(data):
    for ii, char in enumerate(line):
        graphs.append(Graph(int(char), ii, i))
        if ii > 0: 
            graphs[-1].l = graphs[-2] 
            graphs[-2].r = graphs[-1]
        if i > 0: 
            graphs[-1].u = graphs[0 - (len(line) + 1)]
            graphs[0 - (len(line) + 1)].d = graphs[-1]

def pushOneWay(node, direction, counter, heatloss):
    directions = {
        "r": node.r, "l": node.l, "d": node.d, "u": node.u
    }
    node = directions[direction]
    if node is None: return [None, "s", counter, heatloss]
    return [node , direction, counter, heatloss + directions[direction].v]

counter, score = 0, 0
distance = (graphs[-1].x - graphs[0].x) + (graphs[-1].y - graphs[0].y)
stack = [[graphs[0], "r", counter, score], [graphs[0], "d", counter, score]]
end = graphs[-1]
winners = [ float('inf') ]
while True:
    newStack = []
    for s in stack:
        d = ["r", "l", "u", "d"]
        # node = s
        for dd in d:
            n = pushOneWay(*s)
            # reached end node?
            if n[0] == end and n[-1] < min(winners): 
                winners.append(n[-1])
            elif dd != s[1]: # move in all possible directions
                if n[0] is not None and n[-1] < (distance * 9):
                    n[1] = dd
                    n[-2] = 0
                    newStack.append(n)
            elif n[0] is not None: # actual direction should be kept max 3 times
                if n[-2] + 1 < 3: 
                    n[-2] += 1
                    newStack.append(n)
    if newStack == []: break
    sum = 0
    for l in newStack: sum += l[-1]
    m = round(sum / len(newStack))
    stack = []
    for l in newStack: 
        if l[-1] < m: stack.append(l)
        
    # stack = newStack

print(min(winners))