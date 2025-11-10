#entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    
window = Tk()

submit = Button(window,text="submit",command=submit)
submit.pack(side = BOTTOM)

entry = Entry()
entry.config(font=('Times New Roman',50))
entry.config(bg='f70905')
entry.config(bg='ffffff')
#entry.insert(0,'Energetic')
#entry.config(state=DISABLED) #ACTIVE/DISABLED
#entry.config(state=ACTIVE) #ACTIVE/DISABLED
entry.config(width=10)
entry.config(show='*')
#entry.config(show='%')
entry.pack()

window.mainloop()
