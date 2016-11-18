# ICS 31, 4-19-16

'''
Recap
    -We made a restaurants program
        -Very simply, but somewhat useful

Python details - Mutable vs immutable objects.

List are MUTABLE
'''

L = [10,20,30,40]
print(L)
L[2] = 300
print(L)


#Namedtuples are IMMUTABLE
from collections import namedtuple

Book = namedtuple("Book","title author")
b1 = Book('Harry Potter and the Goblet of Fire','Rowling')
print(b1)

#b1.author = "J.K. Rowling" CRASH! Namedtuples are immutable

'''
How do we change the author in this Book namedtuple
1.create a new object
'''
#b1 = Book(b1.title,"J.K. Rowling")# Create new book object with update

'''
2.use the _replace method
'''

b1 = b1.replace(author='J.K. Rowling')# returns a updated namedtuple
print(b1)


