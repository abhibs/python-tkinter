from tkinter import *
from tkinter import ttk

root = Tk()

button1 = Button(root, text='Login')
button2 = ttk.Button(root, text='Login')

button1.pack()
button2.pack()

root.mainloop()