from tkinter import *

def submit():
    print("The Score is: " + str(scale.get()) + " Point")

window = Tk()

hotImage = PhotoImage(file='icon/hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,   #orientation of scales
              font=('Arial',20),
              tickinterval=10,   #add numeric indicator
              #showvalue=0,       #hide current value
              #resolution=5,       #increment of slider
              troughcolor='#52f7d6',
              fg = '#c91404'
              bg = '#e9f5f2'
              )
              
#scale.set(50)
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
#scale = Scale(window,from_=100,to=0)
scale.pack()

coldImage = PhotoImage(file='icon/cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()
