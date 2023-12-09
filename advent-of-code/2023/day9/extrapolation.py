import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

sum1 = 0
sum2 = 0

def getNext(array):
    allZ = True
    for n in array:
        if n != 0: allZ = False
    if allZ: 
        return array
    else: 
        nArray = []
        for n in range(len(array) - 1):
            nArray.append(array[n+1] - array[n])
        nextList = getNext(nArray)
        array.append(nextList[-1] + array[-1])
        return (array)

for line in data:
    n = line.split(" ")
    for nn in range(len(n)): n[nn] = int(n[nn])
    s = getNext(n)
    ns = [int(n[len(n) - nn - 1]) for nn in range(len(n))]
    ss = getNext(ns)
    sum1 += s[-1]
    sum2 += ss[-1]
print(sum1)
print(sum2)