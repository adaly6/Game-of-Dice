"""
Created on Thu Feb 16 18:50:13 2023

Andrew Daly, Jacob Weisshaar

The purpose of this code is for assignment 1 in Computational Thinking. 
This is a simulation of a simple game of dice. Numbers that signify game over on the dice
are 1, 2, and 3. When these numbers are rolled, the game ends. Numbers 4, 5, and 6
signify the amount won by the player ($4, $5, or $6). The player may keep rolling until 
game over numbers are rolled. Through 10,000 simulations of the game, we track the 
average amount won, the probability that the game ends with a non-zero amount, and
the largest amount won for a single game.

"""

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


"""

- Statistically, it is at least 50% likely to win $4 or more dollars
when playing this game. 

- Based on the output of 10,000 simulated die rolls, we would pay 
$3 to play this game because the average amount won was greater than $3
and there is a 50% to win $4 or more on the first roll and any roll thereafter.

"""


