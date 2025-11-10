from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk() #instantiate an instance of a window

label = Label(window,text="I Need A Miracle")
label.pack()
#label.place(x=0,y=0)
#label.place(x=20,y=20)
#label.place(x=50,y=50)

window.mainloop() #place window on computer screes, listen for events

