#Deyu Wu 0952612, Erik Orellana 13656378
#---------part C----------
print('----------part C----------')
print()
print()
from random import randrange
from random import choice
from collections import namedtuple
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""
#c1
def generate_answers()->str:
    '''generates and returns a string of letters representing the correct answers
    to the test.'''
    answers = ''
    for i in range(NUMBER_OF_QUESTIONS):
        
        answers += choice(alphabet[:NUMBER_OF_CHOICES])
    return answers
ANSWERS = generate_answers()
print(ANSWERS)

print()

#c2 and c3 
Student = namedtuple('Student', 'name answers scores total')


infile1 = open('femalenames.txt','r')
infile2 = open('malenames.txt','r')
infile3 = open('surnames.txt','r')
########getting name data

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
######### end
def count_score(a:list):
    return a.count(1)

def check_score(a:str):
    result = []
    for i in range(len(a)):
        if a[i] == ANSWERS[i]:
            result.append(1)
        else:
            result.append(0)
    return result
        

def random_students():
    result = []
    for i in range(NUMBER_OF_STUDENTS):
        name = random_name()
        answers = generate_answers()
        scores = check_score(answers)
        total = count_score(scores)
        s = Student(name,answers,scores,total)
        result.append(s)
    return result


def student_total(S:Student):
    return S.total

print()
SL = random_students()
SL.sort(key=student_total,reverse= True)
print(SL[:10])
print()

def scores_mean(L:'list of Students'):
    '''takes a list of students and return the mean of students' score
    '''
    result = 0
    for s in L:
        result += s.total
    mean = result/len(L)
    return mean
print(scores_mean(SL))
print()

#c4
def generate_weighted_student_answer(a:str):
    '''takes a string (one character, the correct answer) and returns a string
    '''
    alph = alphabet[:NUMBER_OF_CHOICES] + a*randrange(8)
    result = choice(alph)
    return result


def random_students2():
    result = []
    answers = ''
    for i in range(NUMBER_OF_STUDENTS):
        name = random_name
        for a in ANSWERS:
            answers += generate_weighted_student_answer(a)
        scores = check_score(answers)
        total = count_score(scores)
        s = Student(name,answers,scores,total)
        result.append(s)
        answers = ''
    return result
SL2 = random_students2()
SL2.sort(key=student_total,reverse= True)
print(SL[:10])
print()
print(scores_mean(SL2))
print()

#C.5

def question_weights (SL:'list of students records') -> list:
    '''Takes a list of students records and returns a list of numbers,
    that represent the number of times a student answered a question
    incorrectly'''
    result = []
    for question in range(NUMBER_OF_QUESTIONS):
        x = 0
        for student in SL:
            if student.scores[question] == 0:
                x += 1
        result.append(x)
    return result

print(question_weights(SL2))
"""
#-------------part D---------------
print('---------part D--------')
print()

#d1
def calculate_GPA(l:'list of strings')->float:
    '''takes as input a list of strings representing letter
    grades and returns the grade point average'''
    total = 0
    for g in l:
        if g == 'A':
            total += 4
        if g == 'B':
            total += 3
        if g == 'C':
            total += 2
        if g == 'D':
            total += 1
    return total/len(l)

def calculate_GPA2(l:'list of strings')->float:
    '''takes as input a list of strings representing letter
    grades and returns the grade point average'''
    total = 0
    D = {'A':4,'B':3,'C':2,'D':1,'F':0}
    for g in l:
        total += D[g]
    return total/len(l)
assert calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
assert calculate_GPA2(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716

#d2
def flatten_2D_list(s:'2D list')->list:
    '''(d.2) Implement the function flatten_2D_list that takes as
    input a two-dimensional table (a list containing lists) and
    returns the input as a single list containing, in order, all
    the elements on the original nested list.'''
    result = []
    for l in s:
        for n in l:
            result.append(n)
    return result
assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]
    
#d3
print('d3')
print('')
def skip_every_third_item(l:'list of strings'):
    '''takes as input a list and prints out each item on the list, except that it skips every third item
    '''
    for i in range(len(l)):
        if i%3 != 2:
            print(l[i])
L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']
skip_every_third_item(L)


def skip_every_nth_item(l:'list of strings',n:int):
    ''' takes as input a list and an int (call it n) and prints out each item on the list,
    except that it skips every nth item   '''
    for i in range(len(l)):
        if i % n != n-1:
            print(l[i])
#test
skip_every_nth_item(L,3)

#d4
def tally_days_worked(l:list)->dict:
    ''' takes as input the list described above and returns a dictionary where every key is a name of
       an employee and the value is the number of days that employee worked in the
       given week, according to the list'''
    Dic = {}
    for i in l:
        Dic[i] = 0 
    for i in l:
        Dic[i] += 1
    return Dic

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']


workers = tally_days_worked(work_week)
print(workers)

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

def pay_employees(d1:dict,d2:dict):
    ''' takes as input the two dictionaries described above and prints out how much each employee will be paid,
    '''
    for i in d1:
        for n in d2:
            if i==n:
                print("{} will be paid ${:3.2f} for {:2} hours of work at {:3.2f} per hour ".format(i,8*d1[i]*d2[n],8*d1[i],d2[n]))

pay_employees(workers,hourly_wages)

#d5
def reverse_dict(d:dict)->dict:
    '''takes as a parameter a dictionary and returns a new dictionary with the keys and values of the original dictionary reversed'''
    new_dict = {}
    for i in d:
        new_dict[d[i]] = i
    return new_dict

#test
print(reverse_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}))
