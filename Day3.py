import string
file = open("day3input.txt", "r")

alphabet = string.ascii_letters

priorityDict = {}

priority = 1
for char in alphabet:
    priorityDict[char] = priority
    priority += 1

priorityTotal = 0

for line in file.readlines():
    middle = len(line) // 2

    firstComp = line[:middle]
    secondComp = line[middle:]

    commonType = set(firstComp).intersection(set(secondComp))
    # Convert the common set to a string
    commonString = ''.join(map(str, commonType))
    priorityTotal += priorityDict.get(commonString)

print("The total priorities of the common item types is " + str(priorityTotal))

file.close()

# Part 2:
file = open("day3input.txt", "r")

lineCount = 1
lines = []
priorityTotalPart2 = 0

for line in file.readlines():
    if lineCount == 3:
        # If we are on the third line, we go back to 1 line so we can start the group search again. We also set the variables to nothing again.
        lineCount = 1
        commonSet = set(line.strip()).intersection(set(lines[0]), set(lines[1]))
        # Convert the common set to a string
        commonString = ''.join(map(str, commonSet))
        priorityTotalPart2 += priorityDict.get(commonString)

        lines.clear()
    else:
        lines.append(line.strip())
        lineCount += 1

print("The total priorities within a group of three is " + str(priorityTotalPart2))

file.close()
