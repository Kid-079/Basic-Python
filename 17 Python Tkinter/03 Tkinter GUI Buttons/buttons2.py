from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)
    
window = Tk()

button = Button(window,text='Click Here!!!')
button.config(command=click) #performs call back a Function
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#03fc17')
button.config(fg='#0723f5')
button.config(activebackground='#f50707')
button.config(activeforeground='#f5f5f7')
Image = PhotoImage(file='logo1.png')
button.config(image=image)
button.config(compound='bottom')
button.config(state=ACTIVE)
#button.config(state=DISABLED) #disabled button (ACTIVE/DISABLED)
label = Label(window,text=count)
label.config(font=('Arial',50))
label.pack()
button.pack()
window.mainloop()



#button = click it, then does stuff

