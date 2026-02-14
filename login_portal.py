from tkinter import *
from functools import partial

def validationLogin(username,password):
	print(f"Username: {username}")
	print(f"Password: {password}")

	return

tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('github.com')

usernameLabel = Label(tkWindow, text='User Name').grid(row=0,column=0)
username = StringVar()
usernameEntry = Entry(tkWindow,textvariable = username).grid(row=0,column=1)

passwordLabel = Label(tkWindow, text="Password").grid(row=1,column=0)
password = StringVar()
passwordEntry = Entry(tkWindow,textvariable=password).grid(row=1,column=1)

validationLogin = partial(validationLogin,username,password)

loginButton = Button(tkWindow,text='login',command=validationLogin).grid(row=4,column=0)

tkWindow.mainloop()