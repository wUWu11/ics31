#Deyu Wu 0952612,
#Lab6.py
"""
#-------C---------

#-------C1---------
print('#-------C1---------')
def contains(a:str,b:str)->bool:
    '''takes two strings a,b if b is in a return true, else return false
    '''
    return b in a
    

assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
assert not contains('user','kdlas;')
assert contains('ave_ ','_ ')

#-------C2---------
print('#-------C2---------')
def translate_to_blanks(a:str)->str:
    '''return blanks
    '''
    table = str.maketrans('@#$%^&*().,!?:;"\'', '                 ')
    return a.translate(table)
    
    
    
def sentence_stats(a:str)->None:
    
    b = translate_to_blanks(a)
    print('Characters:',len(a))
    print('Words:',len(b.split()))
    result = 0
    for i in b.split():
        result += len(i)
    print('Average word length:',result/len(b.split()))
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
    

#-------C3---------
print('#-------C3---------')
def initials(a:str)->str:
    ''' takes as input a string representing a full name 
        and returns the initials of the name in all capital letters
    '''
    
    result = ''
    new = a.split()
    for i in new:
        result += i[0]
    return result.upper()
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

#-------D---------
#-------D1---------
print('#-------D1---------')
from random import randrange
for i in range(50):
    print(randrange(11))
for i in range(50):
    print(randrange(1,7))
#-------D2---------
print('#-------D2---------')
def roll2dice()->None:
    '''returns a number that reflects the random roll of two dice
    '''
    r1 = randrange(1,7)
    r2 = randrange(1,7)
    result = r1+r2
    return result

#-------D3---------
print('#-------D3---------')
def distribution_of_rolls(a:int):
    new_list = []
    for i in range(a):
        new_list.append(roll2dice())
    for i in range(2,13):
        print(i,':    ',new_list.count(i),'( ',100*new_list.count(i)/a,'%)  ','*'*new_list.count(i),sep = '')

distribution_of_rolls(200)
"""


#-------E---------
#-------F---------
l = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

#-------F1---------
def print_line_numbers(a:'list of strings'):
    '''print out each string preceded by a line number
    '''
    for i in range(len(a)):
        print("{:<5d}:{} ".format(i+1,l[i]))
        
print_line_numbers(l)

#-------F2---------

def stats(a:'list of strings'):
    '''takes a list of strings and prints statistics '''
    num_of_lines = len(a)
    num_of_empty_lines = 0
    num_of_chara = 0
    for i in a:
        i = i.strip()
        print(i)
        num_of_chara += len(i)
        if len(i) == 0:
            num_of_empty_lines += 1
    print('{:<6}'.format(num_of_lines),  'lines in the list')
    print('{:<6}'.format(num_of_empty_lines),   'empty lines')
    print('{:<6}'.format(num_of_chara/num_of_lines) ,"average characters per line")
    print('{:<6}'.format(num_of_chara/(num_of_lines-num_of_empty_lines)),'average characters per non-empty')     

stats(l)
#-------F3---------
def list_of_words(a:'list of strings')->'list of strings':
    ''' takes a list of strings as above and returns a list of individual words
        with all white space and punctuation removed (except for apostrophes/single quotes
    '''
    result = []
    table = str.maketrans('",./<>?[]{}:;~!@\t\n','                  ')
    for i in a:
        i = i.translate(table)
        i = i.replace(' ','')
        i = i.lstrip()
        for n in i:
            result.append(n)
    return result

print(list_of_words(l))


