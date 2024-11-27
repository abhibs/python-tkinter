from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Abhiram B S")

root.geometry("500x450")

textBox = Text(root, width=60, height=20, wrap=WORD)
textBox.grid(row=0, column=0)

scroll = ttk.Scrollbar(root, orient=VERTICAL, command=textBox.yview)
scroll.grid(row=0, column=1, sticky=N+S)
textBox.config(yscrollcommand=scroll.set)

root.mainloop()