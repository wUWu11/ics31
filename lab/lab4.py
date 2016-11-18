#part C
'''
#________c1________


def test_number(a:int,b:str):#returns True if the number has the property indicated by the string
    while True:
        
        if b == "positive":
            return a>0
        if b == "negative":
            return a < 0
        if b == "odd":
            return a % 2 == 1
        if b == "even":
           return a % 2 == 0

assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')

#________c2________

def display():
#print out every character(user input) one per line
    print("Enter a word")
    a = input()
    for i in a:
        print(i)

display()
    
    

#________c3________
def square_list(a:list):
    #takes a list of integers and prints out each integer squared.
    for i in a:
        print(i**2)

square_list([2,3,19,50])

#________c4________

def match_first_letter(a:str,b:list):
    #print out all the strings in the list start with a(a specified character)
    for i in b:
        if i[0] == a:
            print(i)
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])

#________c5________
def match_area_code(a:list,b:list):
    #print the phone numbers whose area code is on the list of area codes
    for i in a:
        for n in b:
            if i == n[1:4]:
                print(n)
match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])

#________c6________
def matching_area_code(a:list,b:list):
    #print the phone numbers in a list
    l = []
    for i in a:
        for n in b:
            if i == n[1:4]:
                l.append(n)
    return print(l)            
                
matching_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])


#part D
'''

#________d1________
def is_vowel(a:str):
    #return ture if this character is a vowel and false otherwise
    return a in ['a','e','i','o','u','A','E','I','O','U']
print(is_vowel('b'))
print(is_vowel('a'))

is_vowel('b')

assert is_vowel('a') 
assert is_vowel('U')
assert not is_vowel('X')
assert not is_vowel('?')

#________d2________
def print_nonvowels(a:str):
    #return nonvowels in this string
    for i in a:
        if is_vowel(i)== False:
            print(i)

print_nonvowels("booleanexpression")

#________d3________
def nonvowels(a):
    #return a string containing all nonvowels in the parameter string
    result = ""
    for i in a :
        if is_vowel(i) == False:
            result = result + i
    return result
print(nonvowels("booleanexpression"))

assert nonvowels("booleanexpression") == "blnxprssn"
assert nonvowels('nonvowels') == 'nnvwls'






#________d4________
con= ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
def is_consonants(a:str):
    # return True if a is a consonant, else Flase
    return a in con

print(is_consonants('b'))
print(is_consonants('a'))

def consonants(a:str)->str:
    #return a str containing all the consonants in previous string
    result = ''
    for i in a:
        if is_consonants(i) == True:
            result = result + i
    return result
print(consonants("boolea1n2e3x4pression!!"))

    

#________d5________
def select_letters(a:str,b:str):
    '''if first parameter is 'v', retrun a string with all the vowels in the second parameter'''
    '''if first is 'c', retrun a string with all the consonants in the second parameter'''
    '''if first is anything else, return empty'''
    result = ''
    if a =='v':
        for i in b:
            if is_vowel(i)== True:
                result = result + i
    elif a == 'c':
        result = consonants(b)
    else:
        result = ''
    return result


assert select_letters('c', 'facetiously') == 'fctsly'
assert select_letters('v', 'facetiously') == 'aeiou'
assert select_letters('k', 'facetiously') == ''


#________d6________
def hide_vowels(a:str)->str:
    #which every vowel in the parameter is replaced with a hyphen ("-") and all other characters remain unchanged
    result = ''
    for i in a:
        if is_vowel(i) ==True:
            result = result + '-'
        else:
            result = result + i
    return result

assert hide_vowels('facetiously') == 'f-c-t---sly'
           



#________e________
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')

def Restaurant_change_price(rest:Restaurant, p:float) -> Restaurant:
    "return the Restaurant Object with the price changed by the input value"
    rest = rest._replace(price = rest.price + p)
    return rest


rest1 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 52.50)
assert Restaurant_change_price(rest1, 10) == Restaurant(name='Nola', cuisine='New Orleans', phone='336-4433', dish='Jambalaya', price=62.5)

#________f________

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


