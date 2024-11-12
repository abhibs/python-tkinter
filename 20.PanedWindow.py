from tkinter import *
from tkinter import ttk


root = Tk()


root.geometry("650x650+650+200")

pw = ttk.PanedWindow(root, orient=HORIZONTAL)
frame1 = ttk.Frame(pw, width=200, height=500, relief=SUNKEN)
frame2 = ttk.Frame(pw, width=200, height=500, relief=SUNKEN)
frame3 = ttk.Frame(pw, width=75, height=500, relief=SUNKEN)

pw.add(frame1)
pw.add(frame2)

# pw.insert(0, frame3)
pw.insert(1, frame3)

pw.pack(fill=BOTH)



lbl = Label(frame2, text="Abhiram B S", pady=30)
btn = Button(frame2, text="Login")


lbl.pack()
btn.pack()

root.mainloop()