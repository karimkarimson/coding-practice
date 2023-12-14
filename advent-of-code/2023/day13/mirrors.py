import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")
maps = [[]]
for d in data:
    if d: maps[-1].append(list(d))
    else: maps.append([])

def mirrors(map):
    rot = list(zip(*map[::-1]))
    half = round(len(map)/2)
    isMirror = True
    for ii in range(half -1, half + 2):
        isMirror = True
        if map[ii] != map[ii - 1]: 
            isMirror = False
        else:
            for i in range(ii):
                if i + ii > len(map) - 1: break
                if map[ii + i] != map[ii - i - 1]:
                    isMirror = False
                    break
        if isMirror: 
            return ii
    else: return 0



sum1 = 0
for m in maps: 
    sum1 += 100 * mirrors(m)
    sum1 += mirrors(list(zip(*m[::-1])))

print(sum1)
