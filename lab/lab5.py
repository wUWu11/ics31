#Deyu Wu X0952612 . Zan Yang 78143521

# part c
#

#------------c1------------

from collections import namedtuple

Dish = namedtuple('Dish','name price calories')
d1 = Dish("Double-Double",3.45,400)
d2 = Dish('sushi',5.00,300)
d3 = Dish('Orange chicken',6.50,450)
d4 = Dish('Orange chicken',10.00,450)
d5 = Dish('Fried rice',5.00,300)
#------------c2------------

def Dish_str(a:Dish)->str:
    '''takes a Dish object and returns string in form of name (price): calories'''
    return a.name + "($"+ str(a.price) +"):" + str(a.calories)


print(Dish_str(d1))

#------------c3------------

def Dish_same(a:Dish,b:Dish)->bool:
    '''takes two dishes as arguments and returns True if the name and calories
       counts are the same'''
    return a.name == b.name and a.calories == b.calories

assert Dish_same(d1, d1) == True
assert Dish_same(d1, d2) == False
assert Dish_same(d1, d4) == False
assert Dish_same(d3, d4) == True


#------------c4------------
def Dish_change_price(a:Dish,number:float)->Dish:
    '''return a Dish which its price is changed
       the number represents a percentage change in price'''
    a = a._replace(price = a.price*(1+number/100) )
    return a 
assert Dish_change_price(d2,50) == Dish('sushi',7.50,300)
assert Dish_change_price(d2,-50) == Dish('sushi',2.50,300)

#------------c5------------
def Dish_is_cheap(a:Dish,number:float)->bool:
    '''return True if the Dish's price is less than the number
    '''
    return a.price < number

print(Dish_is_cheap(d3,10))
assert Dish_is_cheap(d2,6) == True
assert Dish_is_cheap(d3,10) == True

#------------c6------------
DL =[d1,d2,d3,d4,d5]
print(len(DL))
DL.sort()
print(DL)
DL2 = [Dish('pasta',10.99,500),
       Dish('salmon',15.00,300),
       Dish('Fries',3.25,300),
       Dish('salad',5.20,290)]

DL.extend(DL2)
print(DL)

def Dishlist_display(a:'list of Dishes')->str:
    '''return string of each dish on a new line'''
    result = ''
    for i in a:
        result += str(i) + '\n'
    return result
print(Dishlist_display(DL))

#------------c7------------

def Dishlist_all_cheap(a:'list of Dishes',number:float)->bool:
    ''' returns True if the price of every dish on the list is less than that number
    '''
    for i in a:
        if not Dish_is_cheap(i,number):
            return False
    return True

assert Dishlist_all_cheap(DL,20) == True
assert Dishlist_all_cheap(DL,10) == False


#------------c8------------
def Dishlist_change_price(a:'list of Dishes',b:float)->'list of dishes':
    '''takes a list of Dishes and a number representing a percentage change and returns
       a list of Dishes with each price changed by the specified amount.
    '''
    for i in range(len(a)):
        a[i] = Dish_change_price(a[i],b)
    return a
        
    
print(Dishlist_change_price(DL,100))

#------------c9------------
def Dishlist_prices(a:'list of Dishes')->list:
    '''takes a list of Dishes and returns a list of numbers containing
       just the prices of the dishes on that list.'''
    l = []
    for i in a:
        l.append(i.price)
    return l
print(Dishlist_prices(DL))

#------------c10------------
def Dishlist_average(a:'list of Dishes')->float:
    '''takes a list of Dishes and returns the average price of those dishes.
    '''
    result = 0
    for i in Dishlist_prices(a):
        result += i
    return result/len(a)
print(Dishlist_average(DL))
#------------c11------------
def Dishlist_keep_cheap(a:'list of Dishes',number:float)->"list of dishes":
    '''takes a list of Dishes and a number and
       returns a list of those dishes on the original list that have prices less than that number'''
    l = []
    for i in a:
        if Dish_is_cheap(i,number):
            l.append(i)
    return l
print(Dishlist_keep_cheap(DL2,5))

#------------c12------------
DL.extend([Dish('potato',5.10,100),
          Dish('chicken',4.50,500),
          Dish('fish',6.00,300),
          Dish('beef',8.00,400),
          Dish('lamb',10.00,500),
          Dish('tofu',3.50,300),
          Dish('noodle',7.00,200),
          Dish('curry',3.00,150),
          Dish('pork',5.00,320),
          Dish('fruits',10.00,300),
          Dish('sandwich',8.50,490),
          Dish('beef noodle',3.50,899),
          Dish('chicken rice',8.59,600),
          Dish('apple pie',5.00,340),
          Dish('orange pie',5.00,330),
          Dish('pizza',5.00,999),
          Dish('fish cake',6.00,890)]
          )
