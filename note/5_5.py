# ICS 31, 5-5-16

price = 18.00
print("The price is ${:.2f}. That's cheap!".format(price))

# Format
'''
{ : }. Left side of colon says which argument is used within the string
'''

print("{3:} {1:} {1:} {0:}".format('a','b','c','d'))

print("-->{}<--".format(price))
print("-->{:20}<--".format(price))
print("-->{:20}<--".format("18.0"))

# We can use '>' or '<' to justify left or right
print("-->{:<20}<--".format("18.0"))
print("-->{:>20}<--".format("18.0"))

# we want to center our text within some spaces
print("Richert".center(15, ' '))
# or
print("-->{:^20}<--".format("Richert"))


# can identify specific types that should be expected with 's' - string,
# 'd' - int, 'f' - float
name = "John Jones"
age = 24
print("Name is {:12s}; age is {:2d}; price is ${:0.2f}".format(name,age,price))
print("Name is {:12}; age is {:2}; price is ${:0.2}".format(name,age,price))

'''
BIG PICTURE: Programming Languages helps us model the real world
    - Things / nouns / objects - (ints, floats, lists, nametuples, ...)
    - Actions / Verbs - (functions, methods, operators, statements, control
        structure, etc).

DATA STRUCTURES:
    - Single-valued structure - (ints, floats, bool, str,...)
    - Multiple-valued data structures
        - Lists: collection of objects of the same type (for ICS 31)
        - Namedtuples: package of (possibly) different-type data fields
            that describe a more complex object
    - Files - Persists data
    - ... and many others
* The interaction of these components allows us to represent the real world

    - Control statements / structures
        - Single operations: +, -, *, /, %
        - Functions methods: len(L), L.count('Richert'), print()
        - Statements: =, assert, return

We can combine these components in different ways:
    - Simple sequence:
    stmt1
    stmt2
    stmt3
    ...

# Conditions allow us to execute some code and ignore others based on a
# BOOLEAN_VALUE

Stmt1
if BOOLEAN_EXPRESSION:
    stmt2
else: 
    stmt3
stmt4

- It's important to know the syntax and semantics of each statement and control
structure
    - Control structure to BEHAVE A CERTAIN WAY depending on program state
       - if , else
    - Control structure to MODULATIZE behavior
        - functions
    - Control structure to REPEAT behavior
        - for , while

- for-each loop:
for CONTROL_VARIABLE in COLLECTION:
    stmts...

- indexing for loop:
for i in range(10):
    stmts...

for i in range(10):
    L[i] = L[i] + 1
    print(i, "-", L[i])

Q: Ways to find something in a list?

found = False
for r in L:
    if r == 'something' and not found:
        found = True
return found

for r in L:
    if r == 'something':
        found = True
        break
return found

Another example: let's use Restaurant example and we want to find the first
thai restaurant that exists in a list of restaurants.

thai = ""
for r in L:
    if r.cuisine == "Thai":
        thai = r
        return thai
return thai

for r in L:
    if r.cuisine == "Thai":
        return r
return

# Another example

#1
for i in s:
    stmt1
    stmt2
    if BOOLEAN_EXPRESSION:
        continue
    stmt3
    stmt4
stmt5

#2
for i in s:
    stmt1
    stmt2
    if not BOOLEAN_EXPRESSION
        stmt3
        stmt4
stmt5

# Q: is this the same?

'''
x = 10
x = "fjsklfj"
print(x)
