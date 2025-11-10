from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = servers as a container to hold or contains these widgets

window = Tk() #instantiate an instance of a window

#SIZE
#window.geometry("240x120")
#window.geometry("240x480")
window.geometry("360x360")
#window.geometry("640x360")

#TITLE
window.title("Graphical User Interface")

#ICON
icon = PhotoImage(file='icon/picture2.png')
window.iconphoto(True,icon)

#BACKGROUND
#window.config(background="black")
window.config(background="#50f50a")

window.mainloop() #place window on computer screes, listen for events



