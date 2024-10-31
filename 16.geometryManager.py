from tkinter import *

root = Tk()

root.geometry("450x450+650+350")

title = Label(root, text="Abhiram B S", font=(("Verdana"), 15))

name_label = Label(root, text="Your Name: ")
pass_label = Label(root, text="Your Password: ")

name_entry = Entry(root, width=30)
pass_entry = Entry(root, width=30)


button = Button(root, text="Save")


title.place(x=150, y=20)

name_label.place(x=20, y=80)
name_entry.place(x=120, y=80)

pass_label.place(x=20, y=110)
pass_entry.place(x=120, y=110)


button.place(x=270, y=140)

root.mainloop()