from tkinter import *

def display():
    if(x.get()==1):
        print("Keep Smile")
    else:
        print("Don't Be Angry")
        
window = Tk()

x = IntVar()

checkbox = Checkbutton(window,text='Checkpoint',variable=x,onvalue=1,offvalue=0,command=display)
checkbox.pack()
checkbox.config(font=('Arial',20))
checkbox.config(fg='#fa0a0a')
checkbox.config(bg='#ffffff')
checkbox.config(activeforeground='#fa0a0a')
checkbox.config(activebackground='#ffffff')
photo = PhotoImage(file='icon/picture42.png')
checkbox.config(image=photo,compound='left')
window.mainloop()
