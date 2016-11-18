# ICS 31 - 5-31

# Some review

'''
Review:

1D List: L = [1,2,3,4]
2D Lists: L = [ [1], [2], [3], [4] ]
    Index: L[0] = [1], L[0][0] = 1
3D Lists: L = [ [ [1] ], [ [2] ], [ [3] ], [ [4] ] ]
    Index: L[0] = [ [1] ], L[0][0] = [1], L[0][0][0] = 1
'''

'''
Today - Dictionaries within Dictionaries

- We want to keep track of all students who are enrolled in specific courses.
- Schedule is a Dictionary with the class name mapping to another dictionary containing
studentIDs mapping to Student namedtuples
'''

from collections import namedtuple

Student = namedtuple('Student', 'name id')

s1 = Student("Richert", 12345678)
s2 = Student("John Doe", 87654321)
s3 = Student("Jane Doe", 55555555)
s4 = Student("Mr. E", 11111111)
s5 = Student("Peter Anteater", 22222222)

Schedule = {'ICS31': {}, 'ICS32': {}, 'ICS33': {}}

#print(Schedule)

def print_schedule() -> None:
    ''' Prints the class schedule and enrolled students in a nice readable format
    '''
    for course, students in sorted(Schedule.items()):
        #print("Course = ", course)
        #print("Students = ", students)
        print("{:6s}:\n\t".format(course), end="")
        for studentId, student in students.items():
            print("id:{:8d}, name:{}\n\t".format(studentId, student.name), end="")
        print()

def add_Student(course: str, s: Student) -> None:
    #enrolled_students = Schedule[course] #Problem, crashes if course is not in schedule
    enrolled_students = Schedule.get(course)

    if enrolled_students == None: # course does not exist
        print("Course", course, "does not exist")
        return
    
    enrolled_students[s.id] = s
    return

def add_course(course: str) -> None:
    ''' Adds a course to the schedule
    '''

    if Schedule.get(course) == None:
        Schedule[course] = {}
    else:
        print("Course", course, "already exists")
    return

def remove_course(course: str) -> None:
    ''' Removes course from the schedule
    '''
    if Schedule.get(course) != None:
        Schedule.pop(course)
    else:
        print("Course", course, "does not exist")
    return

def remove_Student(course: str, s: Student) -> None:
    ''' Remove a student from the specified course
    '''
    enrolled_students = Schedule.get(course)

    if enrolled_students == None:
        print("Course", course, "does not exist")
        return

    if enrolled_students.get(s.id) == None:
        print("Student", s.name, "is not enrolled in", course)
        return

    enrolled_students.pop(s.id)
    return

#print_schedule()
add_Student('ICS31', s1)
add_Student('ICS31', s2)
add_Student('ICS32', s3)
add_Student('ICS33', s4)
print_schedule()
print('*' * 20)

add_course('ICS45J')
add_Student('ICS45J', s5)
add_Student('ICS199', s4)
print_schedule()
print('*' * 20)

add_Student('ICS45J', s4) # one student in multiple courses
print_schedule()
print('*' * 20)

remove_Student('ICS45J', s1) # student is not enrolled
remove_Student('ICS45J', s4)
remove_Student('ICS199', s1) # 199 does not exist
print_schedule()
print('*' * 20)

remove_course('ICS199') # 199 does not exist
remove_course('ICS45J')
print_schedule()


# How about using Lists instead of Dictionaries

Schedule_List = [ [], [], [] ] # Three courses, ICS 31, 32, and 33.

def print_schedule_list() -> None:
    ''' Prints the Schedule_list in a nice format
    '''
    print("PRINTING SCHEDULE USING LISTS IN LISTS")
    index = 0
    for students in Schedule_List:
        if index == 0:
            course = "ICS31"
        elif index == 1:
            course = "ICS32"
        elif index == 2:
            course = "ICS33"
        else:
            print("Course does not exist")
            return

        print("{:6s}:\n\t".format(course), end="")
        for student in students:
            print("id:{:8d}, name:{}\n\t".format(student.id, student.name), end="")
        print()
        index += 1
    return


def add_student_in_list(course: str, student: Student) -> None:
    ''' Adds a student in the appropriate position in the list
    '''
    if course == 'ICS31':
        index = 0
    elif course == 'ICS32':
        index = 1
    elif course == 'ICS33':
        index = 2
    else:
        print("Course does not exist")

    enrolled_students = Schedule_List[index]
    if student not in enrolled_students:
        enrolled_students.append(student)
        Schedule_List[index] = enrolled_students

add_student_in_list("ICS31", s1)
add_student_in_list("ICS31", s2)
add_student_in_list("ICS33", s3)
print_schedule_list()
    

print_schedule_list()
