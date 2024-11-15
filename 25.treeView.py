from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Abhiram B S")

root.geometry("650x650+650+250")

treeview = ttk.Treeview(root)
treeview.pack()

treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', '2', 'item3', text='Third Item')
treeview.insert('', '3', 'item4', text='Forth Item')
treeview.insert('', '4', 'item5', text='Fifth Item')

treeview.move('item4', 'item1', 'end')
treeview.move('item5', 'item1', 'end')

root.mainloop()