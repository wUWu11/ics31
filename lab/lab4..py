#Shenzhi Li 569710944 and .  ICS 31 Lab sec3.
'''
#
#
#(c)
#
#

#(c.1)
def test_number(x:int, s:str):
    if s == 'even':
        if x % 2 == 0:
            return True
        else:
            return False
    if s == 'odd':
        if x % 2 == 0:
            return False
        else:
            return True
    if s == 'positive':
        if x > 0 :
            return True
        else:
            return False
    if s == 'negative':
        if x < 0:
            return True
        else:
            return False

assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

#(c.2)
def display():
    word = input('Enter a word:')
    for i in range(len(word)):
        print(word[i:i+1])
    return  ##why here is a None?

print(display())

#(c.3)
def square_list(l:list):
    for i in range(len(l)):
        square_value = l[i] * l[i]
        print(square_value)
    return
print()
square_list([2,3,4,10])

#(c.4)
def match_first_letter(s:str,l:list):
    for i in range(0, len(l)):
        if s == l[i][0:0+1]:
            print(l[i])
        else:
            'nothing'
    return

print()
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])

#(c.5)
def match_area_code(larea:list,lphone:list):
    for i in range(0,len(lphone)):
        for k in range(0, len(larea)):
            if lphone[i][1:3+1] == larea[k]:
                   print(lphone[i])
    return
print()
match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])

#(c.6)
def matching_area_codes(larea:list, lphone:list) -> list:
    l = []
    for i in range(0, len(lphone)):
        for k in range(0, len(larea)):
            if lphone[i][1:3+1] == larea[k]:
                l.append(lphone[i])
    return l
print()
print(matching_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234']))

#
#
#(d)
#
#
'''
#(d.1)
def is_vowel(s:str):
    '''take a one-character-long str with the vowel letter,
       return if it is ture or not'''
    return s in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
print(is_vowel('b'))
print(is_vowel('A'))

            
# test part
assert is_vowel('a')
assert is_vowel('O')
assert not is_vowel('T')
assert not is_vowel('?')

#(d.2)
def print_nonvowels(s:str):
    '''return nonvowels in string'''
    for i in s:
        if is_vowel(i) == False:
            print(i)
    return
# test part

print_nonvowels('Happy')

#(d.3)
def nonvowels(a:str) -> str:
    #return a string containing all nonvowels in the parameter string
    result = ""
    for i in a :
        if is_vowel(i) == False:
            result = result + i
    return result
print(nonvowels("booleanexpression"))

#test part
assert nonvowels('?s% 23a') == '?s% 23'
assert nonvowels("booleanexpression") == "blnxprssn"
assert nonvowels('nonvowels') == 'nnvwls'

#(d.4)
def consonants(s:str) -> str:
    new_s = ''
    new_s = nonvowels(s)
    result = ""
    for i in range(len(new_s)):
        if new_s[i:i+1].isalpha():
            result = result + new_s[i:i+1]
    return result
print(consonants("boolea1n2e3x4pression!!"))
#test part
assert consonants('nonvowels') == 'nnvwls'
assert not consonants('?s% 23a') == '?s% 23'

#(d.5)
def select_letters (vc:str,s:str) ->str:
    '''if first parameter is 'v', retrun a string with all the vowels in the second parameter'''
    '''if first is 'c', retrun a string with all the consonants in the second parameter'''
    '''if first is anything, return empty'''
    new_s = ''
    if vc == 'v':
        for i in range(0, len(s)):
            if is_vowel(s[i:i+1]):
                new_s = new_s + s[i:i+1]
    elif vc == 'c':
        for i in range(0, len(s)):
            if not is_vowel(s[i:i+1]):
                new_s = new_s + s[i:i+1]
    else:
        new_s = ''
    return new_s

# test part
assert select_letters('c', 'facetiously') == 'fctsly'
assert select_letters('v', 'facetiously') == 'aeiou'
assert select_letters('k', 'facetiously') == ''

#(d.6)
def hide_vowels(s:str) -> str:
    "replace all the vowel letter with '-' and return the new string"
    new_s = ''
    for i in range(0, len(s)):
        if is_vowel(s[i:i+1]):
            new_s = new_s + '-'
        else:
            new_s = new_s + s[i:i+1]
    return new_s

# test part
assert hide_vowels('facetiously') == 'f-c-t---sly'

