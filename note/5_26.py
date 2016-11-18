# ICS 31, 5-26-16

'''
TUPLES
    - We've been using namedtuples throughout the quarter.
        - Good for representing complex data (heterogenous) as objects with fields.
    - Tuples are like namedtuples except tuples do not have named fields.
    - Like namedtuples, tuples are IMMUTABLE
'''

t = ('Richert', 'Wang')
point_3d = (10, 11, 12)

print(t)
print(point_3d)

print(t[0], t[1])
print(point_3d[0], point_3d[1], point_3d[2])

# Add to a tuple
#point_4d = (10, 11, 12) + (13) # ERROR, thinks (13) is an int, not a tuple.
point_4d = (10, 11, 12) + (13,) # ',' is necessary
print(point_4d)
point_6d = point_4d + (14,15)
print(point_6d)

# Get the size of the tuple
print(len(point_4d))

# Remove from a tuple
# Since it's immutable, a new tuple will have to be formed.

# remove odd numbers
t1 = (1,2,3,4,5,6,7,8,9)
t2 = ()
#print(t2)

for i in t1:
    if i % 2 == 0:
        t2 += (i,)

print(t1)
print(t2)

'''
Q: Why use tuples vs. lists? Conceptually, they're pretty much the same.
A: Sometimes it's stylistic more than anything, but sometimes you have to
use a tuple for certain scenarios.

Scenario:
- Dictionary keys must have immutable types.
- Lists cannot be used as a key in a dictionary
- Tuples are immutable, so it can!
- For example, a 3D point may map to a certain value.
    - Use a tuple to represent the 3 coordinate points and use a dictionary
    to map the point to a value
'''

D = {}
L = [1,2,3]
T = (1,2,3)

#D[L] = "some value"
D[T] = "some value"
print(D)
####

# 2D Table Example
# Class Scheduling
# Rooms 0 to 9 (10 rooms total)
# Hours of a day, 00 to 23
# courses are strings

def create_table(rows:int, cols: int) -> '2D Table':
    ''' Create a 2D table (list of lists) with specified number of rows (hours) and
    columns (rooms). Room numbers are from 0 - 9.
    '''
    Table = []
    for row in range(rows):
        Table.append(["-----"] * cols)
    return Table

#print(create_table(24, 10))

#def schedule_print(T: '2D Table', rows: int, cols: int) -> None:
def schedule_print(T: '2D Table'): # remove rows and cols (unnecessary)
    ''' Print out the table in a format
    '''
    # Print out room numbers
    s = "    " # 4 spaces
    for room in range(len(T[0])):
        s += "ROOM" + str(room) + " "
    print(s)

#    for row in range(rows):
    for row in range(len(T)): # no need for rows
        print("{:2d}: ".format(row), end="")
#        for col in range(cols):
        for col in range(len(T[0])): # no need for cols
            print("{:6s}".format(T[row][col]), sep="", end="")
        print()
    return

#schedule_print(create_table(24,10), 24, 10)

def set_schedule(T: '2D Table', course: str, hour: int, room: int) -> bool:
    ''' Put the specified course into the schedule at the specified room and hour.
    '''

    ### error checking... ###
    if hour not in range(len(T)):
        print("Error. Invalid hour. Must be between 0 and " + str(len(T) - 1))
        return False
    if room not in range(len(T[0])):
        print("Error. Invalid room. Must be between 0 and " + str(len(T[0]) - 1))
        return False
    
    T[hour][room] = course
    return True

'''
schedule = create_table(24, 10)
set_schedule(schedule, "ICS31", 17, 9)
schedule_print(schedule, 24, 10)
'''

schedule = create_table(24,10)
#schedule_print(schedule)
print("\n Table with one class:\n")

#set_schedule(schedule, 'ICS31', -1, 9)
#set_schedule(schedule, 'ICS31', 24, 9)
#set_schedule(schedule, 'ICS31', 17, -1)
#set_schedule(schedule, 'ICS31', 17, 10)
success = set_schedule(schedule, 'ICS31', 17, 9)
schedule_print(schedule)

if success:
    print("A OK!")
else:
    print(":'(")
