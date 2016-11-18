# ICS 31, 5-24-16

# Let's play craps! Woooo!

'''
Rules (Passline bet)
http://casinogambling.about.com/od/craps/a/craps101.htm

- Roll two six-sided dice
    - Roll 7 or 11, "Natural" , you win.
    - Roll 2, 3, or 12, "Craps", you lose
    - Any other number becomes "the point"
        - For each successive roll:
            - Roll "the point", you win.
            - Roll 7 "crap out" - you lose.
            - Roll any other value, keep rolling...
'''

from random import randrange

def roll() -> int:
    ''' Roll two six-sided dice, return value (2 to 12)
    '''
    #return randrange(2,13) not every value has an equal chance
    return randrange(1,7) + randrange(1,7)

#for i in range(10):
#    print(roll())

def playGame() -> bool:
    ''' Play one round. Returns True if the player wins.
        Returns False otherwise. Print each step of the game.
    '''
    point = roll()
    print("First Roll:", point)
    if point in [7,11]:
        print("Natural: Shooter wins!")
        return True
    if point in [2,3,12]:
        print("Craps: Shooter loses")
        return False
    print("The point is:", point)
    while True:
        nextRoll = roll()
        print("Roll:", nextRoll)
        if nextRoll == 7:
            print("Crapped out. Shooter loses")
            return False
        elif nextRoll == point:
            print("Point! Shooter wins!")
            return True

print("Let's play some craps! Wooo!")

#playGame()

def isValidCommand(s: str) -> bool:
    ''' Returns True if s is 'y' or 'n', returns False otherwise.
    '''
    return s in ['y', 'n']

'''
while True:
    print("Your game:")
    result = playGame()
    print()
    print("Computer's game:")
    result = playGame()
    print()
    response = input("Play again? (y or n): ")

    # Check if the user response was valid...
    while not isValidCommand(response):
        response = input("Invalid command, please enter 'y' or 'n': ")

    if response == 'n':
        break
'''

'''
Sometimes , if you want to run simulations that are less interactive,
you can "batch" functionality.
- Good for programs such as simulations
    - Programs dependent on random events (and the outcome is different
    every time. Run a bunch of them to determine the generalized answer
    (Monte Carlo simulations).
'''

'''
playerWins = 0
computerWins = 0

for games in range(5):
    print("Your game:")
    result = playGame()
    if result:
        playerWins += 1
    print("Computer's game:")
    result = playGame()
    if result:
        computerWins += 1
    print()

print("player wins:", playerWins)
print("computer wins:", computerWins)
'''

# You can do other things such as computing the number of times
# a roll equals a value.

'''
diceTally = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 0,1 are not used.

for rolls in range(200):
    nextRoll = roll()
    diceTally[nextRoll] += 1

print("Roll Distribution Histogram")

for roll in range(2,13):
    print("{:2d}. {:3d} {}".format(roll, diceTally[roll],
                                   '#' * diceTally[roll]))
'''
# Using Dictionaries

# initialize dictionary values
D = {}
for i in range(2,13):
    D[i] = 0

for rolls in range(200):
    nextRoll = roll()
    D[nextRoll] += 1

print("Roll Distribution Histogram (using Dictionary)")
for roll in range(2,13):
    print("{:2d}. {:3d} {}".format(roll, D[roll],
                                   '#' * D[roll]))
