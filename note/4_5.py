#ICS 31 4/5

from collections import namedtuple

Student = namedtuple("Student","name id major GPA")

s1 = Student("John Doc", 1212423, "ics", 3.5)
print("Name of s1,",s1.name)
print("ID of s1,",s1.id)
print("Major,",s1.major)
print("GPA of s1,",s1.GPA)

#s1.GPA = 3.6 crash!

s1 = Student(s1.name,s1.id,s1.major,3.6)
print("Name of s1,",s1.name)
print("ID of s1,",s1.id)
print("Major,",s1.major)
print("GPA of s1,",s1.GPA)

'''
Programming language help model the real-world slove complete problems

-Single-value data
    -int float, boolean
boolean
    -Boolean values are a special type that evaluates to either True or False
- Multi-valued data
    -lists["a","b",'c']
    -Namedtuples(Students)

-Functions
    -"Routines" that perform some computation given 0 or more input paramates,
    which may or may not return to a value
    -Examples:
        -print(some values)
        -input()
        -str(5)
- Methods
    -Similiar to functions, but are used with some value.
'''

intlist = []

print(intlist)

inlist = [2,3,5,21,231,14]

print(intlist)

intlist.sort()# sort is a methond that can be used with a list

print(intlist)

stringlist = ["ics31","is","the",'best']

print(stringlist)

stringlist.sort()

print(stringlist)

#Booleans
print(4 !=5 )#true
print(4 >= 5)#false

#more about lists

names = ["Lenardo","Donatello","Michaelangelo","Raphael"]
temperatures = [65,66,70,68,70]

print(66 in temperatures)
print(100 in temperatures)
print("Splinter" in names)

#indexing
'''
indexing allows us to extract a specific element in a list
In computer science, we usually start counting at 0
Therefore, the list element of a list is at index 0, the 2nd element is at 1,
the last element is at index n -1, where n is the number of element in the list
'''
print(temperatures[0])
print("the first three",temperatures[0:3])

#Generalization
#[strating_index:one_past_last_index]
#Note: Starting_index is inclusive, one_past_last_index is exclusive

pri nt(temperatures[3:6])

    
