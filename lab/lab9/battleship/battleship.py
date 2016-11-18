#Deyu Wu 0952612, Erik Orellana 13656378


#Battleship Game


COMMANDS1 = """
Welcome to battleship
L: load game (game.txt)
N: start a new game
Q: Quit

Enter command:"""

COMMANDS2 = """
O: Print Ocean View
F: Fire at player
S: Save

Enter command:"""
def load_game():
    DATA = load_file()
    p1 = []
    p2 = []
    HP_p1 = {}
    HP_p2 = {}
    for i in range(4,9):
        HP_p1[DATA[i][0]] = int(DATA[i][1])
        p1.append(DATA[i][:1]+DATA[i][2:])
    for m in range(14,19):
        HP_p2[DATA[m][0]] = int(DATA[m][1])
        p2.append(DATA[m][:1]+DATA[m][2:])
    
    p1_target = create_table(10,10)
    p1_t = create_table(10,10)
    DIC_p1 = dict_ship(p1)
    p2_target = create_table(10,10)
    p2_t = create_table(10,10)
    DIC_p2 = dict_ship(p2)
    set_ships(p1_t,DIC_p1)
    set_ships(p2_t,DIC_p2)
    for s in  DATA[0]:#set H for p1 target
        if s != '': 
            set_H(p1_target,str_num(s))
    for s in DATA[10]:#set h for p2 target
        if s != '': 
            set_H(p2_target,str_num(s))
    for s in DATA[1]:#set miss for p1 target
        if s != '':
            set_M(p1_target,str_num(s))
    for s in DATA[11]:#set miss for p2 target
        if s != '':
            set_X(p2_target,str_num(s))
    for s in DATA[2]:#set X for p1 ocean view
        if s != '': 
            set_H(p1_t,str_num(s))
    for s in DATA[12]:#set X for p2 ocean view
        if s != '':
            set_X(p2_t,str_num(s))
    moves_p1 = int(DATA[9][0])
    hits_p1 = int(DATA[9][1])
    miss_p1 = int(DATA[9][2])
    moves_p2 = int(DATA[19][0])
    hits_p2 = int(DATA[19][1])
    miss_p2 = int(DATA[19][2])
    if DATA[20][0] == 'P2':
        while True:
            print()
            print('player 2"s turn')
            print_table(p2_target)
            if handle_commands_p2(DIC_p2,HP_p1,HP_p2,p2_t,p2_target,p1_t,moves_p2,hits_p2,miss_p2):
                stats_display(moves_p1,hits_p1,miss_p1,moves_p2,hits_p2,miss_p2)
                break 
            print()
            print("player 1's turn")
            print_table(p1_target)

            if handle_commands_p1(DIC_p1,HP_p1,HP_p2,p1_t,p1_target,p2_t,moves_p1,hits_p1,miss_p1):
                stats_display(moves_p1,hits_p1,miss_p1,moves_p2,hits_p2,miss_p2)
                break 
        
    if DATA[20][0] == 'P1':
        while True:
            print()
            print("player 1's turn")
            print_table(p1_target)

            if handle_commands_p1(DIC_p1,HP_p1,HP_p2,p1_t,p1_target,p2_t,moves_p1,hits_p1,miss_p1):
                break
            print()
            print('player 2"s turn')
            print_table(p2_target)

            if handle_commands_p2(DIC_p2,HP_p1,HP_p2,p2_t,p2_target,p1_t,moves_p2,hits_p2,miss_p2):
                stats_display(moves_p1,hits_p1,miss_p1,moves_p2,hits_p2,miss_p2)
                break 



def new_game():
    moves_p1 = 0
    hits_p1 = 0
    miss_p1 = 0
    moves_p2 = 0
    hits_p2 = 0
    miss_p2 = 0
    p1_target = create_table(10,10)
    p1_t = create_table(10,10)
    p1 = read_file('p1.txt')
    DIC_p1 = dict_ship(p1)
    set_ships(p1_t,DIC_p1)
    HP_p1 = dict_HP()
    p2_target = create_table(10,10)
    p2_t = create_table(10,10)
    p2 = read_file('p2.txt')
    DIC_p2 = dict_ship(p2)
    set_ships(p2_t,DIC_p2)
    HP_p2 = dict_HP()
    
    while True:
        print()
        print("player 1's turn")
        print_table(p1_target)
        if handle_commands_p1(DIC_p1,HP_p1,HP_p2,p1_t,p1_target,p2_t,moves_p1,hits_p1,miss_p1):
            break
        print()
        print('player 2"s turn')
        print_table(p2_target)
        if handle_commands_p2(DIC_p2,HP_p1,HP_p2,p2_t,p2_target,p1_t,moves_p2,hits_p2,miss_p2):
            break        
    

    
