from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("650x650+650+200")


tabs = ttk.Notebook(root)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text="First Tab")
tabs.add(tab2, text="Second Tab")

tabs.pack(fill=BOTH)

root.mainloop()