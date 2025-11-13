from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    #tasks = 5
    #tasks = 3
    #tasks = 1
    x = 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        
window = Tk()

bar = Progressbar(window,orient=HORIZONTAL,length=500)
bar.pack(pady=10)

button = Button(window,text="download",command=start).pack()

window.mainloop()
