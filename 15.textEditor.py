from tkinter import *

root = Tk()

root.geometry("550x550")

texteditor = Text(root, width=30, height=10)
texteditor.grid(row=0, column=0, padx=40, pady=20)

root.mainloop()