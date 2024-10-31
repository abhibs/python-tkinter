from tkinter import *
root = Tk()

root.title("Abhiram B S")

root.geometry("650x650+450+200")


searchbar = LabelFrame(root, text="Search Box")
searchLbl = Label(searchbar, text="Search")
searchbar.pack(side=TOP, pady=30)

entry = Entry(searchbar)
entry.pack(side=LEFT, padx=10, pady=30)

button = Button(searchbar, text="Search")
button.pack(side=LEFT, padx=10)
root.mainloop()