def handle_commands1():
    while True:
        response = input(COMMANDS1)
        if response.lower() == 'q':
            break
        if response.lower() == 'n':
            return new_game()
        if response.lower() == 'l':
            return load_game()
        else:
            print('invalid command, Enter command:')
    return 

def handle_commands_p1(d:'DIC_p1',HP1:'HP_P1',HP2:'HP_P2',T:'p1_t',T1:'p1_target',T2:'p2_t',a:'moves_p1',b:'hits_p1',c:'miss_p1'):
    while True:
        response = input(COMMANDS2)
        if response.lower() == 'o':
            print_table(T)
        elif response.lower() == 'f':
            a += 1
            if fire(d,HP1,T1,T2,a,b,c):
                b += 1
            else:
                c += 1
            HP_display(HP1,HP2)
            if game_status(check_HP(HP2)):
                print('PLAYER 1 WINS!!!!!!!!!!!')
                return True
            break
        elif response.lower() == 's':
            save_file()
            break
        else:
            print('invalid command')
    return False
def handle_commands_p2(d:'DIC_p2',HP1:'HP_P1',HP2:'HP_P2',T:'p2_t',T1:'p2_target',T2:'p1_t',a:'moves_p2',b:'hits_p2',c:'miss_p2'):
    while True:
        response = input(COMMANDS2)
        if response.lower() == 'o':
            print_table(T)
        elif response.lower() == 'f':
            a += 1
            if fire(d,HP1,T1,T2,a,b,c):
                b += 1
            else:
                c += 1
            
            
            HP_display(HP1,HP2)
            if game_status(check_HP(HP1)):
                print('PLAYER 2 WINS!!!!!!!!!!!!!')
                return True
            break
        elif response.lower() == 's':
            save_file()
            break
        else:
            print('invalid command')
    return False

from collections import namedtuple

Ship = namedtuple('Ship','type points')

#store data
##
###
def ships_position(s:str):
    '''take a str which represent name of file and create a file for player that includes ships position
    '''
    outfile = open(s,'w')
    data = ''
    print('Firstly, give 5 points which is your CARRIER')
    info1 = CAR_get_info()
    print('Secondly, give 4 points which represent your BAT')
    info2 = BAT_get_info()
    print('then, give 3 points that is your CRU')
    info3 = CRU_get_info()
    print('almost done, give 3 points that is your SUB')
    info4 = SUB_get_info()
    print('last one, give 2 points that represent your DES')
    info5 = DES_get_info()
    data = info1 +'\n' +info2+'\n'+info3+'\n'+info4+'\n'+info5
    outfile.write(data)
    outfile.close()

#ships get info
##
###
def CAR_get_info():
    l = ['CAR']
    for n in range(5):
        position = str(input('Please input the '+str(n+1)+'th points'))
        l.append(position)
        result = ','.join(l)
    return result
def BAT_get_info():
    l = ['BAT']
    for n in range(4):
        position = str(input('Please input the '+str(n+1)+'th points'))
        l.append(position)
        result = ','.join(l)
    return result
def CRU_get_info():
    l = ['CRU']
    for n in range(3):
        position = str(input('Please input the '+str(n+1)+'th points'))
        l.append(position)
        result = ','.join(l)
    return result
def SUB_get_info():
    l = ['SUB']
    for n in range(3):
        position = str(input('Please input the '+str(n+1)+'th points'))
        l.append(position)
        result = ','.join(l)
    return result
def DES_get_info():
    l = ['DES']
    for n in range(2):
        position = str(input('Please input the '+str(n+1)+'th points'))
        l.append(position)
        result = ','.join(l)
    return result


#dealing with data
##
###


def read_file(f:str):
    infile = open(f,'r')
    data = infile.readlines()
    datalist = []
    for i in data:
        m = i.replace('\n','')
        datalist.append(m.split(','))
    return datalist

def load_file():
    infile = open('game.txt','r')
    data = infile.readlines()
    datalist = []
    for i in data:
        m = i.replace('\n','')
        datalist.append(m.split(','))
    infile.close()
    
    return datalist
def save_file():
    print('save_file!')
    #outfile = open('game.txt','w')
    
