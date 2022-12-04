# Could make a variable to ask them for the file name to parse other files.
file = open("day1input.txt", "r")

elfCalories = []
currentElfCalories = 0

for line in file.readlines():
    # print(line.strip())

    strippedLine = line.strip()

    if strippedLine == "":
        # This is the blank spaces so we need to start again on a new elf
        elfCalories.append(currentElfCalories)
        currentElfCalories = 0
    else:
        # If we are on the same elf, we just convert the line to an int and add it to the current total.
        currentElfCalories += int(strippedLine)

# Max returns the largest value in a list - learned from ChatGPT
mostCaloricElfCalories = max(elfCalories)

print("The elf with the most calories has " + str(mostCaloricElfCalories) + " calories.")

# Part 2: Find the total calories of the top three elves.
elfCalories.remove(mostCaloricElfCalories)

secondMaxElfCalories = max(elfCalories)
elfCalories.remove(secondMaxElfCalories)

thirdMaxElfCalories = max(elfCalories)

topThreeTotalCalories = mostCaloricElfCalories + secondMaxElfCalories + thirdMaxElfCalories

print("The total calories of the top three elves is " + str(topThreeTotalCalories) + " calories.")

file.close()
