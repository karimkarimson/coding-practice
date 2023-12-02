import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
for line in data.split("\n"):
    # split each match
    red = 0
    green = 0
    blue = 0
    line_will_count = True
    for match in line.strip().split(":")[1].split(";"):
        for values in match.split(","):
            value = values.strip().split(" ")
            value[0] = int(value[0])

            if ((value [1] == "red") and (value[0] > red)):
                red = value[0]
            elif ((value [1] == "green") and (value[0] > green)):
                green = value[0]
            elif ((value [1] == "blue") and (value[0] > blue)):
                blue = value[0]

            if (((value[0] > 12) and (value[1] == "red")) or ((value[0] > 13) and (value[1] == "green")) or ((value[0] > 14) and (value[1] == "blue"))):
                line_will_count = False

    if line_will_count:
        addthis = int(line.split(" ")[1].split(":")[0])
        sum1 += addthis
    sum2 += red*green*blue

print(sum1)
print(sum2)