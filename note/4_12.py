# ICS 31, 4-12-16


# Functions (Recap)

def double(n: int) -> int:
    '''
    Return two times the argument
    '''
    return 2 * n

def print_double(n: int) -> None:
    '''
    Print twice the argument
    '''
    print(2 * n)
    return

assert double(14) == 28
assert double(-1) == -2

#assert print_double(14) == 28

# Repetition and Loops

# It's common to do the same thing over-and-over-and-over again...

'''
intList = [2,4,8,16,32,64,128,256,512,1024]
exponent = 1

for x in intList:
    print("2 ^", exponent, "=", x)
    exponent += 1 # exponent = exponent + 1

print("out of loop")

for x in range(4): #[0, 1, 2, 3]
    print("Hello!" * x)

# While Loop
'''
'''
Syntax:
while BOOLEAN_EXPRESSION:
    BODY_OF_LOOP (1 or more statements

- If BOOLEAN_EXPRESSION is True, perform statements in BODY_OF_LOOP
- If BOOLEAN_EXPRESSION is False, skip the BODY_OF_LOOP.
'''
'''
x = 0

while x < 3:
    print(x)
    x += 1

print("out of loop")
'''

'''
# Break

x = 0
while True: # should loop forever
    x = x + 1
    print("Start of while body, x =", x)
    if x > 3:
        break
    print("End while body, x = ", x)

print("outside loop")

# Continue

x = 0
while True:
    x = x + 1
    print("Start of while body, x =", x)
    if x % 2 == 0: # if x is even
        continue
    if x > 5:
        break
    print("End of while body, x =", x)

print("Outside of loop")
'''

# RESTAURANTS PROGRAM
'''
Orgainization: Model - View.
View is the User Interface (UI) (the code that handles interactions with the user.
Model is the "back-end" that manages the "state" of the program
'''

MENU = """
Restaurant Collection Program - Enter one of the following:
a: Add a new restaurant to the collection
r: Remove a restaurant from the collection
s: Search the collection for a selected restaurants
p: Print all the restaurants
q: Quit
"""
'''
def handle_commands(RC: 'list of Restaurants') -> 'list of Restaurants':
    """
    Print menu, accepts commands from the user, maintains restaurants
    """
    while True:
        # let's test this in pieces...
        command = input(MENU)
        if command == "q":
            break
        else:
            print("You typed: ", command)
        
'''

def handle_commands(RC: 'list of Restaurants') -> 'list of Restaurants':
    '''
    Print menu, accepts commands from the user, maintains restaurants
    '''
    while True:
        # let's test this in pieces...
        command = input(MENU)
        if command == "q":
            break
        elif command == "a":
            #ask the user to enter restaurant info
            new_rest = Restaurant_get_info()
            RC
        elif command == "r":
            print("you typed r")
        elif command == "s":
            print("you typed s")
        elif command == "p":
            print("you typed p")
        else:
            print("Invalid command:", command, "\nPlease try again")
    return RC


# View (User Interface) portion:
def restaurants() -> None:
    '''
    Main Restaurants program: Creates and maintains a database of restaurants
    '''
    print("Welcome to the Restaurants program")
    print()
    our_rests = []
    our_rests = handle_commands(our_rests)
    print()
    print("Thank you. Goodbye")
    return

# MODEL (the 'back-end' or 'internal state')

from collections import namedtuple

Restaurant = namedtuple("Restaurant", "name cuisine phone dish price")
# note: dish is most famous and price is price of most famous dish

R1 = Restaurant("In-n-out", "American", "949-555-5555", "Double-double", 3.45)

print(R1)
print()

def Restaurant_to_str(R: Restaurant) -> str:
    '''
    Return a user-readable string of the restaurant
    '''
    return (
        "Name:      " + R.name + "\n" +
        "Cuisine:   " + R.cuisine + "\n" +
        "Phone:     " + R.phone + "\n" +
        "Dish:      " + R.dish + "\n" +
        "Price:     " + str(R.price) + "\n\n"
    )

print(Restaurant_to_str(R1))

restaurants()

