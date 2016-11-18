# ICS 31, 4-14-16

from collections import namedtuple

Restaurant = namedtuple("Restaurant", "name cuisine phone dish price")

R1 = Restaurant("In-n-out", "American", "949-555-5555", "Double-double", 3.45)
R2 = Restaurant("Thai Corner", "Thai", "800-123-4567", "Pad Thai", 9.00)
R3 = Restaurant("Maizuru", "Japanese", "714-555-5555", "Rainbow Roll", 11.00)

TRC = [R1, R2, R3] # The restaurant collection
L = [3, 18, 50, 2, 300, 31, 35]

'''
print(L)
L.sort()
print(L)


# Sorts the numbers in reverse order
print(L)
L.sort(reverse=True)
print(L)


# Sorting namedtuples by their first field - name
print()
print(TRC)
TRC.sort()
print()
print(TRC)
'''

# We can specify what field we want to sort by passing in an additional
# parameter to the sort method.

def get_price(R: Restaurant) -> float:
    ''' Returns the price of the Restaurant
    '''
    return R.price

'''
print(TRC)
print()
TRC.sort(key=get_price, reverse=True)
print(TRC)


print("Testing sorted(). TRC = ")
print(TRC)
new_list = sorted(TRC, key=get_price, reverse=True)
print("\nSorted version:")
print(new_list)
print("\nOriginal version:")
print(TRC)

print()

# Print just the prices of the sorted list:
for r in new_list:
    print(r.price)


# Return just a list of sorted prices
result = []
for r in new_list:
    #result = result + [r.price]
    result.append(r.price)

print(result)
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
            # add new restaurant to the collection
            RC = Collection_add(RC, new_rest)
        elif command == "r":
            # ask the user to remove the restaurant based off its name
            n = input("Please enter the name of restaurant to remove:")
            RC = Collection_remove_by_name(RC, n)
        elif command == "s":
            # ask the user to enter restaurant name to search for
            n = input("Please enter the name of the restaurant to search: ")
            matches = Collection_search_by_name(RC, n)
            print(Collection_to_str(matches))
        elif command == "p":
            # print collection in a nice human-readable format
            print(Collection_to_str(RC))
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

Restaurant = namedtuple("Restaurant", "name cuisine phone dish price")
# note: dish is most famous and price is price of most famous dish

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

def Collection_to_str(C: 'list of Restaurants') -> str:
    ''' Return a string representing the collection C
    '''
    result = ""
    for r in C:
        result = result + Restaurant_to_str(r)
    return result


def Restaurant_get_info() -> Restaurant:
    ''' Prompt the user for fields of a restaurant, create it, and return
    '''
    n = input("Please enter restaurant's name: ")
    c = input("Please enter the kind of food served: ")
    ph = input("Please enter the phone number: ")
    d = input("Please enter the best dish: ")
    p = input("Please enter the price of that dish: ")
    return Restaurant(n, c, ph, d, float(p))


def Collection_add(C: 'list of Restaurants', r: Restaurant) -> 'list of restaurant':
    '''
    Return list of restaurants with r added to it
    '''
    return C + [r]


def Collection_remove_by_name(C: 'list of Restaurants', to_remove: str) -> 'list of Restaurants':
    ''' Resturn list with the named restaurant (to_remove) deleted
    '''
    result = []
    for r in C:
        if r.name != to_remove:
            result.append(r)
    return result



def Collection_search_by_name(C: 'list of Restaurants', looking_for: str) -> 'list of Restaurants':
    ''' Return a collection containing those restaurants in C
        that match the looking_for parameter
    '''
    result = []
    for r in C:
        if r.name == looking_for:
            result.append(r)
    return result

restaurants()
