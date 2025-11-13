from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line(0,0,500,500,fill="#f70a1e",width=5)
#canvas.create_line(0,500,500,0,fill="#051cf0",width=5)
#canvas.create_rectangle(50,50,100,100,fill="#a915d6")
#canvas.create_polygon(200,0,400,400,0,400,fill="#f73f07",outline="black",width=5)

#points = [250,0,500,500,0,500]
#canvas.create_polygon(points,fill="#f73f07",outline="black",width=5)

#canvas.create_arc(0,0,500,500,fill="#02e3c1",outline="black",width=2,style=CHORD)
#canvas.create_arc(0,0,500,500,fill="#02e3c1",outline="black",width=2,style=ARC)

#canvas.create_arc(0,0,500,500,fill="#02e3c1",outline="black",width=2,style=PIESLICE,start=90)
#canvas.create_arc(0,0,500,500,fill="#02e3c1",outline="black",width=2,style=PIESLICE,start=270)

#canvas.create_arc(0,0,500,500,fill="#02e3c1",outline="black",width=2,style=PIESLICE,start=270,extent=180)

canvas.create_arc(0,0,500,500,fill="#f20a0a",extent=180,width=5)
canvas.create_arc(0,0,500,500,fill="#ffffff",extent=180,start=180,width=5)
canvas.create_oval(200,200,300,300,fill="#ffffff",width=5)

canvas.pack()

window.mainloop()

#canvas = widget that is used to draw graphs, plots, images in a window