def dict_ship(d:'2d list'):
    #error
    DIC = {}
    if len(d) != 5:
        print('Should have 5 ships!')
        return False
    for l in d:
        if l[0] == 'CAR':
            DIC['CAR'] = Ship('CAR',l[1:])
        if l[0] == 'BAT':
            DIC['BAT'] = Ship('BAT',l[1:])
        if l[0] == 'CRU':
            DIC['CRU'] = Ship('CRU',l[1:])
        if l[0] == 'SUB':
            DIC['SUB'] = Ship('SUB',l[1:])
        if l[0] == 'DES':
            DIC['DES'] = Ship('DES',l[1:])
    return DIC


# Table
##
###

def create_table(rows:int,cols:int)->'2D table':
    ''' Create a 2D talbe with specified number of rows and columns
    '''
    Table = []
    for row in range(rows):
        Table.append(['_']*cols)
    return Table




def alph_num(l:'list of str') ->'2D list':
    '''translate ['A1','B1','C1'] to [[0, 1], [1, 1], [2, 1]]'''
    
    table = str.maketrans('ABCDEFGHIJabcdefghij','01234567890123456789')
    result = []
    for s in l:
        result.append(str_num(s))
    return result

def str_num(s:str)->'list':
    ''' A1 => [0,1]'''
    table = str.maketrans('ABCDEFGHIJabcdefghij','01234567890123456789')
    if s == '':
        return []
    else:
        l = [int(s[0].translate(table)),int(s[1])]
    
    return l

#print(alph_num(['A1','B1','C1']))

def set_ships(T:'2D Table',D:dict)->None:
    for name,ship in D.items():
        list_points = alph_num(ship.points)
        for point in list_points:
            T[point[0]][point[1]] = '*'

    return T

#Fire and HP
##
###

def fire(d:dict,d2:'dic_HP',T1:'target table',T2:'ocean view',a,b,c):
    #error checking
    while True:
        target = input("Enter target's coordinate [A-J][0-9] to fire at:")
        
        pointlist = []
        if target != '':
            if target[0].upper() in 'ABCDEFGHIJ' and target[1:] in ['0','1','2','3','4','5','6','7','8','9']:
                hit = str_num(target)
                
                a += 1
                
                break
            else:
                print('invalid coordinate')
    for name,ship in d.items():
        for point in ship.points:
            pointlist.append(point)
            if target.upper() == point:
                print('\n'+name +' hit!!'+'\n')
                d2[name] = d2[name] - 1 #HP
                set_H(T1,hit)  
                set_X(T2,hit)
                b += 1
                return True
                
    if target.upper() not in pointlist:
        print('failed')
        set_M(T1,hit)
        c += 1
        return False

    return False


def set_H(T,l):
    '''shows in target table'''
    T[l[0]][l[1]] = 'H'

def set_X(T,l):
    '''shows in ocean view'''
    T[l[0]][l[1]] = 'X'

def set_M(T,l):
    '''shos in target table'''
    T[l[0]][l[1]] = 'M'
        
def dict_HP():
    dic = {}
    dic['CAR'] = 5
    dic['BAT'] = 4
    dic['CRU'] = 3
    dic['SUB'] = 3
    dic['DES'] = 2
    return dic


def HP_display(HP1,HP2):
    print('Player 1 Ships HP   Player 2 Ships HP')
    print('CAR - '+ str(HP1['CAR'])+ '              ' +'CAR - '+ str(HP2['CAR']))
    print('BAT - '+ str(HP1['BAT'])+ '              ' +'BAT - '+ str(HP2['BAT']))
    print('CRU - '+ str(HP1['CRU'])+ '              ' +'CRU - '+ str(HP2['CRU']))
    print('SUB - '+ str(HP1['SUB'])+ '              ' +'SUB - '+ str(HP2['SUB']))
    print('DES - '+ str(HP1['DES'])+ '              ' +'DES - '+ str(HP2['DES']))
def check_HP(HP):
    total = 0
    for name,num in HP.items():
        total += num
        if num == 0:
            print('###'+name + ' sunk!!'+'###')
    return total

def game_status(n:int):
    if n == 0:
        print('*******GAME OVER********')
        
        return True
    else:
        return False

def stats_display(a,b,c,d,e,f):
    print('        Player 1 Stats      Player 2 Stats')
    print('Moves:   {:2}           {}'.format(a,d))
    print('Misses:  {:2}           {}'.format(c,f))
    print('Hits:    {:2}           {}'.format(b,e))
    print('HIT %:   {:2.3f}     {:2.3f}'.format(b/(a),e/(d)))
    print('Miss%:   {:2.3f}     {:2.3f}'.format(c/(a),f/(d)))
    
    
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

handle_commands1()
