from tkinter import *
from tkinter import ttk
root = Tk()

root.geometry('500x500')

def getFields():
    val1 = entry.get()
    val2 = entry1.get()

    print("Your Name is: "+val1)
    print("Your Password: " + val2)

entry = Entry(root, width=50)

# placeholder

entry.insert(0, "Abhiram")

# entry with readonly with state

# entry.config(state="disabled")

# entry with readonly with state another method

entry.config(state=DISABLED)

entry1 = ttk.Entry(root, width=50)

# password * showing using config method with show = "*"

entry1.config(show="*")


button = ttk.Button(root, text='Login', command=getFields)

entry.pack()
entry1.pack()
button.pack()

root.mainloop()