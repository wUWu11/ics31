# Truong Tran 76992464 and Deyu Wu 0952612 . ICS 31 Lab sect 3. JUNKUYL.
#Part c
print('\n')
print('---------- Part c ----------')
print('\n')
from random import randrange


#c.1
print('\n#c.1------------------------------------\n')

def contains(s1:str, s2:str) -> bool:
    return s2 in s1;
assert contains('banana', 'ana') == True
assert contains('racecar', 'ck')== False

#c.2
print('\n#c.2------------------------------------\n')

def sentence_stats(s1:str):
    s1=transform(s1);
    words = s1.split();
    print("Characters: ",len(s1));
    print("words: ",len(words));
    n1 = 0.0;
    for item in words:
         n1 += len(item);
    n1 = n1/len(words);
    print("Average word length: ", n1);

def transform(s1:str)->str:
    a=''
    for item in s1:
        if not((ord(item)>=65 and ord(item)<=90 ) or (ord(item)>=97 and ord(item)<=122)):
            a+=' ';
        else:
            a+=item;
    return a;
sentence_stats('I love UCI');
print('\n');
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.');

#c.3
print('\n#c.3------------------------------------\n')



def initials(s1:str)->str:
    s1=transform(s1);
    words=s1.split();
    a='';
    for item in words:
        if(ord(item[0])>=97):
            a+=chr(ord(item[0])-32);
        else:
            a+=item[0];
    return a;

assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

print('\n#d.1------------------------------------\n')

for i in range(50):
    print(randrange(0,11));

print('\n#d.2------------------------------------\n')
for i in range(50):
    print(randrange(1,7));
print('\n#d.3------------------------------------\n')
def roll2dice()->int:
    n1=randrange(1,7);
    n2=randrange(1,7);
    return n1+n2;
def distribution_of_rolls(n:int):
    L=[];
    for i in range (n):
        L.append(roll2dice())
    print("2:        ",L.count(2),' (',L.count(2)/n*100,' %)', L.count(2)*'*','\n');
    print("3:        ",L.count(3),' (',L.count(3)/n*100,' %)', L.count(3)*'*','\n');
    print("4:        ",L.count(4),' (',L.count(4)/n*100,' %)', L.count(4)*'*','\n');
    print("5:        ",L.count(5),' (',L.count(5)/n*100,' %)', L.count(5)*'*','\n');
    print("6:        ",L.count(6),' (',L.count(6)/n*100,' %)', L.count(6)*'*','\n');
    print("7:        ",L.count(7),' (',L.count(7)/n*100,' %)', L.count(7)*'*','\n');
    print("8:        ",L.count(8),' (',L.count(8)/n*100,' %)', L.count(8)*'*','\n');
    print("9:        ",L.count(9),' (',L.count(9)/n*100,' %)', L.count(9)*'*','\n');
    print("10:        ",L.count(10),' (',L.count(10)/n*100,' %)', L.count(10)*'*','\n');
    print("11:        ",L.count(11),' (',L.count(11)/n*100,' %)', L.count(11)*'*','\n');
    print("12:        ",L.count(12),' (',L.count(12)/n*100,' %)', L.count(12)*'*','\n');
    print("----------------------------------------------------------");
    print("            ",n,"rolls                                  ");

distribution_of_rolls(200);
print('\n')
print('---------- Part e ----------')
print('\n')


def Caesar_encrypt(s1:str,n:int)->str:
    s1=s1.lower();
    a='';
    for item in s1:
        if (ord(item) >=65 and ord(item) <=90):
            if(ord(item)+n>90):
                a+=chr(ord(item)+n-90+64);
            else:
                a+=chr(ord(item)+n);
        elif (ord(item) >=97 and ord(item)<=122):
            if (ord(item)+n>122):
                a+=chr(ord(item)+n-122+96);
            else:
                a+=chr(ord(item)+n);
        else:
            a+=item;
    return a;
def Caesar_decrypt(s1:str,n:int)->str:
    s1=s1.lower();
    a='';
    for item in s1:
        if (ord(item) >=65 and ord(item) <=90):
                if(ord(item)-n<65):
                    a+=chr(91-(65-(ord(item)-n)));
                else:
                    a+=chr(ord(item)-n);
        elif (ord(item) >=97 and ord(item)<=122):
                if (ord(item)-n<97):
                    a+=chr(123-(97-(ord(item)-n)));
                else:
                    a+=chr(ord(item)-n);
        else:
                a+=item;
    return a;

print( Caesar_encrypt('Zbcde',2))
print( Caesar_decrypt(Caesar_encrypt('Zbcde',2),2))
print('\n')

print('\n')
print('---------- Part f ----------')
print('\n')

print ('--- f (1) ---')

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
print ('--- f (2) ---')
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
print ('--- f (3) ---')
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






