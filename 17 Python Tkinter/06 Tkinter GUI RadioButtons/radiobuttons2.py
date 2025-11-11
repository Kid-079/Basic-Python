#radio button = similiar to checkbox, but you can only select one from a group 

from tkinter import *

fruit = ["blueberry","blackberry","strawberry","cherry","cranberry"]

def expression():
    if(x.get()==0):
        print("I Really Like Blueberry!")
    elif(x.get()==1):
        print("I Really Like Blackberry!")
    elif(x.get()==2):
        print("I Really Like Strawberry!")
    elif(x.get()==3):
        print("I Really Like Cherry!")
    elif(x.get()==4):
        print("I Really Like Cranberry!")
    else:
        print("I Don't Like Fruit")


window = Tk()

blueberryImage = PhotoImage(file='icon/blueberry.png')
blackberryImage = PhotoImage(file='icon/blackberry.png')
strawberryImage = PhotoImage(file='icon/strawberry.png')
cherryImage = PhotoImage(file='icon/cherry.png')
pearImage = PhotoImage(file='icon/cranberry.png')

fruitImages = [blueberryImage,blackberryImage,strawberryImage,cherryImage,pearImage]
 
x = IntVar()

for index in range(len(fruit)):
    radiobutton = Radiobutton(window,
                              text=fruit[index],       #add text to radiobutton
                              variable=x,              #groups radiobutton together if they share the same variable
                              value=index,             #assign each radiobutton a different value
                              padx=25,
                              font=("Bookman Old Style",50),
                              image=fruitImages[index], #add images to radiobutton
                              compound='left',
                              indicatoron=0,             #eliminate circle indicators
                              width=500,                 #sets width radiobutton  
                              command=expression         #set command of radiobutton to function
                              )      
    #radiobutton.pack(anchor='w')
    radiobutton.pack(anchor=W)

window.mainloop()
