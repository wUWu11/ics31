# Truong Tran 76992464 and Deyu Wu 0952612 . ICS 31 Lab sect 3. JUNKUYL.

# RESTAURANT COLLECTION PROGRAM


# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 n:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 c:  Change prices for the dishes served
 s:  Search the collection for selected restaurants
 d:  Search a dish in Restaurants collection
 c:  Search a cuisine and display average price
 p:  Print all the restaurants
 e:  Remove (erase) all the restaurants from the collection
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        
        if response=="q":
            return C
        elif response == 'c':
            n = input("Please enter the name of cuisine to search :")
            for r in Collection_search_cuisine(C,n):
                print(Restaurant_str(r))
                print("average price:${}, Average calories:{}".format(average_price(r),average_calories(r)) )
        elif response == 'd':
            n = input('Please enter the name of dish')
            for i in Dish_search_by_name(C,n):
                print(Restaurant_str(i))
        elif response=='n':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
            print("average price:${}, Average calories:{}".format(average_price(r),average_calories(r) ) )
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
            for i in C:
                print("average price:${}, Average calories:{}".format(average_price(i),average_calories(i) ) )
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response=='e':
            C = Collection_remove_all(C)
        elif response=='c':
            n = float(input('Please enter the amount representing a percentage change in price'))
            C = Collection_change_price(C,n)
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Menu:     " +str( self.menu) + "\n" )

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())


#### DISH
Dish = namedtuple('Dish','name price calories')

def Dish_str(a:Dish)->str:
    '''takes a Dish object and returns string in form of name (price): calories'''
    return a.name + "($"+ str(a.price) +"):" + str(a.calories)

def Dish_get_info()-> Dish:
    '''Promopt user for fields of Dish; create and return.
    '''
    return Dish(
        input('Please enter the Dish name'),
        float(input('Please enter the price of that dish')),
        input('Please enter the calories this dish contain'))

def Dish_search_by_name(C:list,name:str)->list:
    result = []
    for i in C:
        for r in i.menu:
            if name in r.name:
                result.append(i)
    return result


def average_price(a:Restaurant):
    total = 0
    num = len(a.menu)
    for i in a.menu:
        total += float(i.price)
    return total/num

def average_calories(a:'list of Resaurant'):
    total = 0
    num = len(a.menu)
    for i in a.menu:
        total += float(i.calories)
    return total/num
        
    

#### MENU
def Menu_enter():
    result = []
    
    
    while True:
        a = input('Please enter "yes" if you want to add a dish or enter "no"')
        if a =='yes':
            result.append(Dish_get_info())
            
        elif a == 'no':
            break
    return result
    

#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result

def Collection_search_cuisine(C:list,name:str)-> list:
    result = []
    for i in C:
        if i.cuisine == name:
            result.append(i)
    return result

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result

def Collection_remove_all(C:list) ->None:
    '''remove all Restaurant in Collection
    '''
    result = []
    return result

def Collection_change_price(a:'list of Restaurant',number:float)->'list of restaurant':
    '''takes a list of Restaurant and a number, return a list of Restaurant
        whose prices has changed by number percentage
    '''
    result = []
    for i in a:
        result.append(Restaurant_change_price(i,number))
    return result

def Restaurant_change_price(a:Restaurant,number:float)->Restaurant:
    '''take a Restaurant and return price increse by the number percentage
    '''
    a = a._replace(price =a.price*(1+number/100))
    return a

restaurants()
