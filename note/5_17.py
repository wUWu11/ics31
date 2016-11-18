# ICS 31, 5-17-16

'''
Recap:
- We've been using some basic tools in Python to help with solving various
problems.
    - Break up our problem into Actions:
        - Create functions, control structures, ...
    - Appliy actions to objects
        - assignments, operations, types: int, str, float, etc.

    - Object Oriented Programming
        - Representation of things and algorithms to manipulate them.
        - We've been doing this with namedtuples.
    - If we choose the right data structure, code can be A LOT easier to write.

Today: 2-dimensional lists.
   - Normal lists: One number to index an item
       - L = [0,1,2] , L[1] == 1
   - Table (matrix): will take two numbers (two dimensions), represented with a
       row and column.

Conceptual Example:
- Computer screens is basically a Grid of pixels.
- Basic color screens have color values (RGB - Red, Green, Blue)
- Monochrome screens (black and white pixels).
'''

# Recall multiplication of lists
#print([0,1] * 10)

def new_screen(rows: int, columns: int) -> '2D list':
    '''
    Create and return an empty screen: a list of rows with each row
    being a list of pixels going across that row. Initially, all pixels will be 0
    (black).
    '''
    result = []
    for r in range(rows):
        result.append([0] * columns)
    return result

assert new_screen(4,2) == [ [0,0], [0,0], [0,0], [0,0] ]

screen = new_screen(10,5)
#print(screen)

def print_screen(s: '2D list') -> None:
    ''' print the 2D list in a matrix-like format
    '''
    for row in range(len(s)):
        for col in range(len(s[0])):
            if s[row][col] == 0:
                pixel = '#'
            else:
                pixel = ' '
            print(pixel, sep='', end='')
        print() # newline for the end of row
    return
'''
print_screen(screen)
print()
screen[2][3] = 1
print_screen(screen)
'''

def set_row(s: '2D list', rownum: int, value: int) -> None:
    ''' Change the screen so that the specified row has the specified
        value across
    '''
    for col in range(len(s[rownum])):
        s[rownum][col] = value
    return

'''
print()
print()
print_screen(screen)
print()
set_row(screen, 7, 1)
print_screen(screen)
print()
'''

def set_column(s: '2D list', column: int, value: int) -> None:
    ''' Change the screen so the specified column has the specified value
        down
    '''
    for row in range(len(s)):
        s[row][column] = value
    return

'''
screen2 = new_screen(20,30)
print_screen(screen2)
print()
set_column(screen2, 17, 1)
set_column(screen2, 27, 1)
set_row(screen2, 15, 1)
print_screen(screen2)
'''

'''
# Other possible functions....
def set_pixel(screen, row, col, value):
    s[row][col] = value

def reverse_pixel(screen, row, col):
   - if pixel is 0, make it 1, If it's 1, make it 0.

def draw_rectangle(screen, UL_row, UL_col, width, height):
   - Some form of loop replacing pixels along the way.
'''

'''
Lists:
L = []
L = ['a', 'b', 'c']

'''
# Dictionaries
D = {}
D = {'John': 18, 'Jane': 19, 'Joe': 20 }


print("Jane's age is:", D['Jane'])

'''
Restrictions on using Dictionaries
- Keys must be an immutable type (int, str, nametuples, ... not lists)
- Values can be anything
- For our purposes, Keys are UNIQUE. Don't define something like
D = {'Joe': 17, 'Joe':17}
    - Python is OK with duplicate keys and it will return the last key/value
    found in the dictionary
    - Four our purposes, we should never use duplicate keys.
- Key-value pairs are NOT ORDERED
'''

'''
for x in D:
    print(x) # Print the key
    print(D[x]) # Print the value
'''

# Assign a new value
D['Jane'] = 100
print(D)
D['Jane'] = D['Joe']
print(D)

# Adding to a dictionary
D['Richert'] = 21
print(D)

# Get number of elements in a dictionary
print(len(D))
