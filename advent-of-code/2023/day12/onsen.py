# so far i didnt find a good strategy to tackle this
import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

def tryPools(line, numbers):
    count = 0
    isTry = False
    for i, c in enumerate(line):
        if c == "?" or "#":
            # insert/account #
            numbers[0] -= 1
            if numbers[0] == 0 and (line[i + 1] in ["?", "."]):
                # This is a possibility
                if len(numbers) == 1:
                    # reached end of numbers so rest will be possibilities
                count = 1
                count += tryPools(line[i + 2::], numbers.pop(0))
                return count
            elif numbers[0] > 0:
                count += tryPools(line[1::], numbers)



for l in data:
    line, numbers = l.split(" ")
    line = list(line)
    numbers = numbers.split(",")
    for n, nn in enumerate(numbers):
        numbers[n] = int(nn)
    print(line)
    print(numbers)