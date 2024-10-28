from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("350x250")


def deleteMgs():
    mbox = messagebox.askquestion("delete", "Are You Sure Want To Delete the Item")
    if mbox == "yes":
        print("Deleted")
    else:
        print("Not Deleted")


def infoMgs():
    messagebox.showinfo("success", "Well Done")



button1 = ttk.Button(root, text='Button One', command=deleteMgs)
button2 = ttk.Button(root, text='Button Two', command=infoMgs)



button1.grid(row=0, column=0, pady=25, padx=50)
button2.grid(row=0, column=1)


root.mainloop()