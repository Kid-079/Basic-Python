from tkinter import *
from time import *

def update():
    #time_string = strftime("%H:%M:%S")  #24-Hours
    time_string = strftime("%I:%M:%S %p")   #12-Hours
    time_label.config(text=time_string)
    
    day_string = strftime("%A") 
    day_label.config(text=day_string)
    
    date_string = strftime("%d-%B-%Y") 
    date_label.config(text=date_string)
    
    window.after(1000,update)
    
    #time_label.config()
    

window = Tk()

time_label = Label(window,font=("Bookman Old Style",50),fg="#2ef202",bg="#000000")
time_label.pack()

day_label = Label(window,font=("Lucida Console",25))
day_label.pack()

date_label = Label(window,font=("Meiryo",35))
date_label.pack()

update()

window.mainloop()
