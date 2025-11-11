from tkinter import *

def submit():
    print("The Score is: " + str(scale.get()) + " Point")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL #orientation of scales
              )
#scale = Scale(window,from_=100,to=0)
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
