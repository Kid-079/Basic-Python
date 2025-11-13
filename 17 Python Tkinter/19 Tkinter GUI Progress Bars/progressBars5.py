from tkinter import *
from tkinter.ttk import *
import time

def start():
    Size = 100
    #Size = 50
    #Size = 30
    #Size = 10
    download = 0
    speed = 1
    while(download<Size):
        time.sleep(0.05)
        bar['value']+=(speed/Size)*100
        download+=speed
        #percent.set(str((download/tasks)*100)+"%")
        percent.set(str(int((download/Size)*100))+"%")
        text.set(str(download)+"/"+str(Size)+" GB completed")
        windows.update_idletasks()
        
window = Tk()

percent = StringVar()
text = StringVar()

#bar = Progressbar(window,orient=HORIZONTAL,length=500)
bar = Progressbar(window,orient=VERTICAL,length=500)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()
