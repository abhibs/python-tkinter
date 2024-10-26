from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x450")


lbltitle = ttk.Label(text='Abhiram B S', font=(('Arial'), 22))
lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password:')

entry1 = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

entry1.insert(0, 'Enter Your Name')
entry2.insert(0, 'Enter Your Password')

button = ttk.Button(root, text="Login")



lbltitle.grid(row=0, column=0, columnspan=2)
# lblname.grid(row=1, column=0, sticky=W)
lblname.grid(row=1, column=0, sticky=E)
entry1.grid(row=1, column=1)
lblpass.grid(row=2, column=0)
entry2.grid(row=2, column=1)
button.grid(row=3, column=0)

root.mainloop()
