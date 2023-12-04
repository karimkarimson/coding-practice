import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")

# Graph Object holding value, coordinate and reference to neighboors
class Graph:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.l = None
        self.r = None
        self.u = None
        self.d = None

# Load data into List of Graphs
graphs = []
for index_line, line in enumerate(data):
    for index_char, char in enumerate(line):
        graphs.append(Graph(data[index_line][index_char],index_line, index_char))
        # First add only left neighboor and upper neighboors
        if index_char > 0: graphs[-1].l = graphs[-2] 
        if index_line > 0: graphs[-1].u = graphs[0 - (len(line) + 1)]

for graph in graphs:
        # now add right and down neighboors
    if graph.l: graph.l.r = graph
    if graph.u: graph.u.d = graph


winners = []
for graph in graphs:
    # functions to find start and endpoint of Number to then cast the String-Number to Integer
    def getStart(this):
        s = this
        if this.l: 
            if this.l.value.isnumeric(): 
                s = getStart(this.l)
        return s
    def getEnd(this):
        e = this
        if this.r:
            if this.r.value.isnumeric():
                e = getEnd(this.r)
        return e
    def getNumber(this):
        b = getStart(this)
        e = getEnd(this)
        number = 0
        while True:
            number = (number * 10) + int(b.value)
            if b == e: break
            b = b.r
        return [number, e]

    v = graph.value
    # check when Symbol if it touches any numbers
    if (v != "." and not v.isnumeric()):
        if graph.l.value.isnumeric(): winners.append(getNumber(graph.l))
        if graph.r.value.isnumeric(): winners.append(getNumber(graph.r))
        if graph.u.value.isnumeric(): winners.append(getNumber(graph.u))
        if graph.d.value.isnumeric(): winners.append(getNumber(graph.d))
        if graph.u.l.value.isnumeric(): winners.append(getNumber(graph.u.l))
        if graph.u.r.value.isnumeric(): winners.append(getNumber(graph.u.r))
        if graph.d.l.value.isnumeric(): winners.append(getNumber(graph.d.l))
        if graph.d.r.value.isnumeric(): winners.append(getNumber(graph.d.r))
        if v == "*":
            # find number-neighboors of '*'
            winners2 = []
            if graph.l.value.isnumeric(): winners2.append(getNumber(graph.l))
            if graph.r.value.isnumeric(): winners2.append(getNumber(graph.r))
            if graph.u.value.isnumeric(): winners2.append(getNumber(graph.u))
            if graph.d.value.isnumeric(): winners2.append(getNumber(graph.d))
            if graph.u.l.value.isnumeric(): winners2.append(getNumber(graph.u.l))
            if graph.u.r.value.isnumeric(): winners2.append(getNumber(graph.u.r))
            if graph.d.l.value.isnumeric(): winners2.append(getNumber(graph.d.l))
            if graph.d.r.value.isnumeric(): winners2.append(getNumber(graph.d.r))
            # clean out duplicate numbers
            for index, winner in enumerate(winners2):
                hold = 1
                while (index + hold < index + 4) and (index + hold < len(winners)):
                    while (index + hold < len(winners2)) and winners2[index + hold] == winner: winners2.pop(index + hold)
                    hold += 1
            # if '*' is touching exactly 2 numbers, multiply these and add to sum2
            if len(winners2) == 2: sum2 += (winners2[0][0] * winners2[1][0])


#cleanout duplicate numbers
for index, winner in enumerate(winners):
    hold = 1
    while (index + hold < index + 10) and (index + hold < len(winners)):
        while (index + hold < len(winners)) and winners[index + hold] == winner: winners.pop(index + hold)
        hold += 1

for winner in winners: sum1 += winner[0]
print(sum1)
print(sum2)