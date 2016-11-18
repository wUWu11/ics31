#Deyu Wu, 0952612 and Yue Zeng 23288035   ICS31 lab sec 3. Lab asst 7.
from random import randrange

#--------------part C----------------
infile1 = open('femalenames.txt','r')
infile2 = open('malenames.txt','r')
infile3 = open('surnames.txt','r')

print('-----part C------')
def extra_names_data(infile):
    '''takes a opened file which includes not only name data
       return name data in a list
    '''
    data = infile.read().split()
    name_data = []
    for i in range(len(data)):
        if i%4 ==0:
            name_data.append(data[i])
    return name_data

female_name = extra_names_data(infile1)
male_name = extra_names_data(infile2)
sur_name = extra_names_data(infile3)
def random_name():
    '''return a random name picked from name data (female_name,male_name,and surname)
    '''
    if randrange(2) == 0:
        name = sur_name[randrange(len(sur_name))].title() +', '+\
               male_name[randrange(len(male_name))].title()
        
    else:
        name = sur_name[randrange(len(sur_name))].title() +', '+\
               female_name[randrange(len(female_name))].title()

    return name

print(random_name())
       
def random_names(a:int)->'list of strings':
    '''takes a number and return a list of that many strings
    '''
    result = []
    for i in range(a):
        result.append(random_name())
    return result
print(random_names(10))

#--------------part D----------------       
print('-----part D------')


infile4 = open('wordlist.txt','r')
words = infile4.readlines()

words_nospace = []
for i in words:
    
    words_nospace.append(i.strip())
print(words_nospace[0])


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_trans_table(k:int):
    '''takes a key and return a new table for translating
    '''
    result = ''
    for i in range(len(ALPHABET)):
        result += ALPHABET[(i+k)%26]
    return result

def Caesar_encrypt(message: str, k: int) -> str:
    '''Takes in a message and a key, adds each letter by the key
       and returns the encrypted message
    '''
    table = str.maketrans(ALPHABET+ALPHABET.upper(),get_trans_table(k)+get_trans_table(k).upper())
    result = message.translate(table)
    return result

def Caesar_decrypt(message: str,k: int) -> str:
    '''Takes in a message and a key, subtracts each letter by the key
       and returns the original message
    '''
    table = str.maketrans(ALPHABET+ALPHABET.upper(),get_trans_table(-k)+get_trans_table(-k))
    result = message.translate(table)
    return result
def remove_punctuation(message: str) -> str:
    '''takes a message and return it without punctuation
    '''
    result = ''
    for i in message:
        if i in ALPHABET or i in ALPHABET.upper() or i == "'" or i == ' ':
            result += i
    return result



def Caser_break(m:str) -> str:
    
    result = ''
    for i in range(26):
        prob_sentence = Caesar_decrypt(m,i)
        prob_words = remove_punctuation(prob_sentence).split()
        for l in prob_words:
            
            if l in words_nospace:
                result = result + l + ' '
    return result

print('#####test part#####')
print(Caesar_encrypt('hello FILE. ! format',10))
print(Caser_break('rovvy PSVO. ! pybwkd'))




#--------------part E----------------       
print('-----part E------')

def stats(a:'list of  strings'):
    '''takes a list of strings and prints statistics '''
    num_of_lines = len(a)
    num_of_empty_lines = 0
    num_of_chara = 0
    for i in a:
        i = i.strip()
        num_of_chara += len(i)
        if len(i) == 0:
            num_of_empty_lines += 1
    print('{:<6}'.format(num_of_lines),  'lines in the list')
    print('{:<6}'.format(num_of_empty_lines),   'empty lines')
    print('{:<6}'.format(num_of_chara/num_of_lines) ,"average characters per line")
    print('{:<6}'.format(num_of_chara/(num_of_lines-num_of_empty_lines)),'average characters per non-empty')


    
def copy_file(p:str)->None:
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r',errors='ignore')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w')
    if p == 'line numbers':
        number = 0
        for line in infile:
            number += 1
            outfile.write('{:>5d}:{:s}'.format(number,line))
    if p == 'Gutenberg trim':#omit content before *** START and after *** END
        data = infile.read()
        num_start = data.find('*** START')
        num_end = data.find('*** END')
        new_data = data[num_start:num_end+7]
        for line in new_data:
            outfile.write(line)
    if p == 'statistics':
        stats(infile.read().split('\n'))
        for line in infile:
            outfile.write(line)
    else:
        for line in infile:
            outfile.write(line)
    infile.close()
    outfile.close()



infile1.close()
infile2.close()
infile3.close()
infile4.close()
