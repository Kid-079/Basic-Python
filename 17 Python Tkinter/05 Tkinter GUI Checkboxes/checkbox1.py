from tkinter import *

def display():
    print("Keep Struggle")

window = Tk()

x = IntVar()
checkbox = Checkbutton(window,text='Checkpoint',variable=x,onvalue=1,offvalue=0,command=display)

window.mainloop()
