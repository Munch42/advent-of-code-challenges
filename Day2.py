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

strategyGuidePart2 = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "L",
    "Y": "D",
    "Z": "W"
}

def switch(x):
    # Return the amount of points that you earn based on if you lose, draw, or win.
    return {
        'L': 0,
        'D': 3,
        'W': 6
    }.get(x, 0)

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

# Part 2:
file = open("day2input.txt", "r")
totalPart2Score = 0

for line in file.readlines():
    roundScore = 0

    strippedLine = line.strip()

    # The first column is always the first character while the second one is always a space away so the third character.
    firstColumn = strippedLine[0]
    secondColumn = strippedLine[2]

    firstColumnPlay = strategyGuidePart2.get(firstColumn)
    secondColumnPlay = strategyGuidePart2.get(secondColumn)

    roundScore += switch(secondColumnPlay)

    # Win Case
    if secondColumnPlay == "W":
        # If we win, then we must find the one that wins against the opponent's choice.
        if firstColumnPlay == "R":
            roundScore += choiceScoreGuide.get("P")
        elif firstColumnPlay == "P":
            roundScore += choiceScoreGuide.get("S")
        elif firstColumnPlay == "S":
            roundScore += choiceScoreGuide.get("R")

    # Lose Case
    elif secondColumnPlay == "L":
        # If we lose, then we must find the one that loses to the opponent's one.
        if firstColumnPlay == "R":
            roundScore += choiceScoreGuide.get("S")
        elif firstColumnPlay == "P":
            roundScore += choiceScoreGuide.get("R")
        elif firstColumnPlay == "S":
            roundScore += choiceScoreGuide.get("P")

    # Draw Case
    elif secondColumnPlay == "D":
        # If in a draw, we must choose the same so we look at the first column and get the score for that.
        roundScore += choiceScoreGuide.get(firstColumnPlay)

    totalPart2Score += roundScore

print("My total score following the updated guide is " + str(totalPart2Score) + " points.")

file.close()
