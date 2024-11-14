from tkinter import *

root = Tk()

root.geometry("650x650+650+200")

def getData():
    items = listbox.curselection()
    for item in items:
        print(listbox.get(item))

def deleteData():
    items = listbox.curselection()
    for item in items:
        listbox.delete(item)

listbox = Listbox(root, width=40, height=15, selectmode=MULTIPLE)
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

btn1 = Button(root, text="Print", command = getData)
btn2 = Button(root, text="Delete", command = deleteData)

listbox.pack()

btn1.place(x=300, y=250)
btn2.place(x=350, y=250)

root.mainloop()