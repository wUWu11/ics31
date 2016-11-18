#Nam Nguyen 33615140, Deyu Wu 0952612
#c

#_________c1_________

def abbreviate(a): #This function takes a name as input and return its frist three characters
    return a[0:3]
print(abbreviate("computerscience"))
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'

#_________c2_________

def find_area_square(b:int)->int:#takes as input a number representing the length of one side of a square and returns the area of that square.
    return b**2
print(find_area_square(5))
assert find_area_square(1) == 1
assert find_area_square(5) == 25

#_________c3_________

def find_area_circle(c:int)->int:#takes as its input the radius of a circle and returns the area of that circle
    return 3.14159*(c**2)
print(find_area_circle(2))
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975

#_________c4_________

def print_even_numbers(d):
    for i in range(len(d)):
        if d[i]%2 == 0 :
            print(d[i])
print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])

#_________c5_________

def calculate_shipping(weight):
    if weight < 2:
        return 2
    if weight >= 2 and weight < 10:
        return 5
    if weight >= 10:
        return (weight-10)*1.5 +5
print(calculate_shipping(17))
assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50

#_________c6_________
import tkinter
my_window = tkinter.Tk()   

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  
my_canvas.pack() 

def create_square(x,y,length):# (x,y) is upper-left corner,create a square
    return my_canvas.create_rectangle(x,y,x+length,y+length)
create_square(100,100,100)

#_________c7_________

def create_circle(x,y,diameter):# (x,y)upper-left corner of the square that encloses the circle 
    return my_canvas.create_oval(x,y,x+diameter,y+diameter)
create_circle(100,100,100)
tkinter.mainloop() 

#d

#_________d1_________
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

def restaurant_price(restaurant):# returns price of restaurant inputted
    return restaurant.price

print(restaurant_price(RC[1]))

#_________d2_________
RC.sort(key=restaurant_price)
print(RC)


#_________d3&d4_________
print(RC)
def costliest(l):# function returns restaurant with most expensive dish
    l.sort(key=restaurant_price)
    return l[-1].name

print(costliest(RC))
print(RC)

#e
from collections import namedtuple
#_________e1_________
Book = namedtuple('Book', 'author title genre year price instock')
BSI = [
    Book("J.R.R. Tolkien", "Lord of the Rings: Fellowship of the Ring", "fantasy", 1954, 7.50, 6),
    Book("J.R.R. Tolkien", "Lord of the Rings: The Two Towers", "fantasy", 1954, 5.00, 12),
    Book("J.R.R. Tolkien", "Lord of the Rings: Return of the King", "fantasy", 1955, 9.99, 18),
    Book("Michael Lewis", "The Blind Side: Evolution of a Game", "Non-fiction", 2006, 9.91, 30),
    Book("Michael Lewis", "The Big Short: Inside the Doomsday Machine", "Finance", 2010, 10.62, 9),
    Book("Michael Lewis", "The New New Thing: A Silicon Valley Story", "Technology", 1999, 3.25, 3)  ]
for i in range(len(BSI)):
    print(BSI[i].title)

    

#_________e2_________
    

def alpha(n):
    n = sorted (n, key=lambda n: n.title)
    for i in range(len(n)):
        print(n[i].title)
alpha(BSI)

#_________e3_________

a = []
n = 0
while n < len(BSI):
    a.append(Book(BSI[n].author, BSI[n].title, BSI[n].genre, BSI[n].year, BSI[n].price * 1.1, BSI[n].instock))
    print(BSI[n].author, BSI[n].title, BSI[n].genre, BSI[n].year, BSI[n].price * 1.1, BSI[n].instock)
    n = n + 1
BSI = a
#_________e4_________

n = 0
while n < len(BSI):
    if BSI[n].genre == "Technology":
        print(BSI[n].title)
    n = n + 1

#_________e5_________

titles_before_2000 = []
titles_after_2000 = []
n = 0
while n < len(BSI):
    if BSI[n].year > 2000:
        titles_after_2000.append(BSI[n].title)
    else:
        titles_before_2000.append(BSI[n].title)
    n = n + 1
print("The titles of books before the year 2000 are:", titles_before_2000)
print("The titles of books after the year 2000 are:", titles_after_2000)

#_________e6_________

def inventory_value(x):
    #This function determines the value of your entire inventory of books
    value = []
    n = 0
    while n < len(x):
        value.append(x[n].price * x[n].instock)
        n = n + 1
    return print("The value of your inventory is worth", sum(value), "dollars.")

inventory_value(BSI)

#_________e7_________
import tkinter
my_window2 = tkinter.Tk()   

my_canvas2 = tkinter.Canvas(my_window2,width=1000, height=1000)  

my_canvas2.pack() 
def draw_eye(x:float,y:float,value: float):#return three circles which make a eye
    my_canvas2.create_oval(x,y,x+value,y+value)
    my_canvas2.create_oval(x+(value/5),y+(value/5),x+(value*3/4),y+(value*3/4),fill ="pink")
    my_canvas2.create_oval(x+(value/3),y+(value/3),x+(2*value/3),y+(2*value/3),fill ="black")   


draw_eye(150,150,100)
draw_eye(350,150,100) #eyes

my_canvas2.create_line(300,300,275,350)
my_canvas2.create_line(275,350,350,350) # nose

my_canvas2.create_oval(240,430,360,450,fill="orange")#mouth
my_canvas2.create_oval(100,50,500,550)#face
tkinter.mainloop() 
