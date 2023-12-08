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

noEnd = True
steps = 0
snodes = list(filter(lambda s: s[-1] == "A", nodes))

while noEnd:
    for d in directions:
        for i, node in enumerate(snodes):
            inode = nodes.index(node)
            refs = references[inode]
            if d == 'L': snodes[i] = refs[0]
            if d == 'R': snodes[i] = refs[1]
        steps += 1

        allEndZ = True
        for node in snodes:
            if not node.endswith("Z") : allEndZ = False

        if allEndZ:
            noEnd = False
            break

print(steps)