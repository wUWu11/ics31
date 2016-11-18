#ICS 31 3-31

'''
Terminology
-Processor: Central processing unit(CPU). It just does computations

-Memory/storage: Random Access Memory(RAM)/Hard drive(magnetic)/soild state drive(SSD)

-Peripherals:Keyboard,Mouse,Webcam,Monitors,speakers

-Software
    -Think of a chef following a recipe
    -Executing something using a step-by-step procedure
    -Programs are form of data (loaded add executed by the computer)
'''

#compute weekly salary
hours = 40
rate = 10

salary = hours * rate
print("Salary is $" + str(salary))#print out the salary

#Escape Characters
print("Hello ICS 31!")
print("\"Hello ICS 31!\"") #for "
print("\'Hello ICS 31!\'") #for '
print("Hello\t ICS\t 31!") #for tab
print("Hello\nICS 31")     #for new line

'''
Software tries to model the real world
you can think of everything with respect to 'things' and 'actions'
    -Things (nouns ) -Objects
        -int:-3, float:3.1415, string: "Gary"
    -Actions (verbs) -Functions: operators, statements
        -print()
'''
# a larger example (tip calculator)
TAX_RATE = 0.1 #symbolic constant
print("Hi,please enter your name:")
username = input()
print("HI", username, ". What's the amout of your bill(not including tax)")
totalBill = float(input())
print("What is the tip percentage you would like to leave?")
tipPercentage = float(input())
taxAmount = totalBill * TAX_RATE
tipAmount = totalBill * (tipPercentage/100)
print("The total amount to pay is $", totalBill + taxAmount + tipAmount)

'''
Some more terminology

Syntax - grammar , how you say something
Semantics - meaning, what it does

Syntactically incorrect: PI equals 3.14159
Semantically incorrect: PI = "apple"

Multi - value data
    - LISTS
        -[1,2,4,5,6]
    - Nametuples - package heterogeneous things into a item

'''

#using a nametuple

#First: import the appropriate components

from collections import nametuple

# Second: Define what your object looks like

Student = nametuple("Student", "name id major GPA" )

#Third: Create distinct students

s1 = student("John Doe", 12345678, "ics", 3.5)
s2 = student("Jane Doe", 81442144, "ics", 3.9)

print(s1.name)
print(s2.name)


