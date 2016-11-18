#ICS 31, 4/7

'''
Extendability
    -we can represent more complex data using featrue such as namedtuple
    -we can increase functionality by providing our own custom functions
'''

#Defining functions

def double(n:int) ->int:
    '''
    Return two times to the parameter
    '''
    return 2*n
'''
-def double() is defining the name of the function
-(n:int)denotes the parameter(s) that this function accpets.
- -> denotes what the function (should) return
-these three pieces are called the function signature.
-the actual code(return 2*n)is called the function body
-If the function return a value, thena return statement is needed,

'''
print(double(8))
def double2(n):
    return 2*n
#assert statements

#print(double(2))

print(double2(8))
assert double(2) == 4
assert double(0) == 0
assert double(-3) == -6
assert double(1234) == 2468

print(double("2"))
print(double(2.5))


def print_5_hyphens() -> None:
    print("-----")
    return #optional, but good to have

def print_n_copies(n:int,s:str):
    print(s*n)
    return

def return_n_copies(n:int,s:str):
    return n*s

print("Study hard", print_n_copies(100,"!")) #works,but probably not as intended
print("study hard", return_n_copies(100,"!"))

#Selection or contional statement
'''
- The ablity to tell the computer to perform one thing in a situation vs. another
thing in another situation
- Enables programmers to customize their performs.

SYNTAX
if Boolean expression:
    statement(s)
-Evaluate the boolean expression (true/false)
-if false, skip the statements and continue execution

'''

milesDriven = 250
print("Should you pull over and fill up your gas tank")
if milesDriven > 200:
    print("Yes")
else:
    print("no,keep going")
'''
Else statement
if Boolean expression:
    statement(s) #1
else:
    statement(s) #@




