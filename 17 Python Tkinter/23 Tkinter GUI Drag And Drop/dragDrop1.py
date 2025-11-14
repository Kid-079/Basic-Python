from tkinter import *

def drag_analog(event):
    label.analogX = event.x
    label.analogY = event.y

def drag_motion(event):
    x = label.winfo_x() - label.analogX + event.x
    y = label.winfo_y() - label.analogY + event.y
    label.place(x=x,y=y)
    
    
window = Tk()

label1 = Label(window,bg="#d40408",width=10,height=5)
label1.place(x=0,y=0)

label2 = Label(window,bg="#0c29e8",width=10,height=5)
label2.place(x=0,y=0)

label1.bind("<Button-1>",drag_analog)
label1.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_analog)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()
