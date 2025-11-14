from tkinter import *

def drag_analog1(event):
    label1.analogX = event.x
    label1.analogY = event.y

def drag_motion1(event):
    x = label1.winfo_x() - label1.analogX + event.x
    y = label1.winfo_y() - label1.analogY + event.y
    label1.place(x=x,y=y)
    
def drag_analog2(event):
    label2.analogX = event.x
    label2.analogY = event.y

def drag_motion2(event):
    x = label2.winfo_x() - label2.analogX + event.x
    y = label2.winfo_y() - label2.analogY + event.y
    label2.place(x=x,y=y)
    
    
window = Tk()

label1 = Label(window,bg="#d40408",width=10,height=5)
label1.place(x=0,y=0)

label1.bind("<Button-1>",drag_analog1)
label1.bind("<B1-Motion>",drag_motion1)


label2 = Label(window,bg="#0c29e8",width=10,height=5)
label2.place(x=0,y=0)

label2.bind("<Button-1>",drag_analog2)
label2.bind("<B1-Motion>",drag_motion2)

window.mainloop()
