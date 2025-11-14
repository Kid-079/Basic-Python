from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

basket_ball = Ball(canvas,0,0,100,1,1,"#e03b09")

while True:
    basket_ball.move()
    window.update()
    time.sleep(0.01)
    

window.mainloop()
