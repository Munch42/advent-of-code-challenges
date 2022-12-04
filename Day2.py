file = open("day2input.txt", "r")

strategyGuide = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S"
}

choiceScoreGuide = {
    "R": 1,
    "P": 2,
    "S": 3,
}

totalScore = 0

for line in file.readlines():
    roundScore = 0

    strippedLine = line.strip()

    # The first column is always the first character while the second one is always a space away so the third character.
    firstColumn = strippedLine[0]
    secondColumn = strippedLine[2]

    firstColumnPlay = strategyGuide.get(firstColumn)
    secondColumnPlay = strategyGuide.get(secondColumn)

    roundScore += choiceScoreGuide.get(secondColumnPlay)

    # Draw Case:
    if firstColumnPlay == secondColumnPlay:
        roundScore += 3
        totalScore += roundScore
        continue

    # Win Case:
    win = False
    if secondColumnPlay == "R" and firstColumnPlay == "S":
        win = True
    elif secondColumnPlay == "P" and firstColumnPlay == "R":
        win = True
    elif secondColumnPlay == "S" and firstColumnPlay == "P":
        win = True

    # If win is still false, clearly the player has not had a winning case, nor a draw case and they must have lost.
    # We do not need to add anything if they lost since they get 0 points.
    if win:
        roundScore += 6

    totalScore += roundScore

print("My total score following the guide will be " + str(totalScore) + " points.")

file.close()
