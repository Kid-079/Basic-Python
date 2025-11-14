from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-1)

window = Tk()

window.geometry("500x500")

window.bind("<d>",move_up)

myimage = PhotoImage(file='icon/image2.png')
label = Label(window,image=myimage,bg="#c90404")
label.place(x=0,y=0)

window.mainloop()

