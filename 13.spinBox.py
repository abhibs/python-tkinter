from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x450")

def getValue():
    print("Your Name: "+ entry1.get())
    print("Your Password: "+ entry2.get())

    if chvar.get() == 1:
        print("Remember Me Selected")
    else:
        print("Remember Me Not Selected")

    print("Your Gender is: "+ gender.get())
    print("Month is: "+ months.get())
    print("Year is: "+ year.get())


lbltitle = ttk.Label(text='Abhiram B S', font=(('Arial'), 22))
lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password:')

entry1 = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)

entry1.insert(0, 'Enter Your Name')
entry2.insert(0, 'Enter Your Password')



chvar = IntVar()
chvar.set(0)
cbox = Checkbutton(root, text='Remember Me', variable=chvar, font="Arial 15")


gender = StringVar()
ttk.Radiobutton(root, text='Male', value="male", variable=gender).grid(row=4, column=0)
ttk.Radiobutton(root, text='Female', value="female", variable=gender).grid(row=4, column=1)


months = StringVar()
numbers = []


for i in range(1, 13):
    numbers.append(i)

combobox = ttk.Combobox(root, textvariable=months, values=(numbers), state='readonly')


year = StringVar()
spinbox = Spinbox(root, from_=1997, to=2025, textvariable=year,  state='readonly')

button = ttk.Button(root, text="Login", command=getValue)



lbltitle.grid(row=0, column=0, columnspan=2)
# lblname.grid(row=1, column=0, sticky=W)
lblname.grid(row=1, column=0, sticky=E)
entry1.grid(row=1, column=1)
lblpass.grid(row=2, column=0)
entry2.grid(row=2, column=1)



cbox.grid(row=3, column=1)

combobox.grid(row=5, column=1)

spinbox.grid(row=6, column=1)
# button.grid(row=3, column=1,sticky=E)
# button.grid(row=3, column=1,sticky=W)
# button.grid(row=3, column=1,sticky=E+W) # center(E+W)
button.grid(row=7, column=1,sticky=E+W, pady=5) # center(E+W) , pady means top and bottom, padx means left and right

root.mainloop()
