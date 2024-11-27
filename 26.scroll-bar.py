from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Abhiram B S")

root.geometry("500x450")

textBox = Text(root, width=60, height=20, wrap=WORD)
textBox.grid(row=0, column=0)

root.mainloop()