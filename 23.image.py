from tkinter import *

root = Tk()

root.title("Abhiram B S")

root.geometry("350x350")

lbl = Label(root,text="Abhiram B S")
logo = PhotoImage(file='icons/Abhi.png')
lblImage = Label(root, image=logo)


lbl.pack()
lblImage.pack()


root.mainloop()