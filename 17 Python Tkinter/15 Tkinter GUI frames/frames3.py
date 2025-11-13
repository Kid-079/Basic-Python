from tkinter import *

window = Tk()

frame = Frame()

button = Button(window,text="C",font=("Arial",30),width=3).pack(side=TOP)
button = Button(window,text="J",font=("Arial",30),width=3).pack(side=BOTTOM)
button = Button(window,text="T",font=("Arial",30),width=3).pack(side=LEFT)
button = Button(window,text="R",font=("Arial",30),width=3).pack(side=LEFT)
button = Button(window,text="V",font=("Arial",30),width=3).pack(side=LEFT)
button = Button(window,text="D",font=("Arial",30),width=3).pack(side=LEFT)


window.mainloop()
