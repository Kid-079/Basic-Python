from tkinter import *

def clickButton1(event):
    print("Mouse Left Coordinates : " + str(event.x)+","+str(event.y))
    
def clickButton2(event):
    print("Mouse Center Coordinates : " + str(event.x)+","+str(event.y))
    
def clickButton3(event):
    print("Mouse Right Coordinates : " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",clickButton1)
window.bind("<Button-2>",clickButton2)
window.bind("<Button-3>",clickButton3)

window.mainloop()
