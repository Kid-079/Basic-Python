#text widget =functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)
    
window = Tk()

text = Text(window,
            bg="#e1fcf3",
            font=("Impact",10),
            #font=("Comic Sans",10),
            font=("Arabic Typesetting",10)
            height=10,
            width=20,
            padx=20,
            pady=20,
            fg="2f302e"
            )
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()
