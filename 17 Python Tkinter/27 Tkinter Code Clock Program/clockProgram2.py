from tkinter import *
from time import *

def update():
    #time_string = strftime("%H:%M:%S")  #24-Hours
    time_string = strftime("%I:%M:%S %p")   #12-Hours
    
    time_label.after(1000,update)
    
    #time_label.config()
    

window = Tk()

time_label = Label(window,font=("Bookman Old Style",50),fg="#2ef202",bg="#000000")
time_label.pack()

update()

window.mainloop()
