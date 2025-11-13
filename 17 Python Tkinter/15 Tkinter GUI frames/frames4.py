from tkinter import *

window = Tk()

frame = Frame(window,bg="#fc03c6")
frame.pack()

Button(frame,text="C",font=("Arial",30),width=3).pack(side=TOP)
Button(frame,text="J",font=("Arial",30),width=3).pack(side=BOTTOM)
Button(frame,text="T",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="R",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="V",font=("Arial",30),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Arial",30),width=3).pack(side=LEFT)


window.mainloop()
