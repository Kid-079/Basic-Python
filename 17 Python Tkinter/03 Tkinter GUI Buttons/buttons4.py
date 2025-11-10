from tkinter import *

count = 0
def click():
    global count
    count += 1
    label.config(text=count)
    label2.pack()
    
window = Tk()

button = Button(window,text='Click Here!!!')
button.config(command=click) #performs call back a Function
button.config(font=('Ink Free',50,'bold'))
button.config(bg='#03fc17')
button.config(fg='#0723f5')
button.config(activebackground='#f50707')
button.config(activeforeground='#f5f5f7')
image1 = PhotoImage(file='Picture2.png')
image2 = PhotoImage(file='Picture12.png')
button.config(image=image1)
button.config(compound='bottom')
button.config(state=ACTIVE)
#button.config(state=DISABLED) #disabled button (ACTIVE/DISABLED)
label = Label(window,text=count)
label.config(font=('Arial',50))
label.pack()
button.pack()
label2 = Label(window,image=image2)
window.mainloop()

#button = click it, then does stuff

