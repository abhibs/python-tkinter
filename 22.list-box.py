from tkinter import *

root = Tk()

root.geometry("650x650+650+200")

listbox = Listbox(root, width=40, height=15)
listbox.insert(0, "Abhiram")
listbox.insert(1, "Anjan")
listbox.insert(2, "Aravind")
listbox.insert(3, "Anitha")
listbox.insert(4, "Anushree")
listbox.insert(5, "Venkatesh Prasad")
listbox.insert(6, "Krishna Prasad")
listbox.insert(7, "Saritha")
listbox.insert(8, "Surabhi")
listbox.insert(9, "Manu")
listbox.insert(10, "Anuradha")


listbox.pack()

root.mainloop()