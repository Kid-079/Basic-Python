from tkinter import *
from tkinter.ttk import *
import time

def start():
    bar['value']+=10
        
window = Tk()

bar = Progressbar(window,orient=HORIZONTAL,length=500)
bar.pack(pady=10)

button = Button(window,text="download",command=start).pack()

window.mainloop()
