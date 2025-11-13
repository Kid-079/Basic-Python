from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1       
tab2 = Frame(notebook) #new frame for tab 2
tab3 = Frame(notebook) #new frame for tab 3
tab4 = Frame(notebook) #new frame for tab 4
tab5 = Frame(notebook) #new frame for tab 5       

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.add(tab4,text="Tab 4")
notebook.add(tab5,text="Tab 5")
#notebook.pack(expand=True) #expand = expand to fill any space not otherwise used
                                       #fill = fill space on x and y axis
notebook.pack(expand=True,fill="both")
#notebook.pack(expand=True,fill="x")
#notebook.pack(expand=True,fill="y")

Label(tab1,text="Tab 1 = CONGRATULATION, You Got A Beautiful Water Dipper",width=20,height=10).pack()
Label(tab2,text="Tab 2 = This is Tab 2",width=20,height=10).pack()
Label(tab3,text="Tab 3 = This is Tab 3",width=20,height=10).pack()
Label(tab4,text="Tab 4 = SUCCESSFULLY, You Got A Limited Wastafel",width=20,height=10).pack()
Label(tab5,text="Tab 5 = This is Tab 5",width=20,height=10).pack()

window.mainloop()
