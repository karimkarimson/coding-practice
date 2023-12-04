import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")

winners = []
for game, line in enumerate(data):
    matches = []
    sepGame = line.split(':')
    allnumbers = sepGame[1].split('|')
    myNumbers = allnumbers[0].strip().split(' ')
    checkNums = [[],[]]
    for number in myNumbers: 
        if number != '': number = checkNums[0].append(int(number))

    winnerNumbers = allnumbers[1].strip().split(' ')
    for number in winnerNumbers:
        if number != '': number = checkNums[1].append(int(number))

    for number in checkNums[0]: 
        if number in checkNums[1]: 
            matches.append('m')

    if len(matches) > 0:
        point = 1
        if len(matches) > 1:
            point = (point + 1) ** (len(matches) - 1)
        winners.append(point)

for winner in winners:
    sum1 += winner

print(sum1)