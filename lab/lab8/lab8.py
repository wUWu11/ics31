#Deyu WU, 0952612 .  ICS 31 Lab sec 7.  Lab asst 8.
#finish lab8 by myself
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')


#---------part C-------------
print('#####PART C######')
print()
print('____part c1____')

def read_menu_with_count(f:str):
    '''takes as an argument a string naming a file in this format,
       reads the file, and returns a list of Dish structures created
       from the data.
    '''
    infile =  open(f,'r')
    data = infile.readlines()
    datalist = []
    for i in data:
        m = i.replace('\n','')
        datalist.extend(m.split('\t'))
    namel = []
    pricel = []
    caloriesl = []
    menu = []
    for i in range(len(datalist[1:])):
        if i% 3 == 1:
            namel.append(datalist[i])
        if i% 3 == 2:
            pricel.append(datalist[i].replace('$',''))
        if i % 3 == 0:
            caloriesl.append(datalist[i])
    for n in range(int(datalist[0])):
        dish = Dish(namel[n],float(pricel[n]),float(caloriesl[n]))
        menu.append(dish)
    infile.close()
    return menu

print(read_menu_with_count('menu2.txt'))    

#
print()
print('____part c2____')
def read_menu(f:str):
    '''  takes as an argument a string naming a file in this format,
        reads the file, and returns a list of Dish structures created from the data
    '''
    infile = open(f,'r')
    data = infile.readlines()
    datalist = []
    for i in data:
        m = i.replace('\n','')
        datalist.extend(m.split('\t'))
    namel = []
    pricel = []
    caloriesl = []
    menu = []
    for i in range(len(datalist)):
        if i% 3 == 0:
            namel.append(datalist[i])
        if i% 3 == 1:
            pricel.append(datalist[i].replace('$',''))
        if i % 3 == 2:
            caloriesl.append(datalist[i])
    for n in range(int(len(datalist)/3)):
        dish = Dish(namel[n],float(pricel[n]),float(caloriesl[n]))
        menu.append(dish)
    infile.close()
    return menu
print(read_menu('menu3.txt'))
#
print()


menu = read_menu('menu3.txt')
def write_menu(l:'list of Dish',f:str):
    '''takes as its argument a list of Dish namedtuples and a string that names a file.
       Your function should write the Dish data to the named file
    '''
    outfile = open(f,'w')
    menu_str = str(len(l)) + '\n'
    for dish in l:
        menu_str += dish.name + '\t$' +str(dish.price) +'\t' +str(dish.calories) +'\n'
    outfile.write(menu_str)
    outfile.close()
#test
#write_menu(menu,'copy.txt')
#---------part D-------------

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])

StudentBody = [sW, sX, sY, sZ]

#________d 1 ___________
def Students_at_level(SL:'list of Students',level:str)->'list of students':
    '''takes a list of Students and a string (representing a class level, e.g., 'FR' or 'SO')
       and returns a list of students whose class level matches the parameter.
    '''
    result = []
    for s in SL:
        if s.level ==  level:
            result = result + [s]
    return result
#test part
assert Students_at_level([],'FR') == []
assert Students_at_level([sW],'FR') == [sW]

#________d 2 ____________
def Students_in_majors(SL:'list of Students',ML:'list of str'):
    '''takes a list of Students and a list of strings (where each string represents a major) and
       returns a list of Students that have majors on the specified list.
    '''
    result = []
    for s in SL:
        if s.major in ML:
            result.append(s)
    return result
# test part
assert Students_in_majors([],['PSB','CS']) == []
assert Students_in_majors([sW,sX],['PSB','CS']) == [sW,sX]

#________d 3____________


def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    return c1.dept == c2.dept and c1.num == c2.num

assert Course_equals(ics31,ics32) == False
assert Course_equals(ics31,ics31) == True

def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    for course in SL:
        if Course_equals(course,c):
            return True
    return False

assert Course_on_studylist(ics31,[ics32,bio97]) == False
assert Course_on_studylist(ics32,[ics31,bio97,ics32]) == True
          
def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	studylist (and False otherwise)
    '''
    for course in S.studylist:
        if course.dept == department and course.num == coursenum:
            return True
    return False

def Students_in_class(SL:'list of students',dept:str,num:str):
    '''takes a list of Students, and two strings - a department name and a course number
    (e.g., 'ICS' and '31') - and returns a list of those Students who are enrolled in the
    specified class.'''
    new_SL = []
    for s in SL:
        if Student_is_enrolled(s,dept,num):
            new_SL.append(s)
    return new_SL

assert Students_in_class(StudentBody,'ICS','31') == [sW,sX]
assert Students_in_class([],'ICS','31') == []


#________d 4____________
def Student_names(SL:"list of students"):
    '''a list of Students and returns a list of just the names of those students'''
    result = []
    for s in SL:
        result.append(s.name)
    return result




#________d 5____________
ICS_major_s  = Students_in_majors(StudentBody,['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS'])
print(ICS_major_s)

names_ICS_major = Student_names(ICS_major_s)
print(names_ICS_major)

num_ICS_major = len(ICS_major_s)
print(num_ICS_major)

names_sr_ICS_major = Student_names(Students_at_level(ICS_major_s,'SR'))
print(names_sr_ICS_major)

num_sr_ICS_major = len(names_sr_ICS_major)
print(num_sr_ICS_major)

majorTotal = 5
percentage = num_sr_ICS_major/(100*majorTotal)
print(str(percentage) +"%")


num_fr_ICS_ics31 = len(Students_in_class(Students_at_level(ICS_major_s,'FR'),'ICS','31'))
print(num_fr_ICS_ics31)

num_fr_ICS_ics31 = 1 #assume
total = 0
for s in Students_in_class(Students_at_level(StudentBody,'FR'),'ICS','31'):
    for c in s.studylist:
        total += c.units
average_units = total/num_fr_ICS_ics31

print(average_units)



