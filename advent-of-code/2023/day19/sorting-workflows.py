import os
base = os.environ["AOC_BASE"]
# Read File
# path = base + "/sample"
path = base + "/input"
data = open(path).read().strip()
data = data.split("\n")
workflows, parts = data[:data.index(""):] , data[data.index("") + 1::]

class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
class Workflow:
    def __init__(self, name, statements, miss):
        self.name = name
        self.statements = statements
        self.miss = miss

partlist = [ Part(*[int(n[n.index("=") + 1::]) for n in l.strip("{}").split(",")]) for l in parts]
tests = []
for l in workflows:
    name, cmds = l[:l.index("{"):], l[l.index("{") + 1::]
    cmds = cmds.strip("}").split(",")
    statements, miss = cmds[:-1:], cmds[-1::]

    for ii, s in enumerate(statements):
        test, dest = s[:s.index(":"):], s[s.index(":") + 1::]
        try: i = test.index("<")
        except: i = test.index(">")
        char, test, num = test[:i:], test[i], int(test[i + 1::])
        statements[ii] = [char, test, num, dest]
    tests.append(Workflow(name, statements, *miss))

# start = 0
for workflow in tests:
    if workflow.name == "in": start = workflow
winners = []
for p in partlist:
    test = start
    while True:
        match = False
        for s in test.statements:
            result = False
            dic = {"x": p.x, "m": p.m, "a": p.a, "s": p.s}
            if s[1] == "<":
                if dic[s[0]] < s[-2]: 
                    result = True
            else:
                if dic[s[0]] > s[-2]: result = True

            if result:
                match = True
                if s[-1] == "A": 
                    winners.append(p)
                    test = None
                    break
                if s[-1] == "R":
                    test = None
                    break
                for x in tests:
                    if x.name == s[-1]: 
                        test = x 
                        break
                break
        if test is None: break
        if match is False:
            if test.miss == "A": 
                winners.append(p)
                break
            elif test.miss == "R": break
            else:
                for x in tests:
                    if x.name == test.miss: 
                        test = x
sum1 = 0
for winner in winners:
    sum1 += winner.x + winner.m + winner.a + winner.s
    print(winner)
print(sum1)
