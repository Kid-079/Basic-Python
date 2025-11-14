from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

basket_ball = Ball(canvas,0,0,100,1,1,"#e03b09")
tennis_ball = Ball(canvas,0,0,35,2,3,"#52e908")
pingpong_ball = Ball(canvas,0,0,15,3,2,"#fc8905")
golf_ball = Ball(canvas,0,0,25,2,1,"#fa8a4d")
volley_ball = Ball(canvas,0,0,50,3,1,"#8fd8f7")

while True:
    basket_ball.move()
    tennis_ball.move()
    pingpong_ball.move()
    golf_ball.move()
    volley_ball()
    window.update()
    time.sleep(0.01)
    

window.mainloop()
