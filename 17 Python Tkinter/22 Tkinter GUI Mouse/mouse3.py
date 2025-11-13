from tkinter import *

def clickButton1(event):
    print("Mouse Coordinates : " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",clickButton1)
#window.bind("<Button-2>",clickButton2)
#window.bind("<Button-3>",clickButton3)

window.mainloop()
