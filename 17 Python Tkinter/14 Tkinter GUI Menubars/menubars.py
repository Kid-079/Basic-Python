from tkinter import *

def newFile():
    print("Created new file!")
def openFile():
    print("File has been open!")
def saveFile():
    print("File has been save!")
def saveAsFile():
    print("Save as file!")

def undoFile():
    print("Undo Progress!")
def redoFile():
    print("Redo Progress!")
def cutFile():
    print("Cut files or text!")
def copyFile():
    print("Copy files or text!")
def pasteFile():
    print("Paste files or text!")

def documentationFile():
    print("Show Documentation!")
def refreshFile():
    print("Refresh Application!")
def updatesFile():
    print("Check for Updates!")
def aboutFile():
    print("About Application!")

window = Tk()

newImage = PhotoImage(file="icon/new.png")
openImage = PhotoImage(file="icon/open.png")
saveAsImage = PhotoImage(file="icon/saveAs.png")
exitImage = PhotoImage(file="icon/exit.png")

undoImage = PhotoImage(file="icon/undo.png")
redoImage = PhotoImage(file="icon/redo.png")
cutImage = PhotoImage(file="icon/cut.png")
copyImage = PhotoImage(file="icon/copy.png")
pasteImage = PhotoImage(file="icon/paste.png")

documentationImage = PhotoImage(file="icon/documentation.png")
refreshImage = PhotoImage(file="icon/refresh.png")
updatesImage = PhotoImage(file="icon/check.png")
aboutImage = PhotoImage(file="icon/about.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("leelawadee",20))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newFile,image=newImage,compound='left')
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Save As",command=saveAsFile,image=saveAsImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0,font=("leelawadee",20))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo",command=undoFile,image=undoImage,compound='left')
editMenu.add_command(label="Redo",command=redoFile,image=redoImage,compound='left')
editMenu.add_command(label="Cut",command=cutFile,image=cutImage,compound='left')
editMenu.add_command(label="Copy",command=copyFile,image=copyImage,compound='left')
editMenu.add_command(label="Paste",command=pasteFile,image=pasteImage,compound='left')

helpMenu = Menu(menubar,tearoff=0,font=("leelawadee",20))
menubar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Documentation",command=documentationFile,image=documentationImage,compound='left')
helpMenu.add_command(label="Refresh",command=refreshFile,image=refreshImage,compound='left')
helpMenu.add_command(label="Check for Updates",command=updatesFile,image=updatesImage,compound='left')
helpMenu.add_command(label="About",command=aboutFile,image=aboutImage,compound='left')

window.mainloop()
