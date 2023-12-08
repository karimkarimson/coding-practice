import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")
races = [[],[]]
for i, l in enumerate(data):
    l = l.split(" ")     
    l.pop(0)
    l = "".join(l).strip()
    races[i].append(int(l))

winners = 1
for d, time in enumerate(races[0]):
    distance = races[1][d]
    wins = 0
    for ms in range(1, time + 1):
        win = ((time - ms) * (ms))
        if win > distance: wins += 1
    winners *= wins

# data.split(" ")
print(winners)