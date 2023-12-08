import os
import copy
base = os.environ["AOC_BASE"]

# Read File
path = base + "/sample"
# path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")

seeds, seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location =[],[],[],[],[],[],[],[]
for i in range(len(data)):
    if data[i] != "":
        if data[i].startswith("seeds:"):
            w, numbers = data[i].split(":")
            seeds.append(numbers.strip().split(' '))

        def getNumbers(li):
            def getEOL(lineIndex):
                ii = 0
                if lineIndex + 1 < len(data): 
                    nextLine = data[lineIndex + 1]
                    if nextLine != "":
                        ii = getEOL(lineIndex + 1)
                    else: 
                        ii = (lineIndex + 1)
                else:
                    ii = lineIndex + 1
                return ii
            numbers = []
            for ii in range(getEOL(li) - li):
                round = []
                index = li + ii
                row = data[index].split(' ')
                for n in row: round.append(int(n))
                numbers.append(round)
            return numbers
            
        if data[i].startswith("seed-to-soil"): seed2soil.append(getNumbers(i + 1))
        if data[i].startswith("soil-to-fertilizer"): soil2fertilizer.append(getNumbers(i + 1))
        if data[i].startswith("fertilizer-to-water"): fertilizer2water.append(getNumbers(i + 1))
        if data[i].startswith("water-to-light"): water2light.append(getNumbers(i + 1))
        if data[i].startswith("light-to-temperature"): light2temperature.append(getNumbers(i + 1))
        if data[i].startswith("temperature-to-humidity"):temperature2humidity.append(getNumbers(i + 1))
        if data[i].startswith("humidity-to-location"): humidity2location.append(getNumbers(i + 1))

games = [seed2soil[0], soil2fertilizer[0], fertilizer2water[0], water2light[0], light2temperature[0], temperature2humidity[0], humidity2location[0]]

for pairs in range(int(len(seeds[0])/2)):
    seeds.append([int(seeds[0].pop(0)), int(seeds[0].pop(0))])
seeds.pop(0)

for round in range(len(games)):
    newPairs = []
    unchanged = []
    for c, line in enumerate(games[round]):
        for iPair, pair in enumerate(seeds):
                # are there any overlaps?
            if(pair[0] > (line[1] + line[-1])) or ((pair[0] + pair[1]) < (line[1])):
                # check if pair is already in newPairs and add if not
                unchanged.append(iPair)
                pairIsInNewPairs = False
                for newPair in newPairs:
                    if pair[0] == newPair[0] and pair[1] == newPair[1]: pairIsInNewPairs = False
                if pairIsInNewPairs: 
                    continue
                else: 
                    newPairs.append(pair)
            else:
                # Overlaps between list A and list B exist
                # 1. Calculate the overlap AB and transform Numbers accordingly
                # 2. Calculate (A - AB) and keep the leftover Seeds in the list

                # catch previous unchanged status
                # for i in len(unchanged):
                #     for s in len(seeds):
                #         l = len(unchanged) - i - 1
                #         toPop = []
                #         if unchanged[l] == seeds[l]:
                #             unchanged.pop(l)
                # if actual pair is in newPairs, it was sorted out before and should be removed now
                toPop = []
                pairIsInNewPairs = False
                for newPair in newPairs:
                    if pair[0] == newPair[0] and pair[1] == newPair[1]: pairIsInNewPairs = False
                if pairIsInNewPairs: toPop.append(i)
                for i in toPop:
                    newPairs.pop(toPop[len(toPop) - i - 1])

                startJoin = max(pair[0], line[1]) 
                # endJoin is a number representing the range
                endJoin = (min((pair[0] + pair[1]), (line[1] + line[-1])) - max(pair[0], line[1]))
                join = [startJoin, endJoin]
                # transform numbers and push new
                startIndex = startJoin - line[1]
                newPairs.append([line[0] + startIndex, endJoin])

                # is A = AB, meaning are all Seeds in the Testrange
                if (pair[0] >= line[1]) and ((pair[0] + pair[1]) <= (line[1] + line[-1])):
                    # all seeds have been translated and added
                    continue
                else: 
                    # Pairrange END is longer then Testrange, break the end of pair into new Pair
                    if pair[0] + pair[1] > startJoin + endJoin:
                        newPair = [startJoin + endJoin, (pair[0] + pair[1]) - (startJoin + endJoin)]
                        newPairs.append(newPair)

                    # Pairrange START is before Testrange, shorten Pairrange to startJoin
                    if pair[0] < startJoin:
                        pair[1] = startJoin - pair[0]
                        newPairs.append(pair)
    # toPop = []
    # for iii, newPair in enumerate(newPairs):
    #     if newPair[1] == 0: toPop.append(iii)
    # for iii in toPop: newPairs.pop(len(newPairs) - iii - 1)
    seeds = newPairs

winner = float('inf') 
for pair in seeds:
    if pair[0] < winner: winner = pair[0]
print(winner)