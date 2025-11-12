from tkinter import *
from tkinter import messagebox #import messagebox library

def click():
    #SHOW INFO
    messagebox.showinfo(title='Info Messagebox',message='Do Not Open The Message')
    
    #SHOW WARNING
    #messagebox.showwarning(title='WARNING..!!!',message='Message Open')
    messagebox.showwarning(title='WARNING..!!!',message='You Have A Job')
    #messagebox.showwarning(title='WARNING..!!!',message='Baroto Infected Your Computer.!!')
    #messagebox.showwarning(title='WARNING..!!!',message='Job Progress Delaying...')
    #messagebox.showwarning(title='WARNING..!!!',message='Meet Another user To Complete The job')
    
    #SHOW INFO
    #messagebox.showinfo(title='Info Messagebox',message='User On A Project')
    messagebox.showinfo(title='Info Messagebox',message='User Busy Now')
    #messagebox.showinfo(title='Info Messagebox',message='Cannot Progress The Job')
    #messagebox.showinfo(title='Info Messagebox',message='Canceling The Job')
    
    #SHOW ERROR
    #messagebox.showerror(title='ERROR',message='Somebody Watching You')
    messagebox.showerror(title='ERROR',message='Something Went Wrong -_-')
    #messagebox.showerror(title='ERROR',message='Your Computer Already Infected')

    #ASKOKCANCEL
    #if messagebox.askokcancel(title='New Message Received',message='Can You Help Me To Do This Thing?'):
        #print('You Did A Thing!')
    #else:
        #print('You Canceled A Thing!')
        
    #ASKRETRYCANCEL
    #if messagebox.askretrycancel(title='New Message Received',message='Something Went Wrong'):
        #print('You Retried A Thing!')
    #else:
        #print('You Canceled A Thing!')
        
    #ASKYESNO
    #if messagebox.askyesno(title='New Message Received',message='Can You Help Me To Do This Thing?'):
        #print('Yes,I Can')
    #else:
        #print('No, I Cant')
        
    #ASKQUESTION
    #print (messagebox.askquestion(title='New Message Received',message='Can You Help Me?'))
    answer = messagebox.askquestion(title='New Message Received',message='Do You Like Stories?')
    if (answer == 'yes'):
        print('I Like Stories')
    else:
        print('Why You Do Not Like Stories? -_- ')

    #print(messagebox.askyesnocancel(title='New Message Received',message='Do You Like Stories?'))
    answer = messagebox.askyesnocancel(title='New Message Received',message='Do You Like Stories?',icon='warning')
    if(answer==True):
        print("I Really Like Stories")
    elif(answer==False):
        print("Why You Do Not Like Stories?")
    else:
        print("Someone Do Not Want To Answer The Question")
    
    
window = Tk()

button = Button(window,command=click,text='click here')
button.pack()

window.mainloop()
