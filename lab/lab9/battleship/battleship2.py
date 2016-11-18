from collections import namedtuple

Ship = namedtuple('Ship','type points')

def fire(d:dict,T1:'target table',T2:'ocean view'):
    #error checking
    while True:
        target = input("Enter target's coordinate [A-J][0-9] to fire at:")
        if target[0].upper() in 'ABCDEFGHIJ' and int(target[1:]) in [0,1,2,3,4,5,6,7,8,9]:
            for name,ship in d.items():
                for point in ship.points:
                    if target == point:
                        print('hit')
                        hit = str_num(target)
                        set_H(T1,hit)
                        set_X(T2,hit)
                        
                        
                        break
                        
        else:
            print('invalid coordinate')
        return 


def str_num(s:str)->'list':
    ''' A1 => [0,1]'''
    table = str.maketrans('ABCDEFGHIJ','0123456789')
    l = [int(s[0].translate(table)),int(s[1])]
    return l
def set_H(T,l):
    '''shows in target table'''
    T[l[0],l[1]] = 'H'

def set_X(T,l):
    '''shows in ocean view'''
    T[l[0],l[1]] = 'X'

def create_table(rows:int,cols:int)->'2D table':
    ''' Create a 2D talbe with specified number of rows and columns
    '''
    Table = []
    for row in range(rows):
        Table.append(['_']*cols)
    return Table
    
def print_table(T:'2D Table'):
    '''print out the table in format
    '''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = '    '
    for cols in range(len(T[0])):
        s += str(cols) + ' '
    print(s)
    for row in range(len(T)):
        print("{:2s}: ".format(alphabet[row]),end = '')
        for col in range(len(T[0])):
            print("{:2s}".format(T[row][col]), sep='',end='')
        print()
    return

DIC_p1={'DES': Ship(type='DES', points=['C5', 'D5']),
 'CRU': Ship(type='CRU', points=['C3', 'D3', 'E3']),
 'BAT': Ship(type='BAT', points=['B2', 'C2', 'D2', 'E2']),
 'CAR': Ship(type='CAR', points=['A1', 'B1', 'C1', 'D1', 'E1']),
 'SUB': Ship(type='SUB', points=['C4', 'D4', 'E4'])}
p1_target = create_table(10,10)

print(Fire(DIC_p1,p1_target))
