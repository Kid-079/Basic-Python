from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
oneLine = canvas.create_line(0,0,500,500,fill="#f70a1e",width=5)
twoLine = canvas.create_line(0,500,500,0,fill="#051cf0",width=5)
canvas.pack()

window.mainloop()

#canvas = widget that is used to draw graphs, plots, images in a window

