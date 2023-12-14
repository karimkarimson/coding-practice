import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

sum1 = 0
sum2 = 0

class Graph:
    def __init__(self, value, x, y):
        self.v = value
        self.x = x
        self.y = y
        self.u, self.d, self.l, self.r = None, None, None, None

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has
lc = ["-", "L", "F"]
rc = ["-","J", "7"]
uc = ["|", "L", "J"]
dc = ["|", "F", "7"]
maxX = len(list(data[0])) - 1
maxY = len(data) - 1

graphs = []
for index_line, line in enumerate(data):
    for index_char, char in enumerate(line):
        graphs.append(Graph(data[index_line][index_char],index_line, index_char))
        # First add only left neighboor and upper neighboors
        if index_char > 0: 
            if graphs[-1].v in rc: 
                graphs[-1].l = graphs[-2] 

        if index_line > 0: 
            if graphs[-1].v in uc:
                graphs[-1].u = graphs[0 - (len(line) + 1)]
for i, graph in enumerate(graphs):
    if graph.v in lc and graph.x < maxX:
        graph.r = graphs[i + 1]
    if graph.v in dc and graph.y < maxY:
        graph.l = graphs[i + maxX]

print(graphs)



# for graph in graphs:
#     # now add right and down neighboors
#     if graph.l: 
#         if graph.l.value in lc:
#             graph.l.r = graph
#     if graph.u: 
#         graph.u.d = graph

# for nn in range(len(n)): n[nn] = int(n[nn])

# ns = [int(n[len(n) - nn - 1]) for nn in range(len(n))]
