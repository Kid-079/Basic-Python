from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    messagebox.showinfo(title='Info Messagebox',message='Do Not Open The Message')
    
    #messagebox.showwarning(title='WARNING..!!!',message='Message Open')
    messagebox.showwarning(title='WARNING..!!!',message='You Have A Job')
    #messagebox.showwarning(title='WARNING..!!!',message='Baroto Infected Your Computer.!!')
    #messagebox.showwarning(title='WARNING..!!!',message='Job Progress Delaying...')
    #messagebox.showwarning(title='WARNING..!!!',message='Meet Another user To Complete The job')
    
    #messagebox.showinfo(title='Info Messagebox',message='User On A Project')
    messagebox.showinfo(title='Info Messagebox',message='User Busy Now')
    #messagebox.showinfo(title='Info Messagebox',message='Cannot Progress The Job')
    #messagebox.showinfo(title='Info Messagebox',message='Canceling The Job')
    
    #messagebox.showerror(title='ERROR',message='Somebody Watching You')
    messagebox.showerror(title='ERROR',message='Something Went Wrong -_-')
    #messagebox.showerror(title='ERROR',message='Your Computer Already Infected')


window = Tk()

button = Button(window,command=click,text='click here')
button.pack()

window.mainloop()
