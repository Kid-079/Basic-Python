from tkinter import *

def pressButton(event):
    print("You Press A Button")

window = Tk()

window.bind("<k>",pressButton)

window.mainloop()



