import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")
