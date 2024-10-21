from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry('500x500')

entry = Entry(root, width=50)

# placeholder

entry.insert(0, "Please Enter Your Name")

entry1 = ttk.Entry(root, width=50)

entry.pack()
entry1.pack()

root.mainloop()