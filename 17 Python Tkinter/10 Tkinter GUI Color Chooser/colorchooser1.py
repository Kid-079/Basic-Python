from tkinter import *
from tkinter import colorchooser #submodule

def click():
    colorchooser.askcolor()

window = Tk()

window.geometry("360x360")
button = Button(text='click here',command=click)
button.pack()

window.mainloop()
