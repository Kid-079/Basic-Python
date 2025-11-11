#radio button = similiar to checkbox, but you can only select one from a group 

from tkinter import *

fruit = ["blueberry","blackberry","strawberry","cherry","cranberry"]

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
                              width=500                  #sets width radiobutton      
                              )      
    #radiobutton.pack(anchor='w')
    radiobutton.pack(anchor=W)

window.mainloop()
