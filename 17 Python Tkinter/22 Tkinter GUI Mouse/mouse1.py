from tkinter import *

def clickButton(event):
    print("You Click A Button")

window = Tk()

#window.bind("<Button-1>",clickButton)
window.bind("<Button-2>",clickButton)
#window.bind("<Button-3>",clickButton)

window.mainloop()
