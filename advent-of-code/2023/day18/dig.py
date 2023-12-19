import os
base = os.environ["AOC_BASE"]
# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

while True:
    x = input("Pack dein X Wert rein: ")
    if x == "e": break
    print(str(float(x)**2 + 4 * float(x)))