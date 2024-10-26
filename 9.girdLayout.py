from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x450")


lbltitle = ttk.Label(text='Abhiram B S', font=(('Arial'), 22))
lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password')

entry1 = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

entry1.insert(0, 'Enter Your Name')
entry2.insert(0, 'Enter Your Password')

button = ttk.Button(root, text="Login")


root.mainloop()
