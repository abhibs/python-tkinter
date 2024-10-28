from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("350x250")

button1 = ttk.Button(root, text='Button One')
button2 = ttk.Button(root, text='Button Two')



button1.grid(row=0, column=0, pady=25, padx=50)
button2.grid(row=0, column=1)


root.mainloop()