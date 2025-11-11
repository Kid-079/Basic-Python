#listbox = A listing of selectable text items within it's own container

from tkinter import *

def submit():

    vegetables = []
    
    for index in listbox.curselection():
        vegetables.insert(index,listbox.get(index))

    print("Legendary Cooking Ingredients : ")
    for index in vegetables:
        print(index)
    
def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#03fca1",
                  #bg="#ff0b03",
                  font=('Courier New',30),
                  width=10,
                  selectmode=MULTIPLE
                 )
listbox.pack()

listbox.insert(1,"ginger")
listbox.insert(2,"turmeric")
listbox.insert(3,"garlic")
listbox.insert(4,"onion")
listbox.insert(5,"tomato")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,text="submit",command=submit)
submitButton.pack()

addButton = Button(window,text="add",command=add)
addButton.pack()

deleteButton = Button(window,text="delete",command=delete)
deleteButton.pack()

window.mainloop()
