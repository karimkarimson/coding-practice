import os
base = os.environ["AOC_BASE"]
# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")

ranks = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
scores = [(len(ranks) - x) for x in range(1, len(ranks) + 1)]
hands, handrank = [],[]

for l in data:
    l = l.split(" ")
    hand, handcount = [],[]
    # create sorted hand, highest values First
    ohand = list(l[0])
    for r in ranks:
        for h in list(l[0]):
            if h == r: hand.append(h)
    # append bet to ordered hand
    # hands.append([hand, int(l[1])])
    hands.append([l[0], int(l[1])])

# For matching winner categories, we check for the amount of same card and amount of unique cards
    # check amount of Cards per value, per hand --> AA = 2  or KKK = 3
    for r in ranks:
        count = 0
        for h in hand:
            if h == r: count += 1
        handcount.append(count)
    count = max(handcount) # Find highest amount of same card per Hand
    if count == 5:
        True
    else:
        part2j = handcount[3]
        if part2j:
            if part2j == count:
                # j are most present card
                handcount[3] = 0
                n = max(handcount)
                if n:
                    handcount[handcount.index(n)] += part2j
            else: handcount[handcount.index(count)] += part2j

    # for part 2
    count = max(handcount)
    uniq = len(list(set(hand))) # how many unique cards per Hand

    # create a handscore for sorting:
    # Card-Value ** Position in [5, 4, 3, 2, 1]
    handscore = 0
    for i, h in enumerate(ohand):
        handscore += (scores[ranks.index(h)] ** 2) * (10 ** ((len(ohand) - i) * 100))
    handrank.append([handscore])

    # Five of a Kind
    if count > 4: handrank[-1].append("FO")
    #  4 of a kind
    elif count > 3: handrank[-1].append("FF")
    # 3 of a Kind TO or Full House FH
    elif count > 2:
        handrank[-1].append("TO") if uniq > 2 else handrank[-1].append("FH")
    # pair PA or two pair TP
    elif count > 1:
        handrank[-1].append("PA") if uniq > 3 else handrank[-1].append("TP")
    # High Card
    else: handrank[-1].append("HI")

ordered = []
# check hand for type of match and if multiple, then sort hand by handrank
lucky = ["FO","FF","FH","TO","TP","PA","HI"] #FiveOfakind, FouroFakind,FullHouse,ThreeOfakind..
for l in lucky:
    count = 0
    for i, hand in enumerate(hands):
        if handrank[i][1] == l:
            count += 1
            # append handscore for later sorting
            hand.append(handrank[i][0])
            ordered.append(hand)
    if count > 1:
        # in the same winning category are multiple games so the list of games needs to be sorted
        toCompare = []
        for c in range(count): toCompare.append(ordered.pop())
        newList = sorted(toCompare, reverse=True, key=lambda x: x[2])
        for c in range(count): ordered.append(newList[c])

# sum1 = 0
# ordered.reverse()
# for i in range(len(ordered)): sum1 += ordered[i][1] * (i + 1)
# print(sum1)
# print(sum1)
sum2 = 0
ordered.reverse()
for i in range(len(ordered)): sum2 += ordered[i][1] * (i + 1)
print(sum2)