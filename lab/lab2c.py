#Deyu Wu 0952612, Yuyi Chen 64913564

#C1
print('How many hours?')
hours = int(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = int(input())
print('This many dollars per hour:  ',"$", rate)
print('Weekly salary:  ',"$", hours * rate)

#C2
Name = str(input('Hello. What is your name'))
print("Hello.",Name)
print("It's nice to meet you.")
Age = int(input("how old are you?"))
Agenextyear = Age + 1
print("next year you will be ", Agenextyear , "years old")
print("Good bye!")

#D
print("Please provide this information:")
Business_name = str(input("Business name:"))
euros = int(input("Number of euros"))
pounds = int(input("Number of pounds"))
dollars = int(input("Number of dollars"))

krone_eu = 7.46 * euros
krone_po = 9.51 * pounds
krone_do = 6.20 * dollars
total = krone_eu + krone_po + krone_do

print("Copenhagen Chamber of Commerce")
print("Business name:" + Business_name)
print(euros , "enros is" , krone_eu , "krone")
print(pounds , "pounds is" , krone_po , "krone")
print(dollars , "dollar is" , krone_do , "krone")
print("Total krone:" , total)

#E
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

print(still_another.title)#e1
print(another.price)#e2

price_average = (favorite.price + another.price + still_another.price)/3
print(price_average)#e3

print(favorite.year < 1900)

still__another = Book("Pride and Prejudice"," Jane Austen", 1813, 9.99)
still___another = Book("Invitation to Computer Science (Introduction to CS)"," G.Michael Schneider and Judith Gersting",2012,203.95)#e4


still_another=still_another._replace(price = 26)
print(still_another.price)#e5
still_another=still_another._replace(price = 1.2* still_another.price)
print(still_another.price)#e6

from collections import namedtuple
#f
Animal = namedtuple("animal", "name species age weight food")
animal1 = Animal("Jumbo","elephant",50,1000,"peanuts")
animal2 = Animal("Perry","platypus",7,1.7,"shirmp")
print(animal1.weight < animal2.weight)
#g
booklist = [favorite, another, still_another]
print(booklist[0].price < booklist[1].price)
print(booklist[0].year > booklist[-1].year)

#h
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

print(RC[2].name)#h1
print(RC[0].dish == RC[3].dish )#h2
print(RC[-1].price)#h3
RC.sort()
print(RC)#h4

print(RC[-1].dish)#h5

l = [RC[0],RC[1],RC[-2],RC[-1]]
print(l)#h6


import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 100, 300, fill='orange') 
my_canvas.create_line(100, 100, 300, 100, fill='blue')   
my_canvas.create_line(300, 100, 300, 300, fill='blue')
my_canvas.create_line(100, 300, 300, 300, fill='green')
my_canvas.create_line(100, 200, 200, 100, fill='blue')
my_canvas.create_line(100, 200, 200, 300, fill='blue') 
my_canvas.create_line(200, 300, 300, 200, fill='blue') 
my_canvas.create_line(200, 100, 300, 200, fill='blue') 

          # Combine all the elements and display the window


my_window2 =tkinter.Tk()
#i3
my_canvas2 =tkinter.Canvas(my_window2,width=1000,height=1000)
my_canvas2.pack()
my_canvas2.create_polygon(350,400,650,150,950,400,fill="orange")
my_canvas2.create_line(400, 400, 900, 400, fill='orange') 
my_canvas2.create_line(400, 400, 400, 900, fill='blue')   
my_canvas2.create_line(900, 400, 900, 900, fill='blue')
my_canvas2.create_line(400, 900, 900, 900, fill='green')
my_canvas2.create_polygon(700,900,800,900,800,700,700,700,fill='brown')
my_canvas2.create_polygon(500,500,500,600,600,600,600,500,)

#i4
my_window3 = tkinter.Tk()
my_canvas3 = tkinter.Canvas(my_window3,width=500,height=500)
my_canvas3.pack()
my_canvas3.create_oval(0,200,500,400)
my_canvas3.create_oval(100,200,400,400,fill="blue")
my_canvas3.create_oval(200,250,300,350,fill="black")

tkinter.mainloop()