print(len(DL))

def before_and_after():
    ''' takes no parameters. It prompts the user for interactive input of a number
        representing a percentage change in prices;
        then it prints the result of Dishlist_display on your big list of Dishes;
        then it changes all the prices of the Dishes on the big list;
        then it prints the result of Dishlist_display again '''
    a = float(input('input a number you want chang in prices'))
    print('before Dishlist \n',Dishlist_display(DL))
    print('after Dishlist \n',Dishlist_display(Dishlist_change_price(DL,a)))

before_and_after()    


# part e
#------------e------------   
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])	

#------------e1------------
r3 = Restaurant('Pascal','French','940-752-0107',[Dish('escargots',12.95,250),
                                                  Dish('poached salmon' ,18.50, 550),
                                                  Dish( 'rack of lamb',24.00,850),
                                                 Dish('marjolaine cake',8.50,950)])
#------------e2------------
def Restaurant_first_dish_name(a:Restaurant)->str:
    if a.menu != []:
        return a.menu[0].name
    else:
        return ''

assert Restaurant_first_dish_name(r1) == 'Mee Krob'
assert Restaurant_first_dish_name(Restaurant('Taillevent', 'French', '01-44-95-15-01',[]))==''


#------------e3------------
def Restaurant_is_cheap(a:Restaurant,number:float)->bool:
    return Dishlist_average(a.menu) <= number

assert Restaurant_is_cheap(r3,24)

#------------e4------------
Collection = [r1,r2,r3]

def Dish_raise_price(a:Dish,number:float)->Dish:
    '''takes a Dish and returns the price of dish  raised by number
    '''
    a = a._replace(price = a.price+number)
    return a

assert Dish_raise_price(Dish('escargots',12.95,250),10) == Dish('escargots',22.95,250)

def menu_raise_price(a:'list of Dish',number:float)->'list of Dish':
    '''takes a list of Dish return the list with the price of dish raised by number
    '''
    result = []
    for i in a:
        result.append(Dish_raise_price(i,number))
    return result

assert menu_raise_price([Dish('escargots',12.95,250),Dish('poached salmon' ,18.50, 550)],10)== [Dish('escargots',22.95,250),Dish('poached salmon' ,28.50, 550)]

def Restaurant_raise_price(a:Restaurant,number:float)->Restaurant:
    '''take a Restaurant and return the Restaurant with the price of dishes rasied by number
    '''
    a = a._replace(menu =menu_raise_price(a.menu,number) )
    return a

def Collection_raise_price(a:'list of Restaurant',number:float)->'list of Restaurant':
    '''take a list of restaurant and return the list that all Resaurants' dishes price have raised by number
    '''
    result = []
    for i in a:
        result.append(Restaurant_raise_price(i,number))
    return result
print(Collection_raise_price(Collection,2.5))

def Restaurant_change_price(a:Restaurant,number:float)->Restaurant:
    '''take a Restaurant and return price increse by the number percentage
    '''
    a = a._replace(menu = Dishlist_change_price(a.menu,number))
    return a

def Collection_change_price(a:'list of Restaurant',number:float)->'list of restaurant':
    result = []
    for i in a:
        result.append(Restaurant_change_price(i,number))
    return result
print(Collection_change_price(Collection,50))

#------------e5------------
def Collection_select_cheap(a:'list of Restaurant',number:float)->'list of restaurant':
    #takes a Collection and a number and returns a list of all the Restaurants in the collection whose average price is less than or equal to that number
    result = []
    for i in a:
        if Restaurant_is_cheap(i,number):
            result.append(i)
    return result
print(Collection_select_cheap(Collection,25))


#------------g------------
Count = namedtuple('Count','letter number')
def letter_count(a:str,b:str)->'list of Count':
    result = []
    
    for n in b:
        result.append(Count(n,a.lower().count(n.lower())))
    return result

assert letter_count('apple__happy','a_p') == [Count(letter='a', number=2), Count(letter='_', number=2), Count(letter='p', number=4)]
assert letter_count('apple__happy','A_p') == [Count(letter='A', number=2), Count(letter='_', number=2), Count(letter='p', number=4)]
assert letter_count('Apple__hAppy','a_p') == [Count(letter='a', number=2), Count(letter='_', number=2), Count(letter='p', number=4)]
