# As solved by jonathanpaulson on GitHub https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/1.py
import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/advent-of-code/2023/day1/sample"
data = open(path).read().strip()

p1 = 0
p2 = 0
for line in data.split("\n"):
    p1_digits = []
    p2_digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        for d, number in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]):
            if line[i:].startswith(number):
                p2_digits.append(str(d + 1))
                break
    p1 += int(p1_digits[0] + p1_digits[-1])
    p2 += int(p2_digits[0] + p2_digits[-1])

print(p1)
print(p2)