import os
base = os.environ["AOC_BASE"]

# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()

sum1 = 0
sum2 = 0
data = data.split("\n")


seeds = []
seed2soil = []
soil2fertilizer = []
fertilizer2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []
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
                index = li + ii
                row = data[index].split(' ')
                numbers.append(data[index].split(' '))
            return numbers
            
        if data[i].startswith("seed-to-soil"): seed2soil.append(getNumbers(i + 1))
        if data[i].startswith("soil-to-fertilizer"): soil2fertilizer.append(getNumbers(i + 1))
        if data[i].startswith("fertilizer-to-water"): fertilizer2water.append(getNumbers(i + 1))
        if data[i].startswith("water-to-light"): water2light.append(getNumbers(i + 1))
        if data[i].startswith("light-to-temperature"): light2temperature.append(getNumbers(i + 1))
        if data[i].startswith("temperature-to-humidity"):temperature2humidity.append(getNumbers(i + 1))
        if data[i].startswith("humidity-to-location"): humidity2location.append(getNumbers(i + 1))

games = [seed2soil, soil2fertilizer, fertilizer2water, water2light, light2temperature, temperature2humidity, humidity2location]

for pairs in range(int(len(seeds[0])/2)):
    seeds.append([int(seeds[0].pop(0)), int(seeds[0].pop(0))])
seeds.pop(0)

locationNumbers= []
for iPair, pair in enumerate(seeds):
    seedlist = []
    for ss in range(pair[-1]): seedlist.append((int(pair[0]) + ss))

    for round in range(len(games)):
        for iSeed, seed in enumerate(seedlist):
            for line in games[round][0]:
                if ((seed >= int(line[1])) and (seed <= (int(line[1]) + int(line[-1])))):
                    seedlist[iSeed] = seed - int(line[1]) + int(line[0])
                    print("seed " + str(seed) + " will be " + str(int(seed) - int(line[1]) + int(line[0])))
                    break
    locationNumbers.append(seedlist)

# winners = []
# for game in seeds:
#     winners.append(min(game))
locationList = []
for i in range(len(locationNumbers)):
    for ii in range(len(locationNumbers[i])): locationList.append(locationNumbers[i].pop())


print(min(locationList))