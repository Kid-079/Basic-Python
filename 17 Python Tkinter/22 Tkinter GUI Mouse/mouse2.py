from tkinter import *

def clickButton1(event):
    print("You Click A Left Button")

def clickButton2(event):
    print("You Click A Center Button")

def clickButton3(event):
    print("You Click A Right Button")

window = Tk()

window.bind("<Button-1>",clickButton1)
window.bind("<Button-2>",clickButton2)
window.bind("<Button-3>",clickButton3)

window.mainloop()
