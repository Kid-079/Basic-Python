from tkinter import *
from tkinter import colorchooser #submodule

def click():
   color = colorchooser.askcolor()
   print(color)
   colorHex = color[1]
   print(colorHex)

window = Tk()

window.geometry("360x360")
button = Button(text='click here',command=click)
button.pack()

window.mainloop()
