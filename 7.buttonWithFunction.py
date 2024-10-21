from tkinter import *

root = Tk()
root.geometry('500x500')


def changeName():
    label.config(text="Abhiram B S Javalli Tudoor Thirthahalli Shimoga", fg='red', bg='blue')

label = Label(root, text="Abhiram")
button = Button(root, text="Update", command=changeName)

label.pack()
button.pack()

root.mainloop()