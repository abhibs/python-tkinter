from tkinter import *

root = Tk()
root.geometry("650x650+650+250")
root.title("Abhiram B S")

menuBar = Menu(root)
root.config(menu=menuBar)

file = Menu(menuBar)
menuBar.add_cascade(label='File', menu=file)

file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Exit")

root.mainloop()