from tkinter import *

def pressButton(event):
    #print("You Press : " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",pressButton)
#window.bind("<k>",pressButton)

label = Label(window,font=("Miriam",50))
label.pack()

window.mainloop()



