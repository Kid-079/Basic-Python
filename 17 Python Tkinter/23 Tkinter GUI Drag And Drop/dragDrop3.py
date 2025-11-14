from tkinter import *

def drag_analog(event):
    widget = event.widget
    widget.analogX = event.x
    widget.analogY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.analogX + event.x
    y = widget.winfo_y() - wdiget.analogY + event.y
    widget.place(x=x,y=y)
    
    
window = Tk()

label1 = Label(window,bg="#d40408",width=10,height=5)
label1.place(x=0,y=0)

label1.bind("<Button-1>",drag_analog)
label1.bind("<B1-Motion>",drag_motion)


label2 = Label(window,bg="#0c29e8",width=10,height=5)
label2.place(x=0,y=0)

label2.bind("<Button-1>",drag_analog)
label2.bind("<B1-Motion>",drag_motion)


label3 = Label(window,bg="#fcf403",width=10,height=5)
label3.place(x=0,y=0)

label3.bind("<Button-1>",drag_analog)
label3.bind("<B1-Motion>",drag_motion)

window.mainloop()
