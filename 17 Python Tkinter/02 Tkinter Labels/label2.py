from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk() #instantiate an instance of a windowfg

Photo = PhotoImage(file='picture9.png')

label = Label(window,
              text="I Need A Miracle",
              font=('Times New Roman',50,'bold'),
              foreground='#00FF00',
              background='#0d240b',
              relief= GROOVE,
              bd=20,
              padx=25,
              pady=25,
              image=photo)
label.pack()
#label.place(x=0,y=0)
#label.place(x=20,y=20)
#label.place(x=50,y=50)

window.mainloop() #place window on computer screes, listen for events

