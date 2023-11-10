
#Import random module for random die rolls 1-6, import mean to find average amount won
import random
from statistics import mean

# Constants for the game, numbers for a winning die roll and numbers that signify game over
winningNumbers = {4: 4, 5: 5, 6: 6}
gameOverNumbers = [1, 2, 3]

# Defining Variables, simulate 10,000 games of dice with constants starting at 0 prior to nested loop
games = 10000
nonZeroGames = 0
totalWinnings = 0
largestWinning = 0

# Nested loop needed for 10,000 dice rolls and two conditions that need to be met
for i in range(games):
    winnings = 0
    gameOver = False
    while not gameOver:
        roll = random.randint(1, 6)
        if roll in gameOverNumbers:
            gameOver = True
        else:
            winnings += winningNumbers[roll]
    if winnings > 0:
        nonZeroGames += 1
        totalWinnings += winnings
        if winnings > largestWinning:
            largestWinning = winnings

# Equations needed to find final output
probNonZero = nonZeroGames / games * 100
avgWinnings = mean([totalWinnings / nonZeroGames]) 

# Output of our simulation
print("Probability of a non-zero winning: ", round(probNonZero, 2),"%")
print("Average amount won: ", round(avgWinnings, 2))
print("Largest amount won: ", round(largestWinning, 2))

