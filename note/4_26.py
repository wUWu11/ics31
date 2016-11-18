#ICS 31, 4-26-16

from collections import namedtuple

Course = namedtuple('Course','dept num title instr units')

#All fields are strings except for units

ics31 = Course('ICS','31','Intro to Programming','Wang',4)
ics132 = Course('ICS','132','Computer Networks','Wang',4)
ics46 = Course('ICS','46','Data Structures','Thornton',4)
ics139w = Course('ICS','139W','Critical Writing','Alfaro',4)
math2a = Course('MATH','2A','Calculus I','Doe',4 )
humanities1a = Course('HUMAN','1A','Humanities core I','Mr.E',4)
music160 = Course('MUSIC','160','university Orchestra','Tucker',2)

####
Student = namedtuple('Student','ID name level major studylist')

s1 = Student(12345678,'Doe,John','FR','ICS',[ics31,math2a,humanities1a])
s2 = Student(11111111,'Doe,Jane','SO','MATH',[math2a,humanities1a,music160])
s3 = Student(22222222,'Wang Richert','JR','ICS',[ics46,ics139w,ics132])
s4 = Student(33333333,'Anteater, Peter','SR','IN4MATX',[ics139w,music160,ics46])

SB = [s1,s2,s3,s4]

def num_students(SL:'list of student')->int:
    '''Return the number of students in SL
    '''
    return len(SL)

assert num_students(SB) == 4

def num_ICS_majors(SL:'list of student')->int:
    '''Return the number of ICS majors in SL
    '''
    total = 0
    for s in SL:
        if s.major == 'ICS':
            total = total + 1
    return total

assert num_ICS_majors(SB) == 2


def num_majors(SL:'list of students', major_to_count:str)->str:
    '''Return the number of students in SL whose major matches
       the parameter major_to_count
    '''
    total = 0
    for s in SL:
        if s.major == major_to_count:
            total +=1
    return total

assert num_majors(SB,"ICS") == 2
assert num_majors(SB,"ECON") == 0

'''
imagine trying to calculate various majors...
num_majors(SB,'ICS') +num_majors(SB,'IN4MATIXS')+...

'''
def num_majors2(SL: 'list of Student', majors_to_count: 'list of str') ->int:
    ''' Return number of strudents with a major in majors_to_count
    '''
    total = 0
    for s in SL:
        if s.major in majors_to_count:
            total += 1
    return total

assert num_majors2(SB, ['ICS']) == 2
assert num_majors2(SB, ['CGS']) == 0
assert num_majors2(SB, ['ICS', 'IN4MATX']) == 3
assert num_majors2(SB, ['MATH', 'BIM', 'ECON']) == 1


def num_seniors_in_majors(SL: 'list of Student', majors: 'list of str') ->int:
    ''' Return number of seniors in the list of majors
    '''
    total = 0
    for s in SL:
        if s.major in majors and s.level == "SR":
            total = total + 1
    return total

assert num_seniors_in_majors(SB, ['ICS', 'IN4MATX']) == 1
assert num_seniors_in_majors(SB, ['ICS']) == 0


def num_majors_at_level(SL: 'list of Student', majors: 'list of str',
levels: 'list of str') -> int:
    ''' Return the number of students for the specified majors at the
specified
        levels
    '''
    total = 0
    for s in SL:
        if s.major in majors and s.level in levels:
            total += 1
    return total


assert num_majors_at_level(SB, ['ICS', 'IN4MATX'], ['SR']) == 1
assert num_majors_at_level(SB, ['ICS', 'MATH'], ['SR']) == 0
assert num_majors_at_level(SB, ['MATH', 'ECON', 'IN4MATX', 'ICS'], ['FR',
'SO']) == 2


def total_enrollments(SL: 'list of Student') -> int:
    ''' Return the seats occupied by all students for all classes
    '''
    total = 0
    for s in SL:
        total += len(s.studylist) # classes a student is enrolled in
    return total

assert total_enrollments(SB) == 12


def units_enrolled(s: Student) -> int:
    ''' Return the number of units for the student's studylist
    '''
    total = 0
    for c in s.studylist:
        total += c.units
    return total

assert units_enrolled(s1) == 12
assert units_enrolled(Student(87654321, 'Shmo, Joe', 'FR', 'CS', [])) == 0


def total_units_enrolled(SL: 'list of Students') -> int:
    ''' Return number of units enrolled by all students in SL
    '''
    total = 0
    for s in SL:
        total += units_enrolled(s)
    return total

assert total_units_enrolled(SB) == 44
assert total_units_enrolled([]) == 0


def total_units_enrolled2(SL: 'list of Students') -> int:
    ''' Return number of units enrolled by all students
    '''
    total = 0
    for s in SL:
        for c in s.studylist:
            total += c.units
    return total

assert total_units_enrolled2(SB) == 44
assert total_units_enrolled2([]) == 0


def average_units(SL: 'list of Students') -> float:
    ''' Return average enrolled units per student
    '''
    if len(SL) == 0:
        return 0
    else:
        return total_units_enrolled(SL) / len(SL)

assert average_units(SB) == 11
assert average_units([]) == 0


def majors_at_level(SL: 'list of Student', majors: 'list of str', levels:
'list of str') -> 'list of Student':
    ''' Return a list of students in specified majors at specified class
levels
    '''

    result = []
    for s in SL:
        if s.major in majors and s.level in levels:
            result = result + [s]
    return result

assert majors_at_level(SB, ['ICS'], ['FR', 'SO', 'JR']) == [s1, s3]

