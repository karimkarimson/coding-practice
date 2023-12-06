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

def getFactors(round):
    factors = []
    for categorie in games:
        table = [[],[]]
        for i in range(len(categorie[round])):
            for ii in range(int(categorie[round][i][-1])):
                table[0].append(int(categorie[round][i][0]) + ii)
                table[1].append(int(categorie[round][i][1]) + ii)
        factors.append(table)
    return factors 

for i, game in enumerate(seeds):
    factors = getFactors(i)
    for round in range(len(games)):
        for iSeed, seed in enumerate(seeds[i]):
            try:
                ii = factors[round][1].index(int(seed))
                print("seed " + str(seed) + " will be " + str(factors[round][0][ii]))
                seeds[i][iSeed] = factors[round][0][ii]
            except:
                continue

winners = []
for game in seeds:
    winners.append(min(game))
     
print(min(winners))