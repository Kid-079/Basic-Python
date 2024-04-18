import tkinter

main_window = tkinter.Tk()

def press_button():
	label2 = tkinter.Label(main_window, text="Already Press The Button")
        label2.pack()
	
label = tkinter.Label(main_window, text="Good Morning \n Create Simple GUI \n Use Python")
button = tkinter.Button(main_window, text="press button", command= press_button)

label.pack()
button.pack()

main_window.mainloops()
