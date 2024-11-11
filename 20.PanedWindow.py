from tkinter import *
from tkinter import ttk


root = Tk()


root.geometry("650x650+650+200")

pw = ttk.PanedWindow(root, orient=HORIZONTAL)
frame1 = ttk.Frame(pw, width=100, height=500, relief=SUNKEN)
frame2 = ttk.Frame(pw, width=300, height=500, relief=SUNKEN)

pw.add(frame1)
pw.add(frame2)

pw.pack(fill=BOTH)

root.mainloop()