from tkinter import *

def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage,0,10)
def move_left(event):
    canvas.move(myimage,-10,0)
def move_right(event):
    canvas.move(myimage,10,0)

window = Tk()

window.bind("<W>",move_up)
window.bind("<S>",move_down)
window.bind("<A>",move_left)
window.bind("<D>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoImage = PhotoImage(file='icon/image2.png')
myimage = canvas.create_image(0,0,image=photoImage,anchor=NW)

window.mainloop()
