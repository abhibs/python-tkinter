from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("650x650+650+250")
root.title("Abhiram B S")


def exitFunction():
    mbox = messagebox.askquestion("Exit", "Are You Sure To Exit ?", icon='warning')
    if mbox == 'yes':
        root.destroy()

menuBar = Menu(root)
root.config(menu=menuBar)

file = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label='File', menu=file)

file.add_command(label="New")
file.add_separator()
file.add_command(label="Open")
file.add_separator()
file.add_command(label="Save")
file.add_separator()
icon = PhotoImage(file='icons/exit.png')
file.add_command(label="Exit", image=icon, compound=LEFT, command=exitFunction)

root.mainloop()