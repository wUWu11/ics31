# ICS 31, 5-3-16

# continuing on text formatting...

price = 1.50
item = "chocolate"

print("price = $", price, sep="")
print("price = $", price, sep="", end="")
print("end of print statements")

# .format method

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
d1 = Dish("Rainbow Roll", 100001.50, 300)

# We want to display this info as [DISH_NAME] $[PRICE]: [CALORIES] calories
print("{} (${}): {} calories".format(d1.name, d1.price, d1.calories))
print("{} (${:5.2f}): {} calories".format(d1.name, d1.price, d1.calories))
print("{} (${:15.3f}): {} calories".format(d1.name, d1.price, d1.calories))


'''
FILES

- Programming languages have a lot of tools for use
    - Some allow you to solve the same problem in slightly different
    ways.
    - Some ways are more obvious than others.

- Different tools allow us to solve new kinds of problems
    - For example, lists allow us to keep track of and modify
    a collection of data
- Some tools just let us do things differently

for i range(10):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

Today, we'll be talking about a new tool: FILES

- FILES gives us PERSISTENCE
    - So far, we're rerun our code and between each run,
    our data is cleared and everything has to be re-entered
    again.
    - With PERSISTENCE, our data can be "saved" between each
    program execution.

FILE BASICS
    - We can read from files
    - We can write to files.
    - We can store files in many different forms
        - Example: .xls, .docx, .pdf, .txt, .jpg
        - For this class, we'll deal with "plain text" (.txt) files
        - in .txt files, characters are represented in something
        called ASCII (American Standard Code for Information
        Interchange).
        - This was a dominant / simple way to represent text where
        each character is 8 bits (1 byte) long.
        - UTF-8, the most popular format in web browsers
        allows between 1 - 4 bytes per character
    - File: a document
    - Directory: A folder containing files and other folders
    - File System: Collection of all files and folders on the computer
    - For this class, we'll deal with reading / writing files
    that are in the same folder as your .py file.
        - This is known as our "working" directory

FILE I/O:
    - I/O stands for Input / Output
    - We read data from a file into our program.
    - We write data from our program into a file.
    STEPS:
    1. Open the file (creates a "connection" between your program
    and the file).
        - Choose if the connection is meant for reading or writing
    2. Read the data or write the data
    3. Close the file (close the "connection"). This needs to be
    done once per file.
'''

'''
infile = open("example.txt", "r")

data = infile.read()
print(data)
infile.close()


outfile = open("example2.txt", "w") # we could use 'a' to append
outfile.write(data)
outfile.close()


# Create a list of lines in the file
infile = open('example.txt', 'r')
data = infile.read()
datalines = data.split('\n')
print(datalines)
infile.close()


Common ways to read data from files

1. read() - Reads the entire file into one string
    a. Good for small data (large files may be too big to store
    into memory)
    b. Bad - you have to write the algorithm for parsing
2. read(n) - Reads the next n characters from the input
    a. Good for larger files since you only have to store n characters
    at a time
3. readline() - Read everything from the current position to
    the next \n (or the the end of file (EOF)).
4. readlines() - Reads all lines in the file and stores them in
    a list.
5. for a_line in inFile:
    a. a_line represents a line in the file


# Example copying / writing from a file to another
infile = open('example.txt', 'r')
outfile = open('copy.txt', 'w')

for line in infile:
    outfile.write(line)

infile.close()
outfile.close()

'''

# RESTAURANT COLLECTION PROGRAM
# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    choice = ("if you'd like to read restaurants from an existing " +
              "file, type the name of that file. If not, just hit " +
              "RETURN: ")
    filename = input(choice)

    if filename == "":
        our_rests = Collection_new()
    else:
        our_rests = fill_collection_from_file(filename)
    #our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    write_file_from_collection(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return (
        "Name:     " + self.name + "\n" +
        "Cuisine:  " + self.cuisine + "\n" +
        "Phone:    " + self.phone + "\n" +
        "Dish:     " + self.dish + "\n" +
        "Price:    ${:2.2f}".format(self.price) + "\n\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        input("Please enter the name of the best dish:  "),
        float(input("Please enter the price of that dish:  ")))

def Restaurant_to_tabbed_string(r: Restaurant) -> str:
    ''' Return a string containing the restaurant's fields,
        separated by tabs '''
    return (r[0] + '\t' + r[1] + '\t' + r[2] + '\t' + r[3] + '\t' +
            str(r[4]))

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
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

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
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]

def fill_collection_from_file(filename: str) -> 'list of Restaurant':
    ''' Read restaurant info from file. return the collection.
        File has one line for each restaurant, with fields
        separated by tabs
    '''
    result = []
    infile = open(filename, 'r')
    for line in infile:
        field_list = line.split('\t')
        new_rest = Restaurant(field_list[0], field_list[1],
                              field_list[2], field_list[3],
                              float(field_list[4]))
        result.append(new_rest)
    infile.close()
    return result

def write_file_from_collection(C: 'list of Restaurant') -> None:
    ''' Write file called 'restaurant.txt', tab-delimited
    '''
    outfile = open('restaurant.txt', 'w')
    for r in C:
        outfile.write(Restaurant_to_tabbed_string(r) + "\n")
    outfile.close()
    return


restaurants()
