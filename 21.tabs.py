from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("650x650+650+200")


icon = PhotoImage(file='icons/favicon.png')

tabs = ttk.Notebook(root)

tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)

tabs.add(tab1, text="First Tab", image=icon, compound=LEFT)
tabs.add(tab2, text="Second Tab", image=icon, compound=LEFT)

tabs.pack(fill=BOTH)

lbl = ttk.Label(tab1, text='Abhiram B S')
lbl.pack(padx=50, pady=50)

btn = ttk.Button(tab2,text="Submit")
btn.pack(padx=50, pady=50)
root.mainloop()