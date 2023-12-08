import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
# path = base + "/sample2"
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
    
noEnd = True
steps = 0
node = 'AAA'
goal = 'ZZZ'
while noEnd:
    for d in directions:
        inode = nodes.index(node)
        refs = references[inode]
        if d == 'L': node = refs[0]
        if d == 'R': node = refs[1]
        steps += 1
        if node == goal:
            noEnd = False
            break

print(steps)