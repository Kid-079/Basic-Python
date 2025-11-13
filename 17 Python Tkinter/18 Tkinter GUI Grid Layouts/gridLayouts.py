from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter Data Here : ",font=("Lao UI",20)).grid(row=0,column=0,columnspan=2)

userNameLabel = Label(window,text="Username : ",width=20,bg="#f2058b").grid(row=1,column=0)
userNameEntry = Entry(window).grid(row=1,column=1)

emailAddressLabel = Label(window,text="Email Address : ",bg="#02f5c3").grid(row=2,column=0)
emailAdressEntry = Entry(window).grid(row=2,column=1)

passwordLabel = Label(window,text="Password : ",bg="#b3f205",width=40).grid(row=3,column=0)
passwordEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=5,column=0,columnspan=5)

window.mainloop()

#grid = geometry manager that organize widgets in a table-like structure in a parent
