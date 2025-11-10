from tkinter import *

def display():
    if(x.get()==1)&(y.get==0):
        print("Keep Smile")
    elif(x.get()==0)&(y.get==1):
        print("Keep Struggle")
    elif(x.get()==1)&(y.get==1):
        print("Keep Smile And Keep Struggle")
    else:
        print("Don't Be Angry")
        
window = Tk()

x = IntVar()
y = IntVar()

checkbox1 = Checkbutton(window,text='Checkpoint 1',variable=x,onvalue=1,offvalue=0,command=display)
checkbox1.pack()
checkbox1.config(font=('Arial',20))
checkbox1.config(fg='#fa0a0a')
checkbox1.config(bg='#ffffff')
checkbox1.config(activeforeground='#fa0a0a')
checkbox1.config(activebackground='#ffffff')
photo1 = PhotoImage(file='icon/picture42.png')
checkbox1.config(image=photo1,compound='left')
checkbox1.config(padx=25,pady=25,width=300,height=50)
checkbox1.config(anchor='e')

checkbox2 = Checkbutton(window,text='Checkpoint 2',variable=x,onvalue=1,offvalue=0,command=display)
checkbox2.pack()
checkbox2.config(font=('Arial',20))
checkbox2.config(fg='#fa0a0a')
checkbox2.config(bg='#ffffff')
checkbox2.config(activeforeground='#fa0a0a')
checkbox2.config(activebackground='#ffffff')
photo2 = PhotoImage(file='icon/picture59.png')
checkbox2.config(image=photo2,compound='left')
checkbox2.config(padx=25,pady=25,width=300,height=50)
checkbox2.config(anchor='w')

window.mainloop()
