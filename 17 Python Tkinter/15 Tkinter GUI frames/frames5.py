from tkinter import *

window = Tk()

frame = Frame(window,bg="#fc03c6",bd=5,relief=SUNKEN)
frame.pack(side=BOTTOM)
#frame.place(x=0,y=0)
#frame.place(x=100,y=100)
#frame.place(x=100,y=50)
#frame.place(x=50,y=100)

Button(frame,text="C",font=("Arial",30),width=3).pack(side=TOP)
Button(frame,text="J",font=("Arial",30),width=3).pack(side=BOTTOM)
Button(frame,text="T",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="R",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="V",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Arial",30),width=3).pack(side=LEFT)


window.mainloop()
