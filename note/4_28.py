# ICS 31, 4-28-16

# Text Processing

# STRING - made up of zero or more CHARACTERS
# CHARACTER - keystrokes - anything you can type on the keyboard

# EMPTY STRING - Contains zero characters
x = ""
x = ''

# Specifically, STRINGS are a SEQUENCE of CHARACTERS
# ... one character after another

# Things you can do with strings
# Getting the length: len(x)
# looping through each character: for c in x
# x[2] - Gets a character in a string
# x[1:3] - Slice a string

# WHITE SPACE CHARACTERS - any character that doesn't display on the screen.
# Example - tab ('\t'), newline ('\n'), space (' ')

# Strings can be formed by surrounding characters in
#   - 'single quotes'
#   - "double quotes"
#   - """ triple quotes """ (used for comments or multi-line strings)

# STRING FUNCTIONS

s = "ICS 31: Intro to Programming"
print(s)

print("Where does the first 'mm' occur in s")
print(s.find("mm"))
print(s.find("31:"))
print(s.find("jfklsajfklsadjl"))

text = """This
string
has
multiple
lines"""

print(text)

# .find method
first_newline = text.find("\n")
print("First newline position: ", first_newline)
print("First line of text:", text[:first_newline]) #without \n
print("First line of text:", text[:first_newline + 1]) #with \n
print("String after first newline:", text[first_newline + 1:])
print("Location of a non-existent string:", text.find("fkdsajfajs"))

# .startswith method
print("Check if s starts with 'C':", s.startswith("C"))
print("Check if s starts with 'ICS':", s.startswith("ICS"))

# .endswith method
print("Check if s ends with 'P':", s.endswith("P"))
print("Check if s ends with 'g':", s.endswith("g"))

# .count method
print("Times 'm' is in s:", s.count("m"))
print("Times 'i' is in Mississippi:", "Mississippi".count("i"))

MS = "Mississippi"

# .replace method
print("Change all 'i' to '!' in 'Mississippi':", MS.replace("i", "!"))
print("Change all ':' to '#' in s:", s.replace(":", "#"))
print("Remove all 'i' in 'Mississippi':", MS.replace("i", " "))

print(MS) # MS does not change
MS = MS.replace("i", "") # Change the original string
print(MS)
MS = "Mississippi"

# upper / lower
print(s.upper())
print(s.lower())
print(s)

# title
print(s.title())
#print(text.title())

x = """      To be

or

     not   to
be
"""

#print(x)

# .split method
wordlist = x.split() # creates list of strings separated by whitespace

print(wordlist)
print("Adding spaces to wordlist:", " ".join(wordlist))
print("Adding ',' to wordlist:", ",".join(wordlist))
print("Adding '\n' to wordlist:", "\n".join(wordlist))

# Removing blanks / tabs / newlines

print("----" + x.strip() + "----")
print()
print("----" + x.lstrip() + "----")
print()
print("----" + x.rstrip() + "----")
print()

# Translation Tables
# When we want to replace a character (or group of characters) with something
# else

def our_lower(s: str) -> str:
    ''' Returns an all-lower case s
    '''
    # 1. Make a TRANSLATION TABLE
    table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                          'abcdefghijklmnopqrstuvwxyz')

    #2 . use the table to translate characters in the string
    return s.translate(table)

assert our_lower(MS) == "mississippi"

table2 = str.maketrans('.,!?:;"\'', '        ')

x = "I'm gonna make 'em an offer he can't refuse"

print(x.translate(table2))