#
#
#(e)
#
#
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')

def Restaurant_change_price(rest:Restaurant, p:float) -> Restaurant:
    "return the Restaurant Object with the price changed by the input value"
    rest = rest._replace(price = rest.price + p)
    return rest

# test part
rest1 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 52.50)
assert Restaurant_change_price(rest1, 10) == Restaurant(name='Nola', cuisine='New Orleans', phone='336-4433', dish='Jambalaya', price=62.5)

#
#
#(f)
#
#
from collections import namedtuple

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number,
#	best dish, price of that dish

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]

#(f.1)
def restaurant_name(res:Restaurant) ->str:
    return res.name

def alphabetical(l:list) -> list:
    "Return the list sorted by name, and do not change the original list's order"
    new_l = []
    for i in range(len(l)):
        new_l.append(sorted(l, key=restaurant_name)[i])
    return new_l

# test part
assert alphabetical(RL) == [R26, R8, R16, R14, R12, R19,
                            R10, R23, R2, R20, R7, R15,
                            R21, R24, R25, R22, R3, R13,
                            R17, R18, R1, R5, R6, R4, R11, R9]

#(f.2)
def alphabetical_names(l:list) -> list:
    "Return a new list with all the name in alphabetical order from the input list"
    new_l = []
    for i in range(len(l)):
        new_l.append(alphabetical(l)[i].name)
    return new_l

# test part
assert alphabetical_names(RL) == ["Addis Ababa", "Burger King", "Chez Panisse", "Gaylord",
                                  "Gina's", "Golden Pagoda", "In-N-Out Burger", "Jitlada",
                                  "La Tour D'Argent", "Langer's", "McDonald's", "Mr. Chow",
                                  "Nobu", "Nola", "Noma", "Nonna", "Pascal", "Peacock, Room",
                                  "Spago", "Sriped Bass", "Taillevent", "Thai Dishes", "Thai Spoon",
                                  "Thai Touch", "The Shack", "Wahoo's"]
#(f.3)
def all_Thai(l:list) -> list:
    "Return a list with all the Thai food restaurant from the input list"
    new_l = []
    for i in range(len(l)):
        if l[i].cuisine == "Thai":
            new_l.append(l[i])
    return new_l

# test part
assert all_Thai(RL) == [R4, R5, R6, R23]

#(f.4)
def select_cuisine(l:list, c: str) -> list:
    "return a list with all the Restaurant Object in the input list with the same cuisine as the input string value"
    new_l = []
    for i in range(len(l)):
        if c == l[i].cuisine:
            new_l.append(l[i])
    return new_l

# test part
assert select_cuisine(RL, "Burgers") == [R7, R8, R10, R11]

#(f.5)
def select_cheaper(l:list, p:float) -> list:
    "Return all the Restaurant in the list whose price is less than the input value p"
    new_l = []
    for i in range(len(l)):
        if l[i].price < p:
            new_l.append(l[i])
    return new_l

# test part
assert select_cheaper(RL, 10.00) == [R5, R6, R7, R8, R9, R10, R11, R19, R21, R24]

#(f.6) ###too complex
def average_price(l:list) -> float:
    "Rerutn the average price of all the restaurant in the list"
    total = 0.00
    for i in range(0, len(l)):
        total = total + l[i].price
    average = total / 2
    return average

def sum_price(l:list)-> float:
    #return the sum price of all the restaurant
    result = 0
    for i in l:
        result = result + l[i].pirce
# test part
assert average_price(RL) == 204.04999999999998

#(f.7)
print(average_price(select_cuisine(RL, "Indian")))

#(f.8)
print(average_price(select_cuisine(RL, "Chinese")+select_cuisine(RL, "Thai")))

#(f.9)
print(alphabetical_names(select_cheaper(RL, 15.00)))

#
#
#(g)
#
#
import tkinter

#  creat_rectangle_from_center:  x: int, y: int, height: int, width: int  
def create_rectangle_from_center(x:int, y:int, height: int, width: int):
    "Return a rectangle by input center point's x and y value , height and width"
    my_canvas.create_rectangle(x-(width/2), y-(height/2), x+(width/2), y+(height/2))
    return

my_window = tkinter.Tk()

my_canvas = tkinter.Canvas(my_window, width=400, height=400)
my_canvas.pack() 

create_rectangle_from_center(200, 200, 150, 300)

tkinter.mainloop()
