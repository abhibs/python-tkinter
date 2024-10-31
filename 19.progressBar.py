from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Abhiram B S")
root.geometry("450x450+650+350")


progress = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progress.pack(pady=20)
# progress.config(mode='indeterminate')
progress.config(mode='determinate')
progress.start()


root.mainloop()