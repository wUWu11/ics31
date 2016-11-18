# ICS 31, 6-2-16

'''
- Final Exam will be longer than the midterm
- Exam is cumulative (covers everything)

Functions
    - Design recipes, parameters, return values

Selection / Conditional Statements
    - if, else, elif

Repitition and Loops
    - for, while, continue, break

Types
    - Basic types (int, str, float, boolean, None)
    - Objects (Namedtuples)
    - Collections (lists, dictionaries, sets)

Assert Statements
    - Used for testing / validating functionality
    - Know how to read / write them

Text Processing
    - Strings, slicing, indexing, finding, startswith, endswith, count, translation
    split, strip, formatting, etc.

File I/O
    - Reading, Writing, parsing, open / close ...

Dictionaries
    - Syntax, indexing D['John'], properties of dictionaries (mutable, keys are immutable, values are
    anything), keys are unique, keys are not guaranteed to be in order
    - Methods
        .pop(), .update(), .keys(), .items(), .values()

Sets
    - Syntax is like dictionaries without the mapping to a value
    - Set methods (.add(), .remove(), .discard(), clear() ...

Tuples
    - Liked namedtuples, except there is no name (and items are indexed by position)
    - Each item can be indexed with [] (similar to lists)
    - unlike lists, tuples are immutable.

Random
    - know things like randrange...

Structures
    - Lists, Dictionaries, Sets, 2D Lists, Dictionaries in Dictionaries, Namedtuples with 2D Lists
    with dictionaries, containing lists....

Structure of Exam
    - Similar to midterms
        - Will be longer (2 hours allocated)
        - Questions like "What does this evaluate to" or "What type is this?"
        - Complete the function definition
        - What is incorrect about a code snippet

Advice
    - Understanding lectures (and examples), labs (be sure you can write it independently),
    Quizzes (be sure to take them seriously... helps prepare for exams), Textbook (perkovich or zybooks),
    Prototyping ("I wonder how python behaves when ..." - write a simple proof-of-concept)
'''

from collections import namedtuple

X = namedtuple('X', 'name')

L = [0,1,2] # mutable
x1 = X('some name')

y1 = x1
y2 = x1

print(y1)
print(y2)

x1 = X("some other name")

print(y1)
print(y2)

'''
y1 = L
y2 = L

print(y1)
print(y2)

L[1] = 100

print(y1)
print(y2)
'''
