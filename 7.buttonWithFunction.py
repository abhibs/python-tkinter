from tkinter import *

root = Tk()
root.geometry('500x500')

label = Label(root, text="Abhiram")
button = Button(root, text="Update")

label.pack()
button.pack()

root.mainloop()