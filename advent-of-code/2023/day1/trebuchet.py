import os
base = os.environ["AOC_BASE"]

# Read File
path = base + "/advent-of-code/2023/day1/sample"
data = open(path , "r")
lines = data.readlines()

# function to find all occurences of a substring in a string
# def find_all(string, substring):
#     start = 0
#     while True:
#         start = string.find(substring, start)
#         if start == -1: return
#         yield start
#         start += 1

# Clean Up List of Strings
iterator = 0
numbersPerLine = []
for line in lines:
    line = line.strip()
    lines[iterator] = line
    iterator += 1

    # Convert Number-Words to Integers
    numberWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    holder = []
    for word in numberWords:
        if word in line:
            # find all occurences of the number-word in the line and save all in a list
            res = [i for i in range(len(line)) if line.startswith(word, i)]
            res.append(numbers[numberWords.index(word)])
            holder.append(res)

    # Insert the Numbers at the indices
    offset = 0
    index = 1
    for pairs in holder:
        number = numberWords[pairs[-1]-1]
        for indices in pairs[:-1]:
            # as more numbers are added, the indices need to be adjusted
            line = line[:indices + offset] + str(pairs[-1]) + line[indices + offset:]
            offset += index

    # Catch all Numbers from each Line
    lineNumbers = []
    for letter in line:
        isnumber = letter.isnumeric()
        if isnumber:
            lineNumbers.append(int(letter))

    # Append each list of Numbers per Line to the list 'numbersPerLine'
    numbersPerLine.append(lineNumbers)

# Now Calculate the Sum
iterator = 0
sum = 0
for line in numbersPerLine:
    # If the line contains only one number X then add another X to the line so that the line is now [X, X]
    if len(line) == 1:
        line.append(line[0])

    # Take the first Number of the line and multiply it by 10 and add the second number to it [2, 5] -> 25
    lineNumber = (line.pop(0) * 10) + line.pop()
    sum += lineNumber

print(sum